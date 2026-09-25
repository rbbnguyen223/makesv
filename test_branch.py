import capstone

def make_b(cond, pc, target):
    diff = target - (pc + 8)
    imm24 = (diff >> 2) & 0x00ffffff
    return (cond << 28) | (0x0a << 24) | imm24

cs = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

# 1. At 0x416068: beq #0x4167dc
b1 = make_b(0x0, 0x416068, 0x4167dc)
ins1 = list(cs.disasm(b1.to_bytes(4, 'little'), 0x416068))[0]
print(f"0x416068: {ins1.mnemonic} {ins1.op_str} (hex: {b1.to_bytes(4, 'little').hex()})")

# 2. At 0x416c14: b #0x416c54
b2 = make_b(0xe, 0x416c14, 0x416c54)
ins2 = list(cs.disasm(b2.to_bytes(4, 'little'), 0x416c14))[0]
print(f"0x416c14: {ins2.mnemonic} {ins2.op_str} (hex: {b2.to_bytes(4, 'little').hex()})")

# 3. Trampoline at 0x416c54:
# 0x416c54: cmp r5, #0  -> 0xe3550000
# 0x416c58: beq #0x4167dc
b3 = make_b(0x0, 0x416c58, 0x4167dc)
# 0x416c5c: b #0x4160a4
b4 = make_b(0xe, 0x416c5c, 0x4160a4)

trampoline = b'\x00\x00\x55\xe3' + b3.to_bytes(4, 'little') + b4.to_bytes(4, 'little')
for ins in cs.disasm(trampoline, 0x416c54):
    print(f"0x{ins.address:08x}: {ins.mnemonic:8s} {ins.op_str}")

# Also check 0x416c80 method:
# 0x416da0: beq #0x417628 (epilogue of 0x416c80)
b_c80_1 = make_b(0x0, 0x416da0, 0x417628)
ins_c80_1 = list(cs.disasm(b_c80_1.to_bytes(4, 'little'), 0x416da0))[0]
print(f"0x416da0: {ins_c80_1.mnemonic} {ins_c80_1.op_str} (hex: {b_c80_1.to_bytes(4, 'little').hex()})")

# 0x415d08 method:
# 0x415dd0: beq #0x415ea4 (epilogue of 0x415d08)
b_d08_1 = make_b(0x0, 0x415dd0, 0x415ea4)
ins_d08_1 = list(cs.disasm(b_d08_1.to_bytes(4, 'little'), 0x415dd0))[0]
print(f"0x415dd0: {ins_d08_1.mnemonic} {ins_d08_1.op_str} (hex: {b_d08_1.to_bytes(4, 'little').hex()})")
