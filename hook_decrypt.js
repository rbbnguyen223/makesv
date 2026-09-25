console.log("[*] Frida script hook_decrypt_v2.js loading...");

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

function dumpHaxeStringOrBytes(ptr_obj) {
    if (ptr_obj.isNull()) return "null";
    try {
        var length = ptr_obj.add(4).readInt();
        if (length > 0 && length < 10000) {
            var strPtr = ptr_obj.add(8);
            var buf = strPtr.readByteArray(length);
            var str = "";
            var bytes = new Uint8Array(buf);
            for(var i=0; i<bytes.length; i++) {
                if(bytes[i] >= 32 && bytes[i] <= 126) {
                    str += String.fromCharCode(bytes[i]);
                } else {
                    str += "\\x" + bytes[i].toString(16).padStart(2, '0');
                }
            }
            return "{len: " + length + ", data: '" + str + "'}";
        }
        return "{len: " + length + ", data: ???}";
    } catch (e) {
        return "Error reading Haxe object: " + e;
    }
}

setTimeout(function () {
    var base = getModuleBase("libApplicationMain.so");
    if (!base) {
        send("[-] Cannot find libApplicationMain.so!");
        return;
    }
    send("[+] libApplicationMain.so base = " + base);

    var decryptAddr = base.add(0x00B196C0).add(1);
    send("[+] Hooking Decrypt at " + decryptAddr);
    try {
        Interceptor.attach(decryptAddr, {
            onEnter: function (args) {
                this.out_ptr = args[0];
                this.in_ptr = args[1];
                this.key_ptr = args[2];
                var in_obj = this.in_ptr.readPointer();
                var key_obj = this.key_ptr.readPointer();
                send("[>>> Decrypt onEnter]");
                send("    IN:  " + dumpHaxeStringOrBytes(in_obj));
                send("    KEY: " + dumpHaxeStringOrBytes(key_obj));
            },
            onLeave: function (retval) {
                var out_obj = this.out_ptr.readPointer();
                send("[<<< Decrypt onLeave]");
                send("    OUT: " + dumpHaxeStringOrBytes(out_obj));
            }
        });
    } catch (e) {
        send("[-] Error attaching to 0x00B196C0: " + e);
    }

    var parseAddr = base.add(0x004D6A30).add(1);
    send("[+] Hooking ParseMessage at " + parseAddr);
    try {
        Interceptor.attach(parseAddr, {
            onEnter: function (args) {
                this.cmd_id = args[1].toInt32();
                var in_str_obj = args[2].readPointer();
                send("[>>> ParseMessage onEnter]");
                send("    CMD ID: " + this.cmd_id);
                send("    IN STR: " + dumpHaxeStringOrBytes(in_str_obj));
            }
        });
    } catch (e) {
        send("[-] Error attaching to 0x004D6A30: " + e);
    }
    
    // Also hook extractMessage
    var extractAddr = base.add(0x008A9320).add(1);
    send("[+] Hooking extractMessage at " + extractAddr);
    try {
        Interceptor.attach(extractAddr, {
            onEnter: function(args) {
                send("[>>> extractMessage REACHED!]");
            }
        });
    } catch(e) {
        send("[-] Error attaching to extractMessage: " + e);
    }



}, 500);
