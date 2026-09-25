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
        var targets = [
            ptr("0xb3832508"), // Start of object containing pointer to string 1
            ptr("0xb48ad6d8")  // Start of object containing pointer to string 2
        ];
        
        send("Scanning for pointers to: " + targets.join(", "));
        
        var ranges = Process.enumerateRanges('r--');
        var count = 0;
        
        targets.forEach(function(addr) {
            var a = addr.toUInt32();
            var p1 = (a & 0xff).toString(16).padStart(2, '0');
            var p2 = ((a >> 8) & 0xff).toString(16).padStart(2, '0');
            var p3 = ((a >> 16) & 0xff).toString(16).padStart(2, '0');
            var p4 = ((a >> 24) & 0xff).toString(16).padStart(2, '0');
            var ptr_pattern = p1 + " " + p2 + " " + p3 + " " + p4;
            
            send("Scanning for ptr: " + ptr_pattern + " -> " + addr);
            
            ranges.forEach(function(range) {
                try {
                    var res = Memory.scanSync(range.base, range.size, ptr_pattern);
                    res.forEach(function(match) {
                        count++;
                        send("Found PTR to " + addr + " at " + match.address + " in " + range.base);
                        try {
                            var mem = match.address.sub(16).readByteArray(64);
                            send("Dump:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
                        } catch(e) {}
                    });
                } catch (e) {}
            });
        });
        
        send("Total level-2 pointers found: " + count);
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
