import capstone

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    data = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

for i in md.disasm(data[0x7AC000:0x7B5000], 0x7AC000):
    if '#0x20]' in i.op_str and ('r0' in i.op_str or 'r4' in i.op_str):
        print(f"0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
