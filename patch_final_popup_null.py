import shutil

src = 'libApplicationMain_final_run.so'
bak = 'libApplicationMain_final_run.so.bak5'
shutil.copyfile(src, bak)
print(f"Backed up {src} to {bak}")

with open(src, 'rb') as f:
    data = bytearray(f.read())

offset = 0xb9fce8
expected = bytes([
    0x01, 0x30, 0xa0, 0xe1, # mov r3, r1
    0x08, 0xd0, 0x4d, 0xe2, # sub sp, sp, #8
    0x64, 0xc0, 0x94, 0xe5, # ldr ip, [r4, #0x64]
    0x01, 0x20, 0xa0, 0xe1, # mov r2, r1
    0xa0, 0x30, 0x84, 0xe5, # str r3, [r4, #0xa0]
])

assert data[offset:offset+20] == expected, f"0x{offset:x} mismatch: {data[offset:offset+20].hex()}"

new_patch = bytes([
    0xa0, 0x10, 0x84, 0xe5, # str r1, [r4, #0xa0]
    0x08, 0xd0, 0x4d, 0xe2, # sub sp, sp, #8
    0x64, 0xc0, 0x94, 0xe5, # ldr ip, [r4, #0x64]
    0x00, 0x00, 0x5c, 0xe3, # cmp ip, #0
    0x07, 0x00, 0x00, 0x0a, # beq #0xb9fd1c
])

data[offset:offset+20] = new_patch
print(f"Patched 0x{offset:x}: null card check for FinalPopup")

with open(src, 'wb') as f:
    f.write(data)

print(f"Successfully updated {src}!")
