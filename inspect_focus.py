import struct
import capstone
import re

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

cs = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

for ins in cs.disasm(data[0x7b2948:0x7b3000], 0x7b2948):
    m = re.search(r'\[pc,\s*#?(0x[0-9a-fA-F]+|\d+)\]', ins.op_str)
    if m:
        offset = int(m.group(1), 0)
        pool_addr = ins.address + 8 + offset
        if pool_addr + 4 <= len(data):
            val = struct.unpack('<I', data[pool_addr:pool_addr+4])[0]
            if 0 < val < len(data):
                end = data.find(b'\0', val)
                if end != -1 and 1 < end - val < 50:
                    s = data[val:end]
                    if all(32 <= b < 127 for b in s):
                        print(f"0x{ins.address:x}: str='{s.decode()}'")
            rel = (ins.address + 8 + val + 4) & 0xffffffff
            if 0 < rel < len(data):
                end_r = data.find(b'\0', rel)
                if end_r != -1 and 1 < end_r - rel < 50:
                    sr = data[rel:end_r]
                    if all(32 <= b < 127 for b in sr):
                        print(f"0x{ins.address:x}: rel_str='{sr.decode()}'")
