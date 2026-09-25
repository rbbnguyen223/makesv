import struct

with open('libApplicationMain.so', 'rb') as f:
    data = bytearray(f.read())

branches = [
    (0x4D9A2C, 0x0A000016, "1: user_leveling -> 0x4D9A8C"),
    (0x4D9C4C, 0x0A00002B, "2: cards -> 0x4D9D00"),
    (0x4D9DB8, 0x0A000016, "3: iter3 -> 0x4D9E18"),
    (0x4D9ED0, 0x0A000016, "4: iter4 -> 0x4D9F30"),
    (0x4DA18C, 0x0A000025, "5: iter5 -> 0x4DA228"),
    (0x4DA258, 0x0A000010, "6: iter6_sub -> 0x4DA2A0"),
    (0x4DA2D0, 0x0A000016, "7: iter6 -> 0x4DA330"),
    (0x4DA540, 0x0A000016, "8: iter7 -> 0x4DA5A0"),
    (0x4DA5D0, 0x0A000016, "9: iter8 -> 0x4DA630"),
    (0x4DA704, 0x0A000016, "10: iter9 -> 0x4DA764"),
    (0x4DA818, 0x0A000016, "11: iter10 -> 0x4DA878"),
]

for addr, opcode, desc in branches:
    old_inst = struct.unpack('<I', data[addr:addr+4])[0]
    new_inst = opcode
    print(f"Patching 0x{addr:X} ({desc}): 0x{old_inst:08X} -> 0x{new_inst:08X}")
    data[addr:addr+4] = struct.pack('<I', new_inst)

out_file = 'libApplicationMain_nullfix.so'
with open(out_file, 'wb') as f:
    f.write(data)

print(f"Successfully generated {out_file} ({len(data)} bytes).")
