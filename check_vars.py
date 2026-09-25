import struct

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

for base, name in [
    (0x00eb45d0 - 0x10000, 'DAT_00eb45d0'),
    (0x00ec00f4 - 0x10000, 'DAT_00ec00f4'),
    (0x00ebb0a8 - 0x10000, 'DAT_00ebb0a8'),
    (0x00ebb0b0 - 0x10000, 'DAT_00ebb0b0')
]:
    val = struct.unpack('<I', data[base:base+4])[0]
    print(f'{name} @ 0x{base:08X} = 0x{val:08X}')
    for v in [val, val - 0x10000]:
        if 0 <= v < len(data) - 20:
            s = data[v:v+40].split(b'\0')[0]
            if len(s) > 1 and all(32 <= b < 127 for b in s):
                print(f'   str @ 0x{v:08X}: "{s.decode("latin1")}"')
