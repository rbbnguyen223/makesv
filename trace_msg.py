import frida
import sys
import time

dev = frida.get_device('emulator-5554')
session = dev.attach(3143)

script_code = """
var base = ptr('0x04a00000');

function dumpMap(mapObj) {
    if (!mapObj || mapObj.isNull()) return 'null';
    try {
        // try to inspect haxe.ds.StringMap
        return 'mapObj=' + mapObj;
    } catch(e) {
        return 'err:' + e;
    }
}

// FBClient_onMessage Ghidra: 0x008acdf4 -> ELF offset: 0x0089cdf4
var onMsgAddr = base.add(0x0089cdf4);
send('[FRIDA] Hooking FBClient_onMessage at ' + onMsgAddr);

Interceptor.attach(onMsgAddr, {
    onEnter: function(args) {
        send('[FRIDA] >>> FBClient_onMessage called! client=' + args[0] + ' msg=' + args[1]);
        this.client = args[0];
        this.msg = args[1];
    },
    onLeave: function(retval) {
        send('[FRIDA] <<< FBClient_onMessage returned: ' + retval);
    }
});

// Also hook recv to see raw data received
var recvPtr = Module.findExportByName("libc.so", "recv");
if (recvPtr) {
    Interceptor.attach(recvPtr, {
        onEnter: function(args) {
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
                send('[FRIDA] recv(' + n + ' bytes): ' + hex);
            }
        }
    });
}
"""

script = session.create_script(script_code)
def on_msg(m, d):
    if m['type'] == 'send':
        print(m['payload'])
    else:
        print('[FRIDA ERROR]', m)
script.on('message', on_msg)
script.load()
print('[*] Script loaded. Running...')
sys.stdout.flush()

time.sleep(1)
