console.log("[*] Script hook dang chay tren LDPlayer...");

function getModuleBase(modName) {
    var p = Process.findModuleByName(modName);
    if (p) return p.base;

    // Fallback doc qua /proc/self/maps cho moi truong Houdini x86
    var maps = new File("/proc/self/maps", "r");
    var line;
    while ((line = maps.readLine()) !== null) {
        if (line.indexOf(modName) !== -1) {
            var addr = line.split("-")[0];
            maps.close();
            return ptr("0x" + addr);
        }
    }
    maps.close();
    return null;
}

setTimeout(function () {
    var base = getModuleBase("libApplicationMain.so");
    if (!base) {
        send("[-] Khong tim thay libApplicationMain.so trong maps!");
        return;
    }
    send("[+] libApplicationMain.so Base = " + base);

    // Offset FBClientSocket_extractMessage (Ghidra: 0x008A9230 - 0x10000 = 0x00899230)
    var extractMsgAddr = base.add(0x00899230);
    send("[+] Target FBClientSocket_extractMessage Address = " + extractMsgAddr);

    Interceptor.attach(extractMsgAddr, {
        onEnter: function (args) {
            send("[>>> S2C PACKET DETECTED <<<]");
            send("    Socket Object: " + args[0]);
        },
        onLeave: function (retval) {
            send("[<<< S2C EXTRACT MESSAGE FINISHED <<<]");
        }
    });

    // Hook StringMap::exists de bat xem client tim key nao
    // Offset StringMap::exists thuong duoc goi trong ham onMessage
    // Hook chuoi string UTF-8 de biet ten key
}, 1000);