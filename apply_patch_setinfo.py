import struct

with open('libApplicationMain.so', 'rb') as f:
    data = bytearray(f.read())

# Patch 0x7b35c4:
# mov r3, #0
# str r3, [r0]
# bx lr
patch = struct.pack('<III', 0xe3a03000, 0xe5803000, 0xe12fff1e)
data[0x7b35c4:0x7b35c4+12] = patch

with open('libApplicationMain.so', 'wb') as f:
    f.write(data)

print("Patched 0x7b35c4 (SetInfo) successfully!")
