with open("libApplicationMain_clean1patch.so", "rb") as f:
    data = bytearray(f.read())

offset = 0x7AF920

# Expected old bytes at 0x7AF920:
# LDR R3, [R4, #0x20]  -> 20 30 94 E5
# MOV R0, R3           -> 03 00 A0 E1
# LDR R3, [R3]         -> 00 30 93 E5
# MOV LR, PC           -> 0F E0 A0 E1
# LDR PC, [R3, #0xF0]  -> F0 F0 93 E5
expected_old = bytes([
    0x20, 0x30, 0x94, 0xE5,
    0x03, 0x00, 0xA0, 0xE1,
    0x00, 0x30, 0x93, 0xE5,
    0x0F, 0xE0, 0xA0, 0xE1,
    0xF0, 0xF0, 0x93, 0xE5,
])

if data[offset:offset+20] == expected_old:
    print("Match found! Patching...")
    # New bytes:
    # LDR R0, [R4, #0x20]  -> 20 00 94 E5
    # CMP R0, #0           -> 00 00 50 E3
    # LDRNE R3, [R0]       -> 00 30 90 15
    # MOVNE LR, PC         -> 0F E0 A0 11
    # LDRNE PC, [R3, #0xF0]-> F0 F0 93 15
    new_patch = bytes([
        0x20, 0x00, 0x94, 0xE5,
        0x00, 0x00, 0x50, 0xE3,
        0x00, 0x30, 0x90, 0x15,
        0x0F, 0xE0, 0xA0, 0x11,
        0xF0, 0xF0, 0x93, 0x15,
    ])
    data[offset:offset+20] = new_patch
    with open("libApplicationMain_patched3.so", "wb") as f:
        f.write(data)
    print("Successfully saved libApplicationMain_patched3.so")
else:
    print("Mismatch at offset! Found bytes:")
    print(data[offset:offset+20].hex())
