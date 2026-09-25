import struct, capstone

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

# Target: 0xED0960 or 0xED0964
targets = {0xED0960, 0xED0964}

# Find all ldr rX, [pc, #imm] followed by add rX, pc, rX
for i in range(0x150000, 0xCB0000, 4):
    w = struct.unpack('<I', d[i:i+4])[0]
    # Check if ldr reg, [pc, #imm] -> 0x059Fxxxx or 0x051Fxxxx
    # Even simpler: check all 4-byte words as offset from i+8
    t = (i + 8 + struct.unpack('<i', d[i:i+4])[0]) & 0xFFFFFFFF
    if t in targets:
        print(f"Literal at 0x{i:X} computes target 0x{t:X} when PC=0x{i:X}")

# Also check if any literal loaded at addr A and added at addr B:
# B is usually within [A+4, A+32]
for b in range(0x150000, 0xCB0000, 4):
    inst = d[b:b+4]
    # add reg, pc, reg: 0xe08f_00_
    if (struct.unpack('<I', inst)[0] & 0xFFF000F0) == 0xE0800000 and (inst[2] & 0x0F) == 0x0F: # add rd, pc, rm
        # Look backward up to 16 instructions for ldr rm, [pc, #imm]
        pc_add = b + 8
        for a in range(b - 4, max(0x150000, b - 64), -4):
            inst_a = struct.unpack('<I', d[a:a+4])[0]
            if (inst_a & 0xFF7F0000) == 0x051F0000: # ldr rd, [pc, #imm]
                u = (inst_a >> 23) & 1
                imm12 = inst_a & 0xFFF
                lit_addr = (a + 8 + imm12) if u else (a + 8 - imm12)
                if 0 <= lit_addr <= len(d) - 4:
                    offset = struct.unpack('<i', d[lit_addr:lit_addr+4])[0]
                    target = (pc_add + offset) & 0xFFFFFFFF
                    if target in targets:
                        print(f"Found code at 0x{b:X} (ldr at 0x{a:X}, lit at 0x{lit_addr:X}) accessing target 0x{target:X}!")
