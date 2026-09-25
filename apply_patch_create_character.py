import shutil

src = 'libApplicationMain_final_run.so'
bak = 'libApplicationMain_final_run.so.bak4'
shutil.copyfile(src, bak)
print(f"Backed up {src} to {bak}")

with open(src, 'rb') as f:
    data = bytearray(f.read())

offset = 0x7b2aec
expected = bytes([
    0x03, 0x00, 0xa0, 0xe1, # mov r0, r3
    0x00, 0x30, 0x93, 0xe5, # ldr r3, [r3]
    0x0f, 0xe0, 0xa0, 0xe1, # mov lr, pc
    0x30, 0xf1, 0x93, 0xe5, # ldr pc, [r3, #0x130]
])

assert data[offset:offset+16] == expected, f"0x{offset:x} mismatch: {data[offset:offset+16].hex()}"

new_patch = bytes([
    0x00, 0x00, 0x53, 0xe3, # cmp   r3, #0
    0x00, 0x30, 0x93, 0x15, # ldrne r3, [r3]
    0x0f, 0xe0, 0xa0, 0x11, # movne lr, pc
    0x30, 0xf1, 0x93, 0x15, # ldrne pc, [r3, #0x130]
])

data[offset:offset+16] = new_patch
print(f"Patched 0x{offset:x}: conditional null check for hero CardPrototypeInfo")

with open(src, 'wb') as f:
    f.write(data)

print(f"Successfully updated {src}!")
