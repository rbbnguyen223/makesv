var hooked = false;

function hookGame() {
    if (hooked) return;
    var base = Module.findBaseAddress("libApplicationMain.so");
    if (base === null) {
        return;
    }
    hooked = true;
    send("libApplicationMain.so Base: " + base);
    
    // Crash is at 0x7AF920, caller is at 0x7AC874
    var targetAddress = base.add(0x7AC86C); // ldr r3, [r0]
    send("Hooking caller at " + targetAddress);
    
    Interceptor.attach(targetAddress, {
        onEnter: function(args) {
            send("Hit caller 0x7AC86C!");
            var r0 = this.context.r0; // The object pointer
            send("Object r0 = " + r0);
            if (!r0.isNull()) {
                try {
                    var vtable = r0.readPointer();
                    send("vtable [r0] = " + vtable);
                    // dump memory
                    var dump = r0.readByteArray(64);
                    send("r0 memory dump: ");
                    send(dump);
                } catch(e) {
                    send("Error reading memory: " + e);
                }
            }
        }
    });

    var crashAddress = base.add(0x7AF920); // ldr r3, [r4, #0x20]
    send("Hooking crash at " + crashAddress);
    Interceptor.attach(crashAddress, {
        onEnter: function(args) {
            send("Hit crash 0x7AF920!");
            var r4 = this.context.r4;
            send("r4 = " + r4);
            if (!r4.isNull()) {
                try {
                    var ptr20 = r4.add(0x20);
                    var val20 = ptr20.readPointer();
                    send("[r4+0x20] = " + val20);
                    if (val20.isNull()) {
                        send("!!! Null pointer detected. Bypassing by faking r3 inside the interceptor !!!");
                        // We can't easily skip instructions safely, but we can set [r4+0x20] to a dummy object!
                        // Let's allocate a dummy object
                        var dummy = Memory.alloc(256);
                        // set dummy's vtable to itself + 4, and at itself+4 set to some safe function?
                        // Or just let it crash after dumping everything. We just need to know what it is!
                    }
                } catch(e) {
                    send("Error: " + e);
                }
            }
        }
    });
}

Interceptor.attach(Module.findExportByName("libc.so", "dlopen"), {
    onEnter: function(args) {
        this.libName = Memory.readCString(args[0]);
    },
    onLeave: function(retval) {
        if (this.libName !== null && this.libName.indexOf("libApplicationMain.so") !== -1) {
            hookGame();
        }
    }
});

// Try now in case it's already loaded
hookGame();
