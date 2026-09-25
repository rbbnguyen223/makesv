import capstone

with open('libApplicationMain.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

targets = [
    0x4D9A28,
    0x4D9C48,
    0x4D9DB4,
    0x4D9ECC,
    0x4DA188,
    0x4DA2CC,
    0x4DA53C,
    0x4DA5CC,
    0x4DA700,
    0x4DA814,
]

for t in targets:
    print(f"=== Target at 0x{t:X} ===")
    for i in md.disasm(d[t-4:t+16], t-4):
        print(f"0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
