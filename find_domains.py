# -*- coding: utf-8 -*-
# find_domains.py - Tim cac chuoi giong dia chi/ten mien trong ban goc libApplicationMain.so va classes.dex
# Chay:  python find_domains.py      Ket qua: so_strings.txt
import re
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "so_strings.txt"
KEYS = [b"http", b".vn", b".com", b".net", b"zing", b"lienminh", b"lmah", b"gateway", b"lmadmin", b"cdn", b"192.168", b"8888"]
PAT = re.compile(rb"[\x20-\x7e]{6,}")

lines = []


def scan(label: str, data: bytes):
    seen = set()
    n = 0
    lines.append(f"===== {label} ({len(data)} B) =====")
    for m in PAT.finditer(data):
        s = m.group()
        low = s.lower()
        if any(k in low for k in KEYS) and s not in seen:
            seen.add(s)
            lines.append(f"0x{m.start():08X}  {s[:220].decode('ascii', 'replace')}")
            n += 1
            if n >= 400:
                lines.append("... (cat bot, qua nhieu)")
                break
    lines.append("")


apks = sorted(BASE.glob("*.apk"))
if not apks:
    lines.append("Khong thay file .apk trong thu muc")
else:
    with zipfile.ZipFile(apks[0]) as z:
        for name in z.namelist():
            if name.endswith("/libApplicationMain.so") or name.endswith(".dex"):
                scan(f"{apks[0].name}:{name}", z.read(name))

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Da ghi {OUT} ({len(lines)} dong)")
