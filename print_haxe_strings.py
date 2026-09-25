with open('libApplicationMain_clean1patch.so', 'rb') as f:
    d = f.read()

import struct

for off in [0x00C9390C, 0x00C937EC, 0x00C936F0, 0x00C936E4, 0x00C93A44, 0x00C93684, 0x0015766C, 0x00157674]:
    if off < len(d):
        s = []
        for b in d[off:off+40]:
            if b == 0: break
            if 32 <= b < 127: s.append(chr(b))
            else: break
        print(f"0x{off:X}: '{''.join(s)}'")
