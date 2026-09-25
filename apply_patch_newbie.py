import struct

with open('libApplicationMain.so', 'rb') as f:
    data = bytearray(f.read())

# Patch 1: 0x7af920 (44 bytes)
patch1 = struct.pack('<I', 0xe3a00000) # mov r0, #0
patch1 += struct.pack('<I', 0xea000008) # b #0x7af94c
patch1 += struct.pack('<I', 0xe1a00000) * 9 # 9 NOPs
assert len(patch1) == 44

# Patch 2: 0x7afa3c (44 bytes)
patch2 = struct.pack('<I', 0xe3a00000) # mov r0, #0
patch2 += struct.pack('<I', 0xea000008) # b #0x7afa68
patch2 += struct.pack('<I', 0xe1a00000) * 9 # 9 NOPs
assert len(patch2) == 44

data[0x7af920:0x7af920+44] = patch1
data[0x7afa3c:0x7afa3c+44] = patch2

with open('libApplicationMain.so', 'wb') as f:
    f.write(data)

print("Patched libApplicationMain.so successfully!")
