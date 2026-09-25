import os
import lzma
import urllib.request
import subprocess
import frida

def download_and_extract(url, out_path):
    print(f"Downloading {url} ...")
    try:
        response = urllib.request.urlopen(url)
        compressed_data = response.read()
        print("Extracting...")
        decompressed_data = lzma.decompress(compressed_data)
        with open(out_path, 'wb') as f:
            f.write(decompressed_data)
        print(f"Saved to {out_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    version = frida.__version__
    print(f"Frida version: {version}")
    
    base_url = f"https://github.com/frida/frida/releases/download/{version}/"
    files = {
        "x86": f"frida-server-{version}-android-x86.xz",
    }
    
    for arch, filename in files.items():
        url = base_url + filename
        out_name = "frida-server"
        if not os.path.exists(out_name):
            download_and_extract(url, out_name)
    
    print("Pushing to emulator...")
    subprocess.run(["adb", "push", "frida-server", "/data/local/tmp/frida-server"])
    subprocess.run(["adb", "shell", "chmod", "755", "/data/local/tmp/frida-server"])
    
    print("Starting frida-server in background...")
    subprocess.run(["adb", "shell", "su", "-c", "'killall -9 frida-server'"], stderr=subprocess.DEVNULL)
    subprocess.Popen(["adb", "shell", "su", "-c", "'/data/local/tmp/frida-server -D'"])
    print("frida-server is ready!")
