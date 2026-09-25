# -*- coding: utf-8 -*-
# disasm3.py - Dich nguoc backtrace crash null ptr tai 0x7AF92C (ban 1-patch)
# Backtrace:
#   #00  0x007af92c  <- diem crash chinh
#   #01  0x007ac874
#   #02  0x007ac8c8
#   #03  0x008077a4
#   #04  0x007ad624
#   #05  0x007b3d18
#   #06  0x00bfa000
#   #07  0x00bf80a8
#   #08  0x00bf54f8
#   #09  0x00c9f100
# Chay: python disasm3.py  -> disasm3.txt
#
# FIX 21/09/2026: bat md.skipdata = True. Truoc day Capstone dung dich (generator
# ket thuc som) ngay khi gap byte khong giai ma duoc thanh ARM hop le (vd literal
# pool / jump table nam xen trong vung disasm co dinh truoc target). Day la ly do
# frame #01 (0x7AC874) chi ra vai dong lenh "vo nghia" (subseq/ldrdeq/rsbeq...)
# roi cat cut - do capstone dang doc nham 4 byte du lieu la 1 lenh ARM that.
# Bat skipdata giup no nhay qua byte du lieu (danh dau ".byte") va disassemble
# tiep phan code thuc su phia sau.

import struct, zipfile
from pathlib import Path

try:
    from capstone import Cs, CS_ARCH_ARM, CS_MODE_ARM
except ImportError:
    raise SystemExit("Chua cai capstone. Chay: pip install capstone")

BASE = Path(__file__).resolve().parent
APK  = next(BASE.glob("*.apk"), None)
if not APK:
    raise SystemExit("Khong tim thay .apk")

with zipfile.ZipFile(APK) as z:
    data = z.read("lib/armeabi/libApplicationMain.so")

# ELF LOAD segments
e_phoff = struct.unpack_from("<I", data, 0x1C)[0]
e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x2A)
loads = []
for i in range(e_phnum):
    p_type, p_offset, p_vaddr, _, p_filesz, *_ = struct.unpack_from("<IIIIIIII", data, e_phoff + i * e_phentsize)
    if p_type == 1:
        loads.append((p_offset, p_vaddr, p_filesz))

def vaddr_to_off(va):
    for off, v, fsz in loads:
        if v <= va < v + fsz:
            return va - v + off
    return None

def read_str(off, maxlen=80):
    end = data.index(b'\x00', off, off + maxlen) if b'\x00' in data[off:off+maxlen] else off+maxlen
    return data[off:end].decode('utf-8', errors='replace')

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md.skipdata = True
md.skipdata_setup = (".byte", None, None)

TARGETS = [
    ("crash #00 - diem null ptr deref: ldr r3,[r4,#0x20]",  0x7AF92C, 0x100, 0x80),
]

lines = ["== DISASM backtrace crash null ptr (ban 1-patch) - skipdata=on ==", ""]

for label, addr, before, after in TARGETS:
    lines.append(f"===== {label} : 0x{addr:X} =====")
    start = addr - before
    off_s = vaddr_to_off(start)
    if off_s is None:
        lines.append("  (khong anh xa duoc)")
        lines.append("")
        continue
    chunk = data[off_s: off_s + before + after]
    for ins in md.disasm(chunk, start):
        note = ""
        if ins.mnemonic == ".byte":
            lines.append(f"  0x{ins.address:07X}: .byte    {ins.bytes.hex()}  ; du lieu, khong phai lenh")
            continue
        # Ghi chú literal pool
        if ins.mnemonic.startswith("ldr") and "[pc," in ins.op_str:
            import re
            m = re.search(r'#(-?)(0x[0-9a-fA-F]+|\d+)', ins.op_str)
            if m:
                imm = int(m.group(2), 0) * (-1 if m.group(1) else 1)
                lit_va = ins.address + 8 + imm
                lo = vaddr_to_off(lit_va)
                if lo is not None and lo + 4 <= len(data):
                    val = struct.unpack_from("<I", data, lo)[0]
                    note = f"  ; [0x{lit_va:X}]=0x{val:08X}"
                    # Nếu val trông như offset chuỗi
                    str_va = ins.address + val + 4 if val < 0x01000000 else val
                    str_off = vaddr_to_off(str_va)
                    if str_off and str_off < len(data):
                        s = read_str(str_off, 40)
                        if s.isprintable() and len(s) > 3:
                            note += f' -> "{s}"'
        mark = "  <<<<< CRASH HERE" if ins.address == addr else ""
        prologue = "  ; [-- possible func start --]" if (ins.mnemonic == "push" and "lr" in ins.op_str) else ""
        lines.append(f"  0x{ins.address:07X}: {ins.mnemonic:<8} {ins.op_str}{note}{prologue}{mark}")
    lines.append("")

OUT = BASE / "disasm3.txt"
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Da ghi {OUT} ({len(lines)} dong)")
