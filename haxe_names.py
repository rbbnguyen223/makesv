# -*- coding: utf-8 -*-
# haxe_names.py - Liet ke TEN HAM Haxe (hxcpp co stack-frame nen moi ham gan chuoi ten o dau ham)
# va tim ham chua cac dia chi crash/vá. Can: pip install capstone
# Chay: python haxe_names.py     Ket qua: func_names_focus.txt (doc cai nay), func_names_all.txt (du phong)
#
# CAP NHAT 21/09/2026: TARGETS doi sang dung 9 frame cua backtrace null-ptr moi nhat
# (ban clean1patch, crash tai 0x7AF92C) thay vi cac dia chi cua crash GOT-corrupt cu
# (0xC76038...) da khong con lien quan sau khi bo 3 vá thua.
import bisect
import re
import struct
import zipfile
from pathlib import Path

from capstone import Cs, CS_ARCH_ARM, CS_MODE_ARM

BASE = Path(__file__).resolve().parent
OUT_FOCUS = BASE / "func_names_focus.txt"
OUT_ALL = BASE / "func_names_all.txt"

TARGETS = [
    ("crash #00 - null ptr r4+0x20", 0x7AF92C),
    ("frame #01", 0x7AC874),
    ("frame #02", 0x7AC8C8),
    ("frame #03", 0x8077A4),
    ("frame #04", 0x7AD624),
    ("frame #05", 0x7B3D18),
    ("frame #06", 0xBFA000),
    ("frame #07", 0xBF80A8),
    ("frame #08", 0xBF54F8),
    ("frame #09 - entry/game loop", 0xC9F100),
    ("vá 1-patch giữ lại", 0x4D9984),
]
REGION = (0x150000, 0xCB0000)
NEIGHBORS = 10

apk = sorted(BASE.glob("*.apk"))[0]
with zipfile.ZipFile(apk) as z:
    data = z.read("lib/armeabi/libApplicationMain.so")

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
LDR_PC = re.compile(r"^(r\d+|sb|sl|fp|ip), \[pc, #(-?)(0x[0-9a-fA-F]+|\d+)\]$")
ADD_PC = re.compile(r"^(r\d+|sb|sl|fp|ip), pc, (r\d+|sb|sl|fp|ip)$")


def read_cstr(va, maxlen=90):
    if va < 0 or va + 4 >= len(data):
        return None
    raw = data[va: va + maxlen]
    end = raw.find(b"\x00")
    s = raw if end == -1 else raw[:end]
    if len(s) >= 2 and all(32 <= b < 127 for b in s):
        return s.decode("ascii")
    return None


def first_string(ins_list, window=30):
    for i, ins in enumerate(ins_list):
        if ins.mnemonic != "ldr":
            continue
        m = LDR_PC.match(ins.op_str)
        if not m:
            continue
        reg = m.group(1)
        imm = int(m.group(3), 0) * (-1 if m.group(2) else 1)
        lit_va = ins.address + 8 + imm
        if lit_va + 4 > len(data):
            continue
        lit = struct.unpack_from("<I", data, lit_va)[0]
        for nxt in ins_list[i + 1: i + window]:
            if nxt.mnemonic == "add":
                m2 = ADD_PC.match(nxt.op_str)
                if m2 and m2.group(2) == reg:
                    s = read_cstr(((nxt.address + 8 + lit) & 0xFFFFFFFF) + 4)
                    if s:
                        return s
                    break
    return None


# 1) tim tat ca dau ham: push {..., lr}
n_words = (REGION[1] - REGION[0]) // 4
words = struct.unpack_from(f"<{n_words}I", data, REGION[0])
starts = []
for i, w in enumerate(words):
    if (w & 0xFFFF0000) == 0xE92D0000 and (w & 0x4000):
        starts.append(REGION[0] + i * 4)
print(f"Tim thay {len(starts)} dau ham (push ..lr) trong vung {REGION[0]:#x}-{REGION[1]:#x}")

# 2) ten ham
names = {}
for s in starts:
    base = s - 8            # 2 lenh (ldr ten, mov r2,#len) thuong nam TRUOC push
    ins_list = list(md.disasm(data[base: base + 160], base))
    names[s] = first_string(ins_list)

with open(OUT_ALL, "w", encoding="utf-8") as f:
    for s in starts:
        f.write(f"0x{s:07X}  {names[s] or ''}\n")

# 3) tap trung vao cac diem quan tam
out = []
for label, addr in TARGETS:
    out.append(f"===== {label}: 0x{addr:X} =====")
    idx = bisect.bisect_right(starts, addr + 8) - 1     # +8: co ham vá o lenh ngay truoc push
    if idx < 0:
        out.append("  (khong tim thay)")
        out.append("")
        continue
    for j in range(max(0, idx - NEIGHBORS), min(len(starts), idx + NEIGHBORS + 1)):
        s = starts[j]
        mark = "  <== CHUA DIA CHI NAY" if j == idx else ""
        out.append(f"  0x{s:07X}  {names[s] or '(khong co ten)'}{mark}")
    out.append("")

OUT_FOCUS.write_text("\n".join(out), encoding="utf-8")
print(f"Da ghi {OUT_FOCUS} va {OUT_ALL}")
