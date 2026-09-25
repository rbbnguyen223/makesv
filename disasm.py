# -*- coding: utf-8 -*-
# disasm.py - Dich nguoc (ARM 32-bit) cac vung quanh dia chi crash/vá trong libApplicationMain.so goc
# Chay:  python disasm.py        Ket qua: disasm.txt
# Can:   pip install capstone
import re
import struct
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "disasm.txt"

# (nhan, dia chi) - cac diem quan trong tu cac lan crash
TARGETS = [
    ("crash cu #1: cho vá 0x7AF920 (r4 = null, doc [r4+0x20])", 0x7AF920),
    ("khung goi 0x7AC874 (vá thanh bx lr)", 0x7AC874),
    ("khung goi 0x7B0F80 (vá thanh bx lr)", 0x7B0F80),
    ("ham 0x4D9984 (vá tra ve 1)", 0x4D9984),
    ("crash moi: khung #01 pc 0xC76038 (nhay vao dia chi rac)", 0xC76038),
]
BEFORE = 0x180
AFTER = 0x60

apks = sorted(BASE.glob("*.apk"))
if not apks:
    raise SystemExit("Khong thay file .apk trong thu muc")
with zipfile.ZipFile(apks[0]) as z:
    data = z.read("lib/armeabi/libApplicationMain.so")

lines = []

# --- program headers: kiem tra offset == vaddr ---
e_phoff = struct.unpack_from("<I", data, 0x1C)[0]
e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x2A)
lines.append("== ELF LOAD segments (offset -> vaddr, filesz, memsz, flags) ==")
loads = []
for i in range(e_phnum):
    p_type, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_flags, p_align = struct.unpack_from(
        "<IIIIIIII", data, e_phoff + i * e_phentsize)
    if p_type == 1:
        loads.append((p_offset, p_vaddr, p_filesz))
        lines.append(f"  off=0x{p_offset:X} vaddr=0x{p_vaddr:X} filesz=0x{p_filesz:X} memsz=0x{p_memsz:X} flags=0x{p_flags:X}")
lines.append("")


def vaddr_to_off(va):
    for off, v, fsz in loads:
        if v <= va < v + fsz:
            return va - v + off
    return None


try:
    from capstone import Cs, CS_ARCH_ARM, CS_MODE_ARM
except ImportError:
    raise SystemExit("Chua cai capstone. Chay: pip install capstone")

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
LDR_PC = re.compile(r"\[pc, #(-?)(0x[0-9a-fA-F]+|\d+)\]")

for label, addr in TARGETS:
    lines.append(f"===== {label} : 0x{addr:X} =====")
    start = addr - BEFORE
    off_start = vaddr_to_off(start)
    if off_start is None:
        lines.append("  (khong anh xa duoc dia chi)")
        continue
    chunk = data[off_start: off_start + BEFORE + AFTER]
    for ins in md.disasm(chunk, start):
        note = ""
        m = LDR_PC.search(ins.op_str)
        if m and ins.mnemonic.startswith("ldr"):
            imm = int(m.group(2), 0) * (-1 if m.group(1) else 1)
            lit_va = ins.address + 8 + imm
            lo = vaddr_to_off(lit_va)
            if lo is not None:
                val = struct.unpack_from("<I", data, lo)[0]
                note = f"    ; [0x{lit_va:X}] = 0x{val:08X}"
        mark = "  <== DIA CHI QUAN TAM" if ins.address == addr else ""
        prologue = "  ; --- co the la dau ham" if (ins.mnemonic == "push" and "lr" in ins.op_str) else ""
        lines.append(f"  0x{ins.address:07X}: {ins.mnemonic:<8}{ins.op_str}{note}{prologue}{mark}")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Da ghi {OUT} ({len(lines)} dong)")
