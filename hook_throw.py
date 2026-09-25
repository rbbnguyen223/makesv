import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print(f"[*] {message['payload']}")
    elif message['type'] == 'error':
        print(f"[-] {message['stack']}")

js_code = """
var cxa_throw = null;
try {
    var m = Process.getModuleByName("libc.so");
    var exports = m.enumerateExports();
    for (var i = 0; i < exports.length; i++) {
        if (exports[i].name === "__cxa_throw") {
            cxa_throw = exports[i].address;
            break;
        }
    }
} catch(e) {}

if (!cxa_throw) {
    try {
        var m2 = Process.getModuleByName("libc++_shared.so");
        var exports = m2.enumerateExports();
        for (var i = 0; i < exports.length; i++) {
            if (exports[i].name === "__cxa_throw") {
                cxa_throw = exports[i].address;
                break;
            }
        }
    } catch(e) {}
}

if (cxa_throw) {
    send("Hooking __cxa_throw at " + cxa_throw);
    Interceptor.attach(cxa_throw, {
        onEnter: function(args) {
            send("Exception thrown!");
            var trace = Thread.backtrace(this.context, Backtracer.ACCURATE);
            var str = "";
            for (var i = 0; i < trace.length; i++) {
                var sym = DebugSymbol.fromAddress(trace[i]);
                str += sym.toString() + "\\n";
            }
            send("Backtrace:\\n" + str);
        }
    });
} else {
    send("Could not find __cxa_throw");
}
"""

try:
    print("[*] Connecting to game...")
    device = frida.get_usb_device()
    import subprocess
    pid_str = subprocess.check_output(['adb', '-s', 'emulator-5554', 'shell', 'pidof', 'lmah.vn']).decode().strip()
    pid = int(pid_str)
    session = device.attach(pid)
    script = session.create_script(js_code)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()
except Exception as e:
    print(f"Error: {e}")
