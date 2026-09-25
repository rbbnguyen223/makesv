import capstone

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

def dis(addr, before=16, after=16):
    start = max(0, addr - before*4)
    code = data[start:start+(before+after)*4]
    print(f"=== Frame around 0x{addr:08X} ===")
    for ins in md.disasm(code, start):
        prefix = "--> " if ins.address == addr else "    "
        print(f"{prefix}0x{ins.address:08X}: {ins.bytes.hex()}  {ins.mnemonic:8s} {ins.op_str}")

dis(0x007AF92C, 6, 6)
dis(0x007AC874, 6, 6)
dis(0x007AC8C8, 6, 6)
dis(0x008077A4, 6, 6)
dis(0x007AD624, 6, 6)
dis(0x007B3D18, 6, 6)
dis(0x00BFA000, 6, 6)
