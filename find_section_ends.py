import capstone

with open('libApplicationMain.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

branch_addrs = [
    0x4D9A2C,
    0x4D9C4C,
    0x4D9DB8,
    0x4D9ED0,
    0x4DA18C,
    0x4DA2D0,
    0x4DA540,
    0x4DA5D0,
    0x4DA704,
    0x4DA818,
]

for b_addr in branch_addrs:
    # scan forward up to 500 bytes for next asset load
    # An asset load begins with ldr r3, [pc, #imm]; ... bl 0xab3280 or bl 0xab3318 or bl 0xab0154
    # or the end of the function (pop {..., pc} at 0x4DAAE0+)
    insts = list(md.disasm(d[b_addr:b_addr+400], b_addr))
    next_asset = None
    for i in insts[1:]:
        if i.mnemonic == 'bl' and i.op_str in ('#0xab3280', '#0xab3318', '#0xab0154'):
            # The start of this call sequence is a few instructions before
            # Look backwards from i for ldr r3, [pc, #imm]
            pass
        if i.mnemonic == 'pop' and 'pc' in i.op_str:
            next_asset = i.address
            break
        # Look for the start of the next asset block: usually ldr r3, [pc, #imm] followed by add rX, sp, ...
        # Or look for where r6 is loaded with the next asset: ldr r6, [sp, #imm]
    print(f"=== Branch 0x{b_addr:X} ===")
    for i in insts[:25]:
        print(f"  0x{i.address:X}:\t{i.mnemonic}\t{i.op_str}")
