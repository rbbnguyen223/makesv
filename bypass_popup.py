# bypass_popup.py
# Chay: python bypass_popup.py
#
# BAT BUOC DIEN 2 GIA TRI NAY TRUOC KHI CHAY (lay tu Ghidra theo Buoc 1 trong phantich.md:
# search_strings "Dang tai du lieu" hoac "Xin cho giay lat" -> get_xrefs_to -> tim FUNC_SHOW
# va ham anh em FUNC_HIDE cung class):
FUNC_SHOW_OFFSET = "0x0000000"   # <-- DIEN OFFSET THAT VAO DAY (hex, vd "0x6f65ac")
FUNC_HIDE_OFFSET = "0x0000000"   # <-- DIEN OFFSET THAT VAO DAY

# Ten process CHINH XAC de attach - Luu y: du an nay tung phat hien process name thuc te
# la "Lien Minh", KHONG PHAI "lmah.vn" (xem lich su TONG_HOP.md / doan chat 23/09) -
# attach sai ten se khien Frida khong bao gio thay tien trinh.
PROCESS_NAME = "Lien Minh"

LIB_NAME = "libApplicationMain.so"

import subprocess
import sys
import time

try:
    import frida
except ImportError:
    print("[!] Chua cai module 'frida' (pip install frida). Dung lai.")
    sys.exit(1)


def adb(args):
    res = subprocess.run(["adb"] + args, capture_output=True, text=True)
    return res.stdout.strip(), res.stderr.strip()


def get_pid(process_name):
    out, _ = adb(["shell", "pidof", process_name])
    if not out:
        # fallback: pidof khong nhan ten co dau cach -> thu qua ps
        out2, _ = adb(["shell", "ps", "-A"])
        for line in out2.splitlines():
            if process_name.replace(" ", "") in line.replace(" ", "") or "lmah.vn" in line:
                parts = line.split()
                if len(parts) > 1 and parts[1].isdigit():
                    return int(parts[1])
        return None
    return int(out.split()[0])


def get_base_address(pid, lib_name):
    """
    Doc /proc/pid/maps, lay dia chi THAP NHAT cua lib_name (dong r--p, offset 000000)
    - KHONG duoc lay nham dong r-xp (offset khac 0) vi se tinh sai base.
    """
    out, err = adb(["shell", "su", "-c", f"cat /proc/{pid}/maps"])
    if not out:
        print(f"[!] Khong doc duoc /proc/{pid}/maps. stderr: {err}")
        return None

    candidates = []
    for line in out.splitlines():
        if lib_name in line:
            addr_range = line.split()[0]
            base_hex = addr_range.split("-")[0]
            candidates.append(int(base_hex, 16))

    if not candidates:
        print(f"[!] Khong tim thay '{lib_name}' trong maps cua pid {pid}.")
        return None

    base = min(candidates)  # dia chi thap nhat = base that
    return base


def main():
    if FUNC_SHOW_OFFSET == "0x0000000" or FUNC_HIDE_OFFSET == "0x0000000":
        print("[!] Chua dien FUNC_SHOW_OFFSET / FUNC_HIDE_OFFSET o dau file. Dien xong roi chay lai.")
        sys.exit(1)

    print(f"[1] Tim PID cua '{PROCESS_NAME}' ...")
    pid = get_pid(PROCESS_NAME)
    if pid is None:
        print(f"[!] Khong tim thay PID. Kiem tra app da mo chua, hoac PROCESS_NAME dung chua.")
        sys.exit(1)
    print(f"    PID = {pid}")

    print(f"[2] Doc base address cua {LIB_NAME} tu /proc/{pid}/maps ...")
    base = get_base_address(pid, LIB_NAME)
    if base is None:
        sys.exit(1)
    print(f"    BASE_ADDRESS = {hex(base)}")

    print("[3] Doc mau JS va thay the placeholder ...")
    with open("hook_bypass.js", "r", encoding="utf-8") as f:
        js_template = f.read()

    js_code = (
        js_template
        .replace("__BASE_ADDRESS__", hex(base))
        .replace("__FUNC_SHOW_OFFSET__", FUNC_SHOW_OFFSET)
        .replace("__FUNC_HIDE_OFFSET__", FUNC_HIDE_OFFSET)
    )

    print("[4] Dinh device + attach process qua Frida ...")
    device = frida.get_usb_device(timeout=10)
    session = device.attach(pid)

    print("[5] Nap script vao process ...")
    script = session.create_script(js_code)

    def on_message(message, data):
        if message["type"] == "send":
            print("[JS] " + str(message["payload"]))
        elif message["type"] == "error":
            print("[JS ERROR] " + message.get("description", str(message)))
            print("           " + message.get("stack", ""))
        else:
            print("[JS RAW] " + str(message))

    script.on("message", on_message)
    script.load()

    print("[6] Dang theo doi log (Ctrl+C de dung). Bay gio hay bam THAM GIA trong game neu chua tap...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Dung theo doi. Thoat.")


if __name__ == "__main__":
    main()
