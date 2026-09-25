console.log("[*] Frida script hook_register.js loading...");

function getModuleBase(modName) {
    var p = Process.findModuleByName(modName);
    if (p) return p.base;
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
        send("[-] Cannot find libApplicationMain.so!");
        return;
    }
    send("[+] libApplicationMain.so base = " + base);

    // 1. Hook Function_1_6 (0x6EBA60): callback for 'register' response
    var func16Addr = base.add(0x006EBA60);
    send("[+] Hooking register callback Function_1_6 at " + func16Addr);
    try {
        Interceptor.attach(func16Addr, {
            onEnter: function (args) {
                send("[>>> Function_1_6 onEnter: args[0]=" + args[0] + ", args[1]=" + args[1] + ", args[2]=" + args[2]);
            }
        });
    } catch (e) {
        send("[-] Error attaching to 0x6EBA60: " + e);
    }

    // 2. Hook 0x6EBC20 (Success handler in 0x6EBA60)
    var successAddr = base.add(0x006EBC20);
    send("[+] Hooking Success branch at " + successAddr);
    try {
        Interceptor.attach(successAddr, {
            onEnter: function (args) {
                send("[>>> 0x6EBC20: SUCCESS CALLBACK REACHED! <<<]");
            }
        });
    } catch (e) {
        send("[-] Error attaching to 0x6EBC20: " + e);
    }

    // 3. Hook 0x6EBB50 (Branch point cmp r0, 1)
    var cmpAddr = base.add(0x006EBB4C);
    send("[+] Hooking cmp r0, 1 at " + cmpAddr);
    try {
        Interceptor.attach(cmpAddr, {
            onEnter: function (args) {
                send("[>>> 0x6EBB4C: r0 (data value) = " + this.context.r0 + " <<<]");
            }
        });
    } catch (e) {
        send("[-] Error attaching to 0x6EBB4C: " + e);
    }

}, 500);
