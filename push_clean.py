import subprocess

def adb_shell(cmd):
    return subprocess.run(['adb', 'shell', cmd], capture_output=True, text=True).stdout.strip()

print('Pushing original clean libApplicationMain.so...')
subprocess.run(['adb', 'root'])
subprocess.run(['adb', 'push', 'libApplicationMain.so', '/data/local/tmp/libApplicationMain_clean.so'])
adb_shell('am force-stop lmah.vn')
out2 = adb_shell('pm path lmah.vn')
apk_path = out2.replace('package:', '').strip()
lib_path = apk_path.replace('base.apk', 'lib/arm/libApplicationMain.so')
print('lib_path:', lib_path)
subprocess.run(['adb', 'shell', f'cat /data/local/tmp/libApplicationMain_clean.so > "{lib_path}"'])
subprocess.run(['adb', 'shell', f'chmod 755 "{lib_path}"'])
print('Done pushing original .so')
