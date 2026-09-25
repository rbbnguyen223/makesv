import struct

with open('libApplicationMain_nullfix.so', 'rb') as f:
    data = bytearray(f.read())

offset = 0x006E6188
expected = bytes([0x2e, 0x00, 0x00, 0x0a]) # beq 0x6e6248

if data[offset:offset+4] == expected:
    print("Match at 0x6E6188! Patching to branch to epilogue...")
    data[offset:offset+4] = bytes([0x4a, 0x00, 0x00, 0x0a]) # beq 0x6e62b8
    
    out_name = 'libApplicationMain_popup.so'
    with open(out_name, 'wb') as f:
        f.write(data)
    print(f"Saved {out_name} successfully!")
else:
    print("Mismatch at 0x006E6188:", data[offset:offset+4].hex())
