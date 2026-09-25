import struct
import capstone

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

# Scan backwards for push {..., lr}
func_start = None
for addr in range(0x7AF920, 0x7AE000, -4):
    word = struct.unpack('<I', data[addr:addr+4])[0]
    if (word & 0xFFFF0000) == 0xE92D0000 and (word & (1<<14)): # PUSH {..., LR}
        func_start = addr
        break

print(f"Function start: 0x{func_start:08X}")

md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)

# Disassemble from func_start to 0x7B0000
for a in range(func_start, func_start + 0x1000, 4):
    word = struct.unpack('<I', data[a:a+4])[0]
    # Check if this instruction loads PC-relative constant
    if (word & 0x0E5F0000) == 0x041F0000: # LDR Rd, [PC, #imm]
        imm = word & 0xFFF
        u = (word >> 23) & 1
        target = (a + 8) + (imm if u else -imm)
        if 0 <= target < len(data) - 4:
            val = struct.unpack('<I', data[target:target+4])[0]
            if 0 <= val < len(data):
                end = data.find(b'\0', val)
                if 0 <= end - val < 200:
                    s = data[val:end]
                    if len(s) > 1 and all(32 <= b < 127 for b in s):
                        print(f"0x{a:08X}: string @ 0x{val:08X} -> {s.decode('latin1')}")

print("\nDisassembly around 0x7AF8F0 - 0x7AF960:")
code = data[0x7AF8F0:0x7AF980]
for ins in md.disasm(code, 0x7AF8F0):
    print(f"0x{ins.address:08X}: {ins.bytes.hex()}  {ins.mnemonic:8s} {ins.op_str}")
