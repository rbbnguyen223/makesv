import struct
import capstone
import re

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

cs = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

for ins in cs.disasm(data[0xb8427c:0xb84900], 0xb8427c):
    m = re.search(r'\[pc,\s*#?(0x[0-9a-fA-F]+|\d+)\]', ins.op_str)
    if m:
        offset = int(m.group(1), 0)
        pool_addr = ins.address + 8 + offset
        if pool_addr + 4 <= len(data):
            val = struct.unpack('<I', data[pool_addr:pool_addr+4])[0]
            rel = (ins.address + 8 + val + 4) & 0xffffffff
            for v in (val, rel):
                if 0 < v < len(data):
                    end = data.find(b'\0', v)
                    if end != -1 and 1 < end - v < 50:
                        s = data[v:end]
                        if all(32 <= b < 127 for b in s):
                            print(f"0x{ins.address:x}: str='{s.decode()}'")
