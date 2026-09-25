import frida
import sys
import time

dev = frida.get_usb_device()
process = dev.get_process('Lien Minh')
session = dev.attach(process.pid)

script_code = """
var recvPtr = Module.findGlobalExportByName("recv");
if (recvPtr) {
    Interceptor.attach(recvPtr, {
        onEnter: function(args) {
            this.fd = args[0].toInt32();
            this.buf = args[1];
            this.len = args[2].toInt32();
        },
        onLeave: function(retval) {
            var n = retval.toInt32();
            if (n > 0) {
                var hex = "";
                var max = Math.min(n, 32);
                for (var i = 0; i < max; i++) {
                    var b = this.buf.add(i).readU8().toString(16);
                    if (b.length == 1) b = "0" + b;
                    hex += b + " ";
                }
                send('[RECV fd=' + this.fd + ' len=' + n + ']: ' + hex);
            }
        }
    });
    send('[OK] recv hooked at ' + recvPtr);
}

var sendPtr = Module.findGlobalExportByName("send");
if (sendPtr) {
    Interceptor.attach(sendPtr, {
        onEnter: function(args) {
            var fd = args[0].toInt32();
            var buf = ptr(args[1]);
            var len = args[2].toInt32();
            var hex = "";
            var max = Math.min(len, 32);
            for (var i = 0; i < max; i++) {
                var b = buf.add(i).readU8().toString(16);
                if (b.length == 1) b = "0" + b;
                hex += b + " ";
            }
            send('[SEND fd=' + fd + ' len=' + len + ']: ' + hex);
        }
    });
    send('[OK] send hooked at ' + sendPtr);
}

var connectPtr = Module.findGlobalExportByName("connect");
if (connectPtr) {
    Interceptor.attach(connectPtr, {
        onEnter: function(args) {
            var fd = args[0].toInt32();
            var sa = ptr(args[1]);
            try {
                var family = sa.readU16();
                if (family === 2) {
                    var port = ((sa.add(2).readU8() << 8) | sa.add(3).readU8());
                    var ip = sa.add(4).readU8() + '.' + sa.add(5).readU8() + '.' + sa.add(6).readU8() + '.' + sa.add(7).readU8();
                    send('[CONNECT fd=' + fd + ']: ' + ip + ':' + port);
                }
            } catch(e) {}
        }
    });
    send('[OK] connect hooked at ' + connectPtr);
}
"""

script = session.create_script(script_code)
def on_msg(m, d):
    if m['type'] == 'send':
        print(m['payload'])
        sys.stdout.flush()
    else:
        print('[FRIDA ERROR]', m)
        sys.stdout.flush()
script.on('message', on_msg)
script.load()
print('[*] Script loaded. Running...')
sys.stdout.flush()

while True:
    time.sleep(1)
