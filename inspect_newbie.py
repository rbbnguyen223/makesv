import struct

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

# Find string 'GameStateNewbie'
idx = data.find(b'GameStateNewbie')
print('Found GameStateNewbie at', hex(idx))

# Search where this string pointer is stored
ptr = struct.pack('<I', idx)
pos = 0
found = []
while True:
    pos = data.find(ptr, pos)
    if pos == -1:
        break
    found.append(pos)
    pos += 4

print('References:', [hex(x) for x in found])
for ref in found:
    print(f'=== Around 0x{ref:x} ===')
    for off in range(ref - 0x20, ref + 0xa0, 4):
        val = struct.unpack('<I', data[off:off+4])[0]
        s = ''
        if 0 < val < len(data):
            e = data.find(b'\0', val)
            if e != -1 and 1 < e - val < 50:
                raw = data[val:e]
                if all(32 <= b < 127 for b in raw):
                    s = raw.decode()
        if s:
            print(f'  0x{off:x}: 0x{val:08x} "{s}"')
