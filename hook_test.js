console.log("[*] Frida script test loading...");

setTimeout(function () {
    try {
        var libc_recv = Module.getExportByName("libc.so", "recv");
        console.log("libc recv: " + libc_recv);
        Interceptor.attach(libc_recv, {
            onEnter: function(args) {
                this.fd = args[0].toInt32();
                this.len = args[2].toInt32();
            },
            onLeave: function(retval) {
                var ret = retval.toInt32();
                if (ret > 0) {
                    console.log("[recv] fd: " + this.fd + " len: " + ret);
                }
            }
        });

        var libc_send = Module.getExportByName("libc.so", "send");
        Interceptor.attach(libc_send, {
            onEnter: function(args) {
                var len = args[2].toInt32();
                console.log("[send] fd: " + args[0].toInt32() + " len: " + len);
            }
        });
    } catch(e) {
        console.log("Error in libc hook: " + e.stack);
    }
}, 500);
