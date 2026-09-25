import shutil
import sys

src = 'libApplicationMain_final_run.so'
bak = 'libApplicationMain_final_run.so.bak_force_hid'
shutil.copyfile(src, bak)
print(f"Backed up {src} to {bak}")

with open(src, 'rb') as f:
    data = bytearray(f.read())

offset = 0x7b2ad4
expected = bytes([0x2c, 0x20, 0x94, 0xe5]) # ldr r2, [r4, #0x2c]

if data[offset:offset+4] != expected:
    if data[offset:offset+4] == bytes([0x02, 0x20, 0xa0, 0xe3]):
        print("Already patched!")
        sys.exit(0)
    else:
        print(f"Mismatch! Found {data[offset:offset+4].hex()}")
        sys.exit(1)

# Patch to mov r2, #2 (Cận Chiến)
new_patch = bytes([0x02, 0x20, 0xa0, 0xe3])
data[offset:offset+4] = new_patch
print(f"Patched 0x{offset:x}: forced hid=2 for CardPrototypeInfo")

with open(src, 'wb') as f:
    f.write(data)

print(f"Successfully updated {src}!")
