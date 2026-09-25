import frida
import sys

def on_message(message, data):
    print(message)

device = frida.get_usb_device()
session = device.attach(3351)
script = session.create_script("""
var closePtr = Module.findExportByName('libc.so', 'close');
if (closePtr) {
    Interceptor.attach(closePtr, {
        onEnter: function(args) {
            var fd = args[0].toInt32();
            if (fd > 2) {
                var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\\n');
                if (trace.indexOf('libApplicationMain') !== -1) {
                    send('close fd=' + fd + '\\n' + trace);
                }
            }
        }
    });
}
""")
script.on('message', on_message)
script.load()
sys.stdin.read()
