import frida

js_code = """
rpc.exports = {
    scan: function() {
        try {
            var mem = ptr("0xb3832464").readByteArray(64);
            send("Dump 0xb3832464:\\n" + hexdump(mem, { offset: 0, length: 64, header: true, ansi: false }));
        } catch(e) {
            send("Error: " + e);
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
    script.on('message', lambda m, d: print(m['payload']) if m['type'] == 'send' else print(m))
    script.load()
    script.exports.scan()
    session.detach()
except Exception as e:
    print(f"Error: {e}")
