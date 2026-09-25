import capstone

with open('libApplicationMain_clean1patch.so', 'rb') as f:
    data = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

for i in md.disasm(data[0x7AF3D0:0x7AF450], 0x7AF3D0):
    print(f"0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
