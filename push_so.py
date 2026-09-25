# -*- coding: utf-8 -*-
# push_so.py - Tạo .so 1-patch và cài vào LDPlayer đúng path
# Chạy: python push_so.py
import subprocess, sys, zipfile, struct
from pathlib import Path

BASE = Path(__file__).resolve().parent

def adb(*args):
    result = subprocess.run(["adb.exe"] + list(args), capture_output=True, text=True, cwd=BASE)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def adb_shell(cmd):
    return adb("shell", cmd)

# ==== Bước 1: Tạo .so 1-patch ====
print("[1/4] Tạo libApplicationMain_clean1patch.so...")
APK = next(BASE.glob("*.apk"), None)
if not APK:
    sys.exit("Không tìm thấy .apk")

with zipfile.ZipFile(APK) as z:
    data = bytearray(z.read("lib/armeabi/libApplicationMain.so"))

# Vá DUY NHẤT: 0x4D9984 bypass user_leveling
offset   = 0x4D9984
expected = bytes([0xc8, 0x3f, 0x9f, 0xe5, 0x0d, 0x20, 0xa0, 0xe3])
new_code = bytes([0x01, 0x00, 0xa0, 0xe3, 0x1e, 0xff, 0x2f, 0xe1])

if bytes(data[offset:offset+8]) != expected:
    sys.exit(f"ABORT: offset 0x{offset:X} không khớp — kiểm tra lại APK")

data[offset:offset+8] = new_code
OUT = BASE / "libApplicationMain_clean1patch.so"
OUT.write_bytes(data)
print(f"  ✓ Đã tạo {OUT.name} ({len(data)} bytes)")

# ==== Bước 2: Bật root, push lên tmp ====
print("[2/4] Bật root và push lên /data/local/tmp/...")
adb("root")
import time; time.sleep(3)

out, err, rc = adb("push", str(OUT), "/data/local/tmp/libApplicationMain_new.so")
if rc != 0:
    sys.exit(f"FAILED push: {err}")
print(f"  ✓ Push OK")

# ==== Bước 3: Tìm path đúng trong LDPlayer ====
print("[3/4] Tìm path libApplicationMain.so trong /data/app/...")
adb_shell("am force-stop lmah.vn")
time.sleep(1)

out, err, rc = adb_shell("find /data/app -name libApplicationMain.so 2>/dev/null")
paths = [p.strip() for p in out.splitlines() if "lmah.vn" in p and p.strip().endswith("libApplicationMain.so")]

if not paths:
    # Thử cách khác: tìm qua pm path
    out2, _, _ = adb_shell("pm path lmah.vn")
    print(f"  pm path: {out2}")
    # output: package:/data/app/~~xxx==/lmah.vn-yyy==/base.apk
    if "package:" in out2:
        apk_path = out2.replace("package:", "").strip()
        lib_path = apk_path.replace("base.apk", "lib/arm/libApplicationMain.so")
        paths = [lib_path]
    else:
        sys.exit(f"FAILED: Không tìm thấy path. find output: {out!r}")

so_path = paths[0]
print(f"  ✓ Tìm thấy: {so_path}")

# ==== Bước 4: Copy và set quyền ====
print("[4/4] Copy vào vị trí và set quyền...")
out, err, rc = adb_shell(f"cp /data/local/tmp/libApplicationMain_new.so '{so_path}'")
if rc != 0:
    print(f"  cp lỗi (rc={rc}): {err}")
    # Thử dùng cat thay vì cp (một số ROM giới hạn cp)
    out, err, rc = adb_shell(f"cat /data/local/tmp/libApplicationMain_new.so > '{so_path}'")
    if rc != 0:
        sys.exit(f"FAILED copy: {err}")

adb_shell(f"chmod 755 '{so_path}'")

# Kiểm tra
out, err, _ = adb_shell(f"ls -la '{so_path}'")
print(f"  Kết quả: {out}")

print()
print("=== XONG ===")
print(f".so 1-patch đã cài tại: {so_path}")
print("Bây giờ chạy cycle.bat để test.")
