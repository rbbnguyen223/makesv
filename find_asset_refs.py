import struct, capstone

with open('libApplicationMain.so', 'rb') as f:
    d = f.read()

targets = {0xECDA3C, 0xECDBD0}

# Scan every ADD instruction where operand 1 is pc
for addr in range(0x150000, 0xCB0000, 4):
    w = struct.unpack('<I', d[addr:addr+4])[0]
    if (w & 0x0FF00000) == 0x00800000 and ((w >> 16) & 0xF) == 0xF:
        rd = (w >> 12) & 0xF
        rm = w & 0xF
        for back in range(addr - 4, max(0x150000, addr - 80), -4):
            wb = struct.unpack('<I', d[back:back+4])[0]
            if (wb & 0x0F7F0000) == 0x051F0000 and ((wb >> 12) & 0xF) == rm:
                u = (wb >> 23) & 1
                imm = wb & 0xFFF
                lit_va = (back + 8 + imm) if u else (back + 8 - imm)
                if 0 <= lit_va <= len(d) - 4:
                    offset = struct.unpack('<i', d[lit_va:lit_va+4])[0]
                    target = ((addr + 8) + offset) & 0xFFFFFFFF
                    if target in targets:
                        print(f"Found ref at 0x{addr:X} (lit at 0x{lit_va:X}) -> 0x{target:X}")
                break
