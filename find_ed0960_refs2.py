import struct, capstone

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

# Target: 0xED0960 or 0xED0964
targets = {0xED0960, 0xED0964}

# Scan every ADD instruction where operand 1 is pc
for addr in range(0x150000, 0xCB0000, 4):
    w = struct.unpack('<I', d[addr:addr+4])[0]
    # Check if add Rd, pc, Rm (0x_08F_00_)
    if (w & 0x0FF00000) == 0x00800000 and ((w >> 16) & 0xF) == 0xF:
        rd = (w >> 12) & 0xF
        rm = w & 0xF
        # Check backward for LDR rm, [pc, #imm]
        for back in range(addr - 4, max(0x150000, addr - 80), -4):
            wb = struct.unpack('<I', d[back:back+4])[0]
            # ldr Rm, [pc, #offset]
            if (wb & 0x0F7F0000) == 0x051F0000 and ((wb >> 12) & 0xF) == rm:
                u = (wb >> 23) & 1
                imm = wb & 0xFFF
                lit_va = (back + 8 + imm) if u else (back + 8 - imm)
                if 0 <= lit_va <= len(d) - 4:
                    offset = struct.unpack('<i', d[lit_va:lit_va+4])[0]
                    target = ((addr + 8) + offset) & 0xFFFFFFFF
                    if target in targets:
                        print(f"Found reference at 0x{addr:X} (ldr at 0x{back:X}, lit at 0x{lit_va:X}) -> target 0x{target:X} (reg r{rd})")
                break
