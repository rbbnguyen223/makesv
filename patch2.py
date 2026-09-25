import shutil
import subprocess

src = "libApplicationMain_clean1patch.so"
dst = "libApplicationMain_patched2.so"

shutil.copy(src, dst)

with open(dst, "r+b") as f:
    f.seek(0x7AC874)
    # ldr pc, [r3, #0xf4] -> nop
    f.write(bytes([0x00, 0x00, 0xa0, 0xe1]))

print("Patched 0x7AC874 with NOP!")

# Push to LDPlayer
subprocess.run(["python", "push_so.py", dst])
