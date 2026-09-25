import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

try:
    import subprocess
    
    import time
    device = None
    while not device:
        try:
            manager = frida.get_device_manager()
            device = manager.get_device('emulator-5554')
        except:
            time.sleep(1)
    print("[*] Found device:", device.name)
    print("[*] Found device:", device.name)
    
    import time
    session = None
    import subprocess
    print("[*] Waiting for lmah.vn to start...")
    pid = None
    while not pid:
        try:
            p = device.get_process("Lien Minh")
            pid = p.pid
        except frida.ProcessNotFoundError:
            time.sleep(0.5)
        except Exception as e:
            time.sleep(0.5)
            
    print(f"[*] Found PID {pid}, attaching...")
    session = device.attach(pid)
    
    print("[*] Waiting for libApplicationMain.so in maps...")
    base_address = None
    while not base_address:
        try:
            result = subprocess.run(["adb", "shell", "su", "-c", f"'cat /proc/{pid}/maps | grep libApplicationMain.so'"], capture_output=True, text=True)
            output = result.stdout
            if output:
                for line in output.splitlines():
                    if "libApplicationMain.so" in line and ("r-xp" in line or "r--p" in line):
                        parts = line.split()
                        # offset check to get the actual base
                        if parts[2] == "00000000":
                            base_address = parts[0].split("-")[0]
                            break
        except Exception as e:
            pass
        if not base_address:
            time.sleep(1)
            
    print(f"[*] Module loaded at 0x{base_address}! Injecting script...")
    
    with open("hook_new.js") as f:
        script_code = f.read()
        
    script_code = f"var MANUAL_BASE_ADDRESS = ptr('0x{base_address}');\n" + script_code
    
    script = session.create_script(script_code)
    script.on('message', on_message)
    script.load()
    
    print("[*] Hook loaded!")
    sys.stdin.read()
except Exception as e:
    print(f"Error: {e}")
