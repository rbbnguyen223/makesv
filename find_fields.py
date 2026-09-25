# -*- coding: utf-8 -*-
# find_fields.py - Tim ten truong / lop lien quan den server, phien, dang nhap trong ban goc libApplicationMain.so
# Chay: python find_fields.py      Ket qua: so_fields.txt
import re
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "so_fields.txt"
PAT = re.compile(rb"[\x20-\x7e]{3,}")
KEYS = [b"serv", b"cluster", b"snsid", b"accid", b"sessi", b"host", b"port", b"errorcode", b"transactions",
        b"lasts", b"connect", b"socket", b"login", b"mapping", b"userid", b"token", b"packet", b"opcode"]
CTX_CENTER = 0x00CFC008   # vi tri chuoi ".../gateway2.php?func=listS&version="
CTX_RANGE = 0x600

lines = []
apks = sorted(BASE.glob("*.apk"))
if not apks:
    raise SystemExit("Khong thay file .apk")
with zipfile.ZipFile(apks[0]) as z:
    data = z.read("lib/armeabi/libApplicationMain.so")

lines.append(f"===== A. Chuoi xung quanh URL listS (0x{CTX_CENTER - CTX_RANGE:X}..0x{CTX_CENTER + CTX_RANGE:X}) =====")
for m in PAT.finditer(data, CTX_CENTER - CTX_RANGE, CTX_CENTER + CTX_RANGE):
    lines.append(f"0x{m.start():08X}  {m.group()[:160].decode('ascii', 'replace')}")

lines.append("")
lines.append("===== B. Chuoi chua tu khoa server/phien/dang nhap (toan bo .so) =====")
seen = set()
n = 0
for m in PAT.finditer(data):
    s = m.group()
    if len(s) > 90 or s in seen:
        continue
    low = s.lower()
    if any(k in low for k in KEYS):
        seen.add(s)
        lines.append(f"0x{m.start():08X}  {s.decode('ascii', 'replace')}")
        n += 1
        if n >= 1500:
            lines.append("... (cat bot)")
            break

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Da ghi {OUT} ({len(lines)} dong)")
