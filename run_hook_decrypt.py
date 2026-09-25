import frida
import sys
import time

log_file = open("frida_log_decrypt.txt", "w", encoding="utf-8")

def log(msg):
    print(msg, flush=True)
    log_file.write(msg + "\n")
    log_file.flush()

def on_message(message, data):
    if message['type'] == 'send':
        log(f"[*] {message['payload']}")
    elif message['type'] == 'error':
        log(f"[!] {message['stack']}")
    else:
        log(f"[*] {message}")
    if data:
        log(f"    Data: {data.hex()}")

def main():
    device = frida.get_usb_device()
    session = None
    log("[+] Waiting for Lien Minh to start...")
    while True:
        try:
            session = device.attach("Lien Minh")
            break
        except frida.ProcessNotFoundError:
            time.sleep(1)
        except Exception as e:
            log(f"[-] Error: {e}")
            time.sleep(1)
            
    log("[+] Attached to Lien Minh!")
    
    with open("hook_decrypt.js", "r", encoding="utf-8") as f:
        script_code = f.read()
        
    script = session.create_script(script_code)
    script.on('message', on_message)
    script.load()
    
    log("[+] Script loaded. Listening...")
    sys.stdin.read()

if __name__ == '__main__':
    main()
