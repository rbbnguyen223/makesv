import capstone

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

funcs = [0x897c90, 0x899d74, 0x89a278, 0x89a7a4, 0x89aa74]
for fn in funcs:
    print(f"=== Disassembly of 0x{fn:x} ===")
    for insn in list(md.disasm(data[fn:fn+36], fn))[:5]:
        print(f"  0x{insn.address:x}: {insn.mnemonic:8} {insn.op_str}")
