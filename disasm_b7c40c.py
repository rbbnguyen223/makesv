import capstone, struct

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

for i in md.disasm(d[0xB7C40C:0xB7C800], 0xB7C40C):
    print(f"0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
