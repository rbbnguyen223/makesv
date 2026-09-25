import frida
import sys

def on_message(message, data):
    print(message)

device = frida.get_usb_device()
process = device.get_process('Lien Minh')
session = device.attach(process.pid)
script = session.create_script("""
var throwPtr = Module.findExportByName(null, '__cxa_throw');
if (throwPtr) {
    Interceptor.attach(throwPtr, {
        onEnter: function(args) {
            send('Exception thrown!\\n' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\\n'));
        }
    });
} else {
    send('__cxa_throw not found');
}
""")
script.on('message', on_message)
script.load()
sys.stdin.read()
