import subprocess, sys, time
from pathlib import Path

BASE = Path(__file__).resolve().parent

def adb(*args):
    result = subprocess.run(["adb.exe"] + list(args), capture_output=True, text=True, cwd=BASE)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def adb_shell(cmd):
    return adb("shell", cmd)

print("[1/3] Pushing to /data/local/tmp...")
adb("root")
time.sleep(1)
out, err, rc = adb("push", "libApplicationMain_popup.so", "/data/local/tmp/libApplicationMain_popup.so")
if rc != 0:
    sys.exit(f"FAILED push: {err}")
print("Push OK")

print("[2/3] Finding path...")
adb_shell("am force-stop lmah.vn")
time.sleep(1)
out, _, _ = adb_shell("find /data/app -name libApplicationMain.so 2>/dev/null")
paths = [p.strip() for p in out.splitlines() if "lmah.vn" in p and p.strip().endswith("libApplicationMain.so")]

if not paths:
    out2, _, _ = adb_shell("pm path lmah.vn")
    if "package:" in out2:
        apk_path = out2.replace("package:", "").strip()
        paths = [apk_path.replace("base.apk", "lib/arm/libApplicationMain.so")]

if not paths:
    sys.exit("Not found")

so_path = paths[0]
print(f"Target: {so_path}")

print("[3/3] Copying...")
out, err, rc = adb_shell(f"cp /data/local/tmp/libApplicationMain_popup.so '{so_path}'")
if rc != 0:
    adb_shell(f"cat /data/local/tmp/libApplicationMain_popup.so > '{so_path}'")
adb_shell(f"chmod 755 '{so_path}'")

print("DONE!")
