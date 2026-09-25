import capstone
with open('libApplicationMain.so', 'rb') as f:
    f.seek(0x007ba310)
    code = f.read(0x40)
    md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
    for i in md.disasm(code, 0x007ba310):
        print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
