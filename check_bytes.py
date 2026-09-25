import struct

with open('libApplicationMain.so', 'rb') as f:
    data = f.read()

# Check original bytes at 0x7AF920
print("=== Original bytes at 0x7AF920 ===")
for i in range(5):
    word = struct.unpack('<I', data[0x7AF920 + i*4:0x7AF924 + i*4])[0]
    print(f"0x7AF920+{i*4}: 0x{word:08X}")

# Expected from patch_skip_null.py
print("\n=== Expected bytes from patch_skip_null.py ===")
expected = [
    0x20, 0x30, 0x94, 0xE5,  # ldr r3, [r4, #0x20]
    0x03, 0x00, 0xA0, 0xE1,  # mov r0, r3
    0x00, 0x30, 0x93, 0xE5,  # ldr r3, [r3]
    0x0F, 0xE0, 0xA0, 0xE1,  # mov lr, pc
    0xF0, 0xF0, 0x93, 0xE5,  # ldr pc, [r3, #0xF0]
]
for i, b in enumerate(expected):
    print(f"  {i}: 0x{b:02X}", end="")
    actual_byte = (struct.unpack('<I', data[0x7AF920 + i*4:0x7AF924 + i*4])[0] >> (i*8)) & 0xFF
    match = "MATCH" if actual_byte == b else "MISMATCH"
    print(f" (actual byte {i}: 0x{actual_byte:02X} {match})")

# Check original bytes at 0x7AC874
print("\n=== Original bytes at 0x7AC874 ===")
for i in range(5):
    word = struct.unpack('<I', data[0x7AC874 + i*4:0x7AC878 + i*4])[0]
    print(f"0x7AC874+{i*4}: 0x{word:08X}")

# Expected from patch2.py
print("\n=== Expected bytes from patch2.py ===")
expected2 = [
    0x20, 0x00, 0x94, 0xE5,  # ldr r0, [r4, #0x20]
    0x00, 0x00, 0x50, 0xE3,  # cmp r0, #0
    0x00, 0x30, 0x90, 0x15,  # ldrne r3, [r0]
    0x0F, 0xE0, 0xA0, 0x11,  # movne lr, pc
    0xF0, 0xF0, 0x93, 0x15,  # ldrne pc, [r3, #0xF0]
]
for i, b in enumerate(expected2):
    print(f"  {i}: 0x{b:02X}", end="")
    actual_byte = (struct.unpack('<I', data[0x7AC874 + i*4:0x7AC878 + i*4])[0] >> (i*8)) & 0xFF
    match = "MATCH" if actual_byte == b else "MISMATCH"
    print(f" (actual byte {i}: 0x{actual_byte:02X} {match})")
