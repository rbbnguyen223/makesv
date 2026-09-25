import struct

with open('libApplicationMain.so', 'rb') as f:
    data = bytearray(f.read())

# Patch 0x7b2ae8 (20 bytes):
# ldr r3, [sp, #0x204]
# cmp r3, #0
# beq #0x7b2afc
# nop
# nop
patch = struct.pack('<IIIII', 0xe59d3204, 0xe3530000, 0x0a000001, 0xe1a00000, 0xe1a00000)
data[0x7b2ae8:0x7b2ae8+20] = patch

with open('libApplicationMain.so', 'wb') as f:
    f.write(data)

print("Patched 0x7b2ae8 (CreateCharacter card check) successfully!")
