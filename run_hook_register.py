import frida
import sys
import subprocess
import time

def on_message(message, data):
    if message['type'] == 'send':
        print(f"[FRIDA] {message['payload']}", flush=True)
    else:
        print(f"[FRIDA ERROR] {message}", flush=True)

try:
    manager = frida.get_device_manager()
    device = manager.get_device('emulator-5554')
    print("[*] Device connected:", device.name, flush=True)

    # find PID of lmah.vn
    res = subprocess.run(["adb", "shell", "pidof lmah.vn"], capture_output=True, text=True)
    pid_str = res.stdout.strip()
    if not pid_str:
        print("[-] lmah.vn is not running!", flush=True)
        sys.exit(1)
    
    pid = int(pid_str.split()[0])
    print(f"[*] Attaching to lmah.vn (PID {pid})...", flush=True)
    session = device.attach(pid)

    with open("hook_register.js", "r", encoding="utf-8") as f:
        code = f.read()

    script = session.create_script(code)
    script.on('message', on_message)
    script.load()
    print("[*] Frida hook_register.js loaded successfully! Listening...", flush=True)
    
    # keep alive
    while True:
        time.sleep(1)

except Exception as e:
    print(f"[-] Frida Error: {e}", flush=True)
