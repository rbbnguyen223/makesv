import os
import shutil
import glob
from capstone import *

def main():
    fpaths = glob.glob('**/libstd.so', recursive=True)
    if not fpaths:
        print("[-] libstd.so not found!")
        return
        
    src_path = fpaths[0]
    print(f"[*] Found libstd.so at: {src_path}")
    
    # 1. Backup
    backup_path = "libstd_backup.so"
    if not os.path.exists(backup_path):
        shutil.copyfile(src_path, backup_path)
        print(f"[+] Created backup at: {backup_path}")
    else:
        print(f"[*] Backup already exists at: {backup_path}")
        
    with open(src_path, 'rb') as f:
        data = bytearray(f.read())
        
    patch_offset = 0xca48
    expected_orig = bytes.fromhex('7020ffe60600a0e12214a0e1022481e1b620cde1')
    actual_bytes = bytes(data[patch_offset:patch_offset+20])
    
    if actual_bytes != expected_orig:
        print(f"[-] Bytes mismatch at 0x{patch_offset:04x}!")
        print(f"    Expected: {expected_orig.hex()}")
        print(f"    Actual:   {actual_bytes.hex()}")
        if actual_bytes == bytes.fromhex('000050e3b8020203b02fbfe6b620cde10600a0e1'):
            print("[*] File already patched!")
        else:
            return
            
    # Patch bytes:
    # 0xca48: cmp r0, #0          -> 00 00 50 e3
    # 0xca4c: movweq r0, #0x22b8  -> b8 02 02 03
    # 0xca50: rev16 r2, r0        -> b0 2f bf e6
    # 0xca54: strh r2, [sp, #6]   -> b6 20 cd e1
    # 0xca58: mov r0, r6          -> 06 00 a0 e1
    patch_bytes = bytes.fromhex('000050e3b8020203b02fbfe6b620cde10600a0e1')
    data[patch_offset:patch_offset+20] = patch_bytes
    
    out_path = "libstd_patched.so"
    with open(out_path, 'wb') as f:
        f.write(data)
    print(f"[+] Wrote patched binary to {out_path}")
    
    # Verify with Capstone
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    print("[*] Verification:")
    for insn in md.disasm(patch_bytes, patch_offset):
        print(f"    0x{insn.address:04x}: {insn.mnemonic} {insn.op_str}")

if __name__ == "__main__":
    main()
