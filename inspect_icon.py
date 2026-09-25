import struct
import capstone
import re

with open('libApplicationMain_final_run.so', 'rb') as f:
    data = f.read()

def read_str(addr):
    if 0 <= addr < len(data):
        end = data.find(b'\0', addr)
        if end != -1 and 1 < (end - addr) < 100:
            s = data[addr:end]
            if all(32 <= b < 127 for b in s):
                return s.decode('ascii')
    return ''

cs = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

for ins in cs.disasm(data[0x415f40:0x416500], 0x415f40):
    m = re.search(r'\[pc,\s*#?(0x[0-9a-fA-F]+|\d+)\]', ins.op_str)
    if m:
        offset = int(m.group(1), 0)
        pool_addr = ins.address + 8 + offset
        if pool_addr + 4 <= len(data):
            val = struct.unpack('<I', data[pool_addr:pool_addr+4])[0]
            s = read_str(val)
            rel = (ins.address + 8 + val + 4) & 0xffffffff
            s_rel = read_str(rel)
            print(f"0x{ins.address:08x}: {ins.mnemonic:8s} {ins.op_str} -> pool 0x{pool_addr:x} = 0x{val:08x} (str: '{s}' or rel: '{s_rel}')")
