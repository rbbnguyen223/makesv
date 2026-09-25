import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print(f"[*] {message['payload']}")
    elif message['type'] == 'error':
        print(f"[-] {message['stack']}")

js_code = """
rpc.exports = {
    scan: function() {
        var base = ptr("0x4a00000");
        var size = 0xDDCE00; // hardcoded size for libApplicationMain.so
        
        // We are looking for the pointer to typeinfo of Popup_obj
        // typeinfo offset is 0xE705C0. At runtime it is base + 0xE705C0.
        var ti_addr = base.add(0xE705C0);
        
        var a = ti_addr.toInt32();
        var p1 = (a & 0xff).toString(16).padStart(2, '0');
        var p2 = ((a >> 8) & 0xff).toString(16).padStart(2, '0');
        var p3 = ((a >> 16) & 0xff).toString(16).padStart(2, '0');
        var p4 = ((a >>> 24) & 0xff).toString(16).padStart(2, '0');
        var ptr_pattern = p1 + " " + p2 + " " + p3 + " " + p4;
        
        send("Scanning libApplicationMain.so for vtable containing typeinfo pointer: " + ptr_pattern + " (" + ti_addr + ")");
        
        var res = Memory.scanSync(base, size, ptr_pattern);
        res.forEach(function(match) {
            send("Found vtable at " + match.address + " (offset: 0x" + match.address.sub(base).toString(16) + ")");
            try {
                // Read the vtable functions
                send("Vtable functions:");
                for(var i = 1; i <= 10; i++) {
                    var funcPtr = match.address.add(i*4).readPointer();
                    send("  [" + i + "] " + funcPtr + " (offset: 0x" + funcPtr.sub(base).toString(16) + ")");
                }
            } catch(e) {}
        });
        send("Total vtables found: " + res.length);
    }
};
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
    
    script.exports.scan()
    session.detach()
except Exception as e:
    print(f"Error: {e}")
