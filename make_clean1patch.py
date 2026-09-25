# -*- coding: utf-8 -*-
# make_clean1patch.py
# Tạo libApplicationMain_clean1patch.so từ bản gốc trong APK,
# chỉ áp dụng DUY NHẤT 1 vá tại 0x4D9984 (bypass user_leveling / license check).
# Bỏ hoàn toàn 3 vá kia (0x7AC874, 0x7AF920, 0x7B0F80) đã xác nhận là SAI.
#
# Chạy: python make_clean1patch.py
# Output: libApplicationMain_clean1patch.so  (cùng thư mục)
# Sau đó: adb push libApplicationMain_clean1patch.so <đường dẫn trong LDPlayer>

import struct
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
APK = next(BASE.glob("*.apk"), None)
if APK is None:
    raise SystemExit("Không tìm thấy file .apk trong thư mục")

print(f"Đọc từ APK: {APK.name}")
with zipfile.ZipFile(APK) as z:
    data = bytearray(z.read("lib/armeabi/libApplicationMain.so"))

print(f"Kích thước .so gốc: {len(data)} bytes")

# ==============================================================================
# PATCH DUY NHẤT: 0x4D9984 — ép hàm user_leveling trả về 1 ngay lập tức
# Gốc (8 bytes): c8 3f 9f e5 0d 20 a0 e3  (ldr r3,[pc,#0xfc8] ; mov r2,#0xd)
# Mới  (8 bytes): 01 00 a0 e3 1e ff 2f e1  (mov r0,#1 ; bx lr)
# Ý nghĩa: hàm kiểm tra phiên bản/license trả về 1 = OK, bỏ qua toàn bộ logic
# ==============================================================================
PATCHES = [
    (0x4D9984, bytes([0xc8, 0x3f, 0x9f, 0xe5, 0x0d, 0x20, 0xa0, 0xe3]),
               bytes([0x01, 0x00, 0xa0, 0xe3, 0x1e, 0xff, 0x2f, 0xe1]),
     "bypass user_leveling / license check"),
]

for offset, expected, replacement, label in PATCHES:
    actual = bytes(data[offset:offset + len(expected)])
    if actual != expected:
        raise SystemExit(
            f"ABORT: offset 0x{offset:X} không khớp!\n"
            f"  Mong đợi: {expected.hex()}\n"
            f"  Thực tế:  {actual.hex()}\n"
            "Kiểm tra lại APK hoặc offset."
        )
    data[offset:offset + len(replacement)] = replacement
    print(f"✓ Patch 0x{offset:X}: {label}")
    print(f"  {expected.hex()} -> {replacement.hex()}")

OUT = BASE / "libApplicationMain_clean1patch.so"
OUT.write_bytes(data)
print(f"\nGhi ra: {OUT.name} ({len(data)} bytes)")
print("\nBước tiếp theo:")
print("  adb.exe push libApplicationMain_clean1patch.so /data/local/tmp/")
print("  (xem push_so.bat để push và cài tự động)")
