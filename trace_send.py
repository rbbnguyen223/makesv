import frida
import sys

def on_message(message, data):
    print(message)

device = frida.get_usb_device()
process = device.get_process('Lien Minh')
session = device.attach(process.pid)
script = session.create_script("""
var sendPtr = Module.findExportByName('libc.so', 'send');
if (sendPtr) {
    Interceptor.attach(sendPtr, {
        onEnter: function(args) {
            var fd = args[0].toInt32();
            var buf = args[1];
            var len = args[2].toInt32();
            if (fd > 2) {
                var data = buf.readByteArray(len);
                send('send fd=' + fd + ' len=' + len, data);
            }
        }
    });
}
""")
script.on('message', on_message)
script.load()
sys.stdin.read()
