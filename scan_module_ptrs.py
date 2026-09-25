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
        
        var targetAddr = base.add(0xCF4A70);
        send("Target string address: " + targetAddr);
        
        // Convert integer pointer back to bytes for scanning
        var a = targetAddr.toInt32();
        var p1 = (a & 0xff).toString(16).padStart(2, '0');
        var p2 = ((a >> 8) & 0xff).toString(16).padStart(2, '0');
        var p3 = ((a >> 16) & 0xff).toString(16).padStart(2, '0');
        var p4 = ((a >>> 24) & 0xff).toString(16).padStart(2, '0');
        var ptr_pattern = p1 + " " + p2 + " " + p3 + " " + p4;
        
        send("Scanning libApplicationMain.so for pointer: " + ptr_pattern);
        
        var res = Memory.scanSync(base, size, ptr_pattern);
        res.forEach(function(match) {
            send("Found direct pointer at " + match.address + " (offset: 0x" + match.address.sub(base).toString(16) + ")");
            try {
                var mem = match.address.sub(16).readByteArray(64);
                send("Dump:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
            } catch(e) {}
        });
        send("Total direct pointers found: " + res.length);
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
