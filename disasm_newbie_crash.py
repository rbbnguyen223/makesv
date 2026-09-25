import capstone

with open('libApplicationMain.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

for i in md.disasm(d[0x7AF918:0x7AFA90], 0x7AF918):
    print(f"0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
