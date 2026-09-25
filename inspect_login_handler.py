import capstone
import struct

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
base = 0x006E6158
code = data[base:base+0x280]

for ins in md.disasm(code, base):
    extra = ""
    if ins.mnemonic == 'ldr' and '[pc' in ins.op_str:
        parts = ins.op_str.split(',')
        imm_str = parts[1].replace('[', '').replace(']', '').replace('pc', '').replace('#', '').strip()
        imm = int(imm_str, 0) if imm_str else 0
        target = ins.address + 8 + imm
        if 0 <= target < len(data) - 4:
            val = struct.unpack('<I', data[target:target+4])[0]
            extra = f" // [0x{target:X}] = 0x{val:X}"
            # Check if val is a string or pointer
            if 0 <= val < len(data) - 20:
                s_cand = data[val:val+40]
                if b'\0' in s_cand:
                    s = s_cand.split(b'\0')[0]
                    if len(s) > 1 and all(32 <= b < 127 for b in s):
                        extra += f" '{s.decode('latin1')}'"
    print(f"0x{ins.address:08X}: {ins.mnemonic:8s} {ins.op_str:<25s} {extra}")
