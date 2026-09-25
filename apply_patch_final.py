import struct

with open('libApplicationMain_nullfix.so', 'rb') as f:
    data = bytearray(f.read())

offset = 0x7AF920
# Expected original bytes in nullfix:
# 20 30 94 E5 (ldr r3, [r4, #0x20])
# 03 00 A0 E1 (mov r0, r3)
# 00 30 93 E5 (ldr r3, [r3])
# 0F E0 A0 E1 (mov lr, pc)
# F0 F0 93 E5 (ldr pc, [r3, #0xf0])
expected = bytes([
    0x20, 0x30, 0x94, 0xE5,
    0x03, 0x00, 0xA0, 0xE1,
    0x00, 0x30, 0x93, 0xE5,
    0x0F, 0xE0, 0xA0, 0xE1,
    0xF0, 0xF0, 0x93, 0xE5,
])

if data[offset:offset+20] == expected:
    print("Match at 0x7AF920! Patching safe skip to 0x7AFB50...")
    new_patch = bytes([
        0x20, 0x00, 0x94, 0xe5, # ldr r0, [r4, #0x20]
        0x00, 0x00, 0x50, 0xe3, # cmp r0, #0
        0x88, 0x00, 0x00, 0x0a, # beq #0x7afb50
        0x87, 0x00, 0x00, 0xea, # b #0x7afb50
        0x86, 0x00, 0x00, 0xea, # b #0x7afb50
    ])
    data[offset:offset+20] = new_patch
    out_name = 'libApplicationMain_final_run.so'
    with open(out_name, 'wb') as f:
        f.write(data)
    print(f"Saved {out_name} successfully!")
else:
    print("Mismatch at 0x7AF920:", data[offset:offset+20].hex())
