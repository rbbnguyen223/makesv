import capstone

with open('libApplicationMain.so', 'rb') as f:
    d = f.read()

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
md.skipdata = True

targets = [
    (0x4D9A24, 0x4D9A2C, 0x4D9A68),
    (0x4D9C44, 0x4D9C4C, 0x4D9C88),
    (0x4D9DB0, 0x4D9DB8, 0x4D9DF4),
    (0x4D9EC8, 0x4D9ED0, 0x4D9F0C),
    (0x4DA184, 0x4DA18C, 0x4DA1C8),
    (0x4DA2C8, 0x4DA2D0, 0x4DA30C),
    (0x4DA538, 0x4DA540, 0x4DA57C),
    (0x4DA5C8, 0x4DA5D0, 0x4DA60C),
    (0x4DA6FC, 0x4DA704, 0x4DA740),
    (0x4DA810, 0x4DA818, 0x4DA854),
]

for cmp_addr, beq_addr, check_addr in targets:
    # Disassemble around check_addr
    insts = list(md.disasm(d[check_addr:check_addr+40], check_addr))
    # Look for cmp r3, r2 ... bge / blt
    # Then see where it falls through or exits
    print(f"=== Loop at 0x{cmp_addr:X}, check at 0x{check_addr:X} ===")
    for idx, inst in enumerate(insts):
        print(f"  0x{inst.address:X}: {inst.mnemonic} {inst.op_str}")
        if inst.mnemonic in ('bge', 'bgt', 'blt', 'ble'):
            # The next instruction or branch target is the exit
            pass
