import subprocess
import time
import sys

DEVICE = "emulator-5554"

def adb(cmd):
    full_cmd = f"adb -s {DEVICE} {cmd}"
    res = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip()

def ensure_hosts_redirect():
    print(f"[0] Kiem tra quyen root va cau hinh hosts cho {DEVICE} tro ve 127.0.0.1...")
    adb("root")
    time.sleep(2)

    hosts_content = (
        "127.0.0.1 localhost lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn\n"
    )
    with open("hosts_new.txt", "w", encoding="utf-8") as f:
        f.write(hosts_content)

    adb("push hosts_new.txt /data/local/tmp/hosts_new")
    adb('shell "mount -o rw,remount /system >/dev/null 2>&1 || mount -o rw,remount / >/dev/null 2>&1"')
    adb('shell "cp /data/local/tmp/hosts_new /etc/hosts >/dev/null 2>&1"')
    adb('shell "cp /data/local/tmp/hosts_new /system/etc/hosts >/dev/null 2>&1"')
    adb('shell "mount -o bind /data/local/tmp/hosts_new /system/etc/hosts >/dev/null 2>&1"')
    adb('shell "mount -o bind /data/local/tmp/hosts_new /etc/hosts >/dev/null 2>&1"')

    current = adb("shell cat /system/etc/hosts")
    if "127.0.0.1" in current and "lienminh.g6-mobile.zing.vn" in current:
        print("    [OK] Hosts da duoc tro thanh cong ve 127.0.0.1!")
    else:
        print("    [CANH BAO] Hosts chua ghi de duoc:")
        print("    " + current.replace("\n", "\n    "))

    print("[0.1] Thiet lap adb reverse cho cong 80 va 8888...")
    adb("reverse --remove-all")
    adb("reverse tcp:80 tcp:80")
    adb("reverse tcp:8888 tcp:8888")
    adb("reverse tcp:8080 tcp:80")
    adb('shell "iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-ports 8080 >/dev/null 2>&1"')

ensure_hosts_redirect()

print("[1] Restarting app...")
adb("shell am force-stop lmah.vn")
adb("shell am start -n lmah.vn/lmah.vn.MainActivity")

print("[2] Waiting 7s for splash / login popup...")
time.sleep(7)

print("[3] Tapping Choi ngay (270, 729)...")
adb("shell input tap 270 729")
time.sleep(4)

print("[4] Tapping VAO GAME (270, 805)...")
adb("shell input tap 270 805")
time.sleep(5)
adb("shell screencap -p /sdcard/screen_vao.png")
adb("pull /sdcard/screen_vao.png screen_vao.png")

print("[5] Selecting hero (Xa Thu 180, 350)...")
adb("shell input tap 180 350")
time.sleep(1)

print("[5.1] Tapping Name Box (270, 770) & entering name...")
adb("shell input tap 270 770")
time.sleep(1)
adb("shell input text AnhHoang")
time.sleep(1)
# Bấm phím Enter / ẩn bàn phím
adb("shell input keyevent 66")
time.sleep(1)

print("[6] Tapping Tham Gia (268, 880)...")
adb("shell input tap 268 842")
time.sleep(5)

print("[7] Checking screen...")
adb("shell screencap -p /sdcard/screen.png")
adb("pull /sdcard/screen.png current_screen.png")
print("Done! Screenshot pulled to current_screen.png")
