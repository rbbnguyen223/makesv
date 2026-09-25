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
        var ptr1 = "70 4a 6f 05"; // 0x56f4a70
        var ptr2 = "ac d6 0a b9"; // 0xb90ad6ac
        
        send("Scanning for pointers: " + ptr1 + " and " + ptr2);
        
        var ranges = Process.enumerateRanges('r--');
        var count = 0;
        
        ranges.forEach(function(range) {
            try {
                var res1 = Memory.scanSync(range.base, range.size, ptr1);
                res1.forEach(function(match) {
                    count++;
                    send("Found PTR1 at " + match.address + " in " + range.base + " (" + range.size + ")");
                    try {
                        var mem = match.address.sub(16).readByteArray(64);
                        send("Dump:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
                    } catch(e) {}
                });
                
                var res2 = Memory.scanSync(range.base, range.size, ptr2);
                res2.forEach(function(match) {
                    count++;
                    send("Found PTR2 at " + match.address + " in " + range.base + " (" + range.size + ")");
                    try {
                        var mem = match.address.sub(16).readByteArray(64);
                        send("Dump:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
                    } catch(e) {}
                });
            } catch (e) {}
        });
        
        send("Total pointers found: " + count);
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
