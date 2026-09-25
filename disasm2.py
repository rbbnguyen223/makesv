# -*- coding: utf-8 -*-
# disasm2.py - Tim TEN HAM / TEN LOP (chuoi hxcpp tham chieu trong ham) cua cac diem crash/vá
# Chay: python disasm2.py       Ket qua: disasm2.txt        Can: pip install capstone
import re
import struct
import zipfile
from pathlib import Path

from capstone import Cs, CS_ARCH_ARM, CS_MODE_ARM

BASE = Path(__file__).resolve().parent
OUT = BASE / "disasm2.txt"

TARGETS = [
    ("cho crash #1 (r4+0x20 = null)", 0x7AF920),
    ("khung goi 0x7AC874", 0x7AC874),
    ("khung goi 0x7B0F80", 0x7B0F80),
    ("ham vá tra ve 1", 0x4D9984),
    ("khung crash moi #01", 0xC76038),
]
BACK = 0x5000     # quet nguoc toi da tim dau ham
FWD = 0x300

apk = sorted(BASE.glob("*.apk"))[0]
with zipfile.ZipFile(apk) as z:
    data = z.read("lib/armeabi/libApplicationMain.so")

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md.detail = False
LDR_PC = re.compile(r"^(r\d+|sb|sl|fp|ip), \[pc, #(-?)(0x[0-9a-fA-F]+|\d+)\]$")
ADD_PC = re.compile(r"^(r\d+|sb|sl|fp|ip), pc, (r\d+|sb|sl|fp|ip)$")
SUB_SP = re.compile(r"^sp, sp, #(0x[0-9a-fA-F]+|\d+)$")

lines = []


def out(s=""):
    lines.append(s)


def read_cstr(va, maxlen=80):
    if va < 0 or va + 8 >= len(data):
        return None
    raw = data[va: va + maxlen]
    end = raw.find(b"\x00")
    if end == -1:
        end = len(raw)
    s = raw[:end]
    if len(s) >= 2 and all(32 <= b < 127 for b in s):
        return s.decode("ascii")
    return None


def disasm(start, end):
    return list(md.disasm(data[start:end], start))


def find_func_start(addr):
    ins_list = disasm(addr - BACK, addr + 4)
    cand = None
    for i, ins in enumerate(ins_list):
        if ins.mnemonic == "push" and "lr" in ins.op_str:
            # ham that thuong co "sub sp, sp, #N" trong vai lenh sau
            window = ins_list[i + 1: i + 5]
            if any(SUB_SP.match(w.mnemonic + " " + w.op_str) or (w.mnemonic == "sub" and SUB_SP.match(w.op_str)) for w in window):
                cand = ins.address
    return cand


def string_refs(ins_list):
    """Tim mau hxcpp: ldr rN,[pc,#x] ; ... add rN, pc, rN  -> con tro chuoi = (addr_add+8+literal)+4"""
    refs = []
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
        for nxt in ins_list[i + 1: i + 8]:
            if nxt.mnemonic == "add":
                m2 = ADD_PC.match(nxt.op_str)
                if m2 and m2.group(2) == reg:
                    ptr = (nxt.address + 8 + lit) & 0xFFFFFFFF
                    s = read_cstr(ptr + 4)
                    if s:
                        refs.append((ins.address, ptr, s))
                    break
    return refs


for label, addr in TARGETS:
    out(f"===== {label}: 0x{addr:X} =====")
    fs = find_func_start(addr)
    if fs is None:
        out("  (khong tim thay dau ham trong 0x5000 byte truoc do)")
        out("")
        continue
    out(f"  dau ham (uoc luong): 0x{fs:X}   (cach diem quan tam {addr - fs:#x} byte)")
    ins_list = disasm(fs, addr + FWD)
    refs = string_refs(ins_list)
    seen = set()
    out("  chuoi tham chieu (theo thu tu trong ham):")
    n = 0
    for a, ptr, s in refs:
        if s in seen:
            continue
        seen.add(s)
        marker = "  <-- gan diem quan tam" if abs(a - addr) < 0x100 else ""
        out(f"    0x{a:07X}  \"{s}\"{marker}")
        n += 1
        if n >= 40:
            out("    ...")
            break
    out("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Da ghi {OUT} ({len(lines)} dong)")
