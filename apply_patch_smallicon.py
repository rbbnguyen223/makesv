import struct

with open('libApplicationMain.so', 'rb') as f:
    data = bytearray(f.read())

# Patch 0x415f40: mov r0, #0; bx lr
patch = struct.pack('<II', 0xe3a00000, 0xe12fff1e)
data[0x415f40:0x415f48] = patch

with open('libApplicationMain.so', 'wb') as f:
    f.write(data)

print("Patched 0x415f40 (SmallIcon) successfully!")
