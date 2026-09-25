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
        var pattern = "54 45 58 54 5f 41 4c 49 47 4e 5f 43 45 4e 54 45 52 5f 4c 4f 41 44 49 4e 47 5f 44 41 54 41"; 
        send("Start scanning for pattern: " + pattern);
        
        var ranges = Process.enumerateRanges('r--');
        send("Ranges to scan: " + ranges.length);
        
        var matches_found = 0;
        var found_addresses = [];
        
        ranges.forEach(function(range) {
            try {
                var results = Memory.scanSync(range.base, range.size, pattern);
                if (results.length > 0) {
                    results.forEach(function(match) {
                        matches_found++;
                        found_addresses.push(match.address);
                        send("Found string at " + match.address + " in range base: " + range.base);
                    });
                }
            } catch (e) {}
        });
        
        send("String scan complete. Matches: " + matches_found);
        
        if (found_addresses.length > 0) {
            send("Scanning for pointers to found strings...");
            var ptr_count = 0;
            found_addresses.forEach(function(addr) {
                // Address to Little Endian hex string
                var a = addr.toUInt32();
                var p1 = (a & 0xff).toString(16).padStart(2, '0');
                var p2 = ((a >> 8) & 0xff).toString(16).padStart(2, '0');
                var p3 = ((a >> 16) & 0xff).toString(16).padStart(2, '0');
                var p4 = ((a >> 24) & 0xff).toString(16).padStart(2, '0');
                var ptr_pattern = p1 + " " + p2 + " " + p3 + " " + p4;
                
                send("Scanning for ptr: " + ptr_pattern + " (address: " + addr + ")");
                
                ranges.forEach(function(range) {
                    try {
                        var res = Memory.scanSync(range.base, range.size, ptr_pattern);
                        res.forEach(function(match) {
                            ptr_count++;
                            send("Found PTR at " + match.address + " in " + range.base);
                            try {
                                var mem = match.address.sub(16).readByteArray(64);
                                send("Dump:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
                            } catch(e) {}
                        });
                    } catch(e) {}
                });
            });
            send("Pointer scan complete. Total pointers found: " + ptr_count);
        }
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
