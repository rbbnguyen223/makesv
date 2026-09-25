import struct, capstone

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    data = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

pools = set()
for i in md.disasm(data[0x7AEF00:0x7AFB00], 0x7AEF00):
    if i.mnemonic in ('ldr', 'vldr') and 'pc' in i.op_str:
        parts = i.op_str.split(',')
        if len(parts) == 2 and 'pc' in parts[1]:
            offset_str = parts[1].replace('[', '').replace(']', '').replace('pc', '').replace('#', '').strip()
            if offset_str:
                offset = int(offset_str, 16) if '0x' in offset_str else int(offset_str)
                target_addr = (i.address + 8 + offset)
                if target_addr + 4 <= len(data):
                    val = struct.unpack('<I', data[target_addr:target_addr+4])[0]
                    pools.add((i.address, val))

for addr, p in sorted(pools):
    if 0 <= p < len(data):
        s = []
        for b in data[p:p+64]:
            if b == 0: break
            if 32 <= b < 127: s.append(chr(b))
            else: break
        if len(s) >= 3:
            print(f"0x{addr:X} -> 0x{p:X}: \"{''.join(s)}\"")
        else:
            # Maybe points to another pointer or HX_CSTRING
            p2 = struct.unpack('<I', data[p:p+4])[0] if p + 4 <= len(data) else 0
            if 0 <= p2 < len(data):
                s2 = []
                for b in data[p2:p2+64]:
                    if b == 0: break
                    if 32 <= b < 127: s2.append(chr(b))
                    else: break
                if len(s2) >= 3:
                    print(f"0x{addr:X} -> 0x{p:X} -> 0x{p2:X}: \"{''.join(s2)}\"")
