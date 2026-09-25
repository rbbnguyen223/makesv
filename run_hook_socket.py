import frida
import sys
import time

def on_message(message, data):
    if message['type'] == 'send':
        print(f"[*] {message['payload']}")
    else:
        print(f"[frida] {message}")

def main():
    manager = frida.get_device_manager()
    device = manager.get_device('emulator-5554')
    print(f"[*] Connected to device: {device.name}")
    
    import subprocess
    print("[*] Waiting for lmah.vn process...")
    session = None
    while session is None:
        try:
            pid_str = subprocess.check_output(['adb', '-s', 'emulator-5554', 'shell', 'pidof', 'lmah.vn']).decode().strip()
            if pid_str:
                pid = int(pid_str)
                session = device.attach(pid)
            else:
                time.sleep(0.5)
        except Exception as e:
            time.sleep(0.5)
            
    print(f"[*] Attached to lmah.vn (PID: {pid})")
    
    with open("hook_socket.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    script = session.create_script(js)
    script.on('message', on_message)
    script.load()
    print("[*] hook_socket.js loaded and active. Listening for events...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[*] Detaching...")
        session.detach()

if __name__ == "__main__":
    main()
