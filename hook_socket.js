console.log("[*] hook_socket.js injected!");

function htons(port) {
    return ((port & 0xff) << 8) | ((port >> 8) & 0xff);
}

function ntohs(port) {
    return htons(port);
}

// Hook connect in libc.so
var connectPtr = Module.findExportByName("libc.so", "connect");
if (connectPtr) {
    console.log("[*] Found connect() at " + connectPtr);
    Interceptor.attach(connectPtr, {
        onEnter: function(args) {
            var sockfd = args[0].toInt32();
            var sockaddr = ptr(args[1]);
            var addrlen = args[2].toInt32();
            
            try {
                var family = sockaddr.readU16();
                if (family === 2) { // AF_INET
                    var rawPort = sockaddr.add(2).readU16();
                    var port = ntohs(rawPort);
                    var ip0 = sockaddr.add(4).readU8();
                    var ip1 = sockaddr.add(5).readU8();
                    var ip2 = sockaddr.add(6).readU8();
                    var ip3 = sockaddr.add(7).readU8();
                    var ipStr = ip0 + "." + ip1 + "." + ip2 + "." + ip3;
                    
                    console.log("[*] connect(sockfd=" + sockfd + ", ip=" + ipStr + ", port=" + port + ")");
                    
                    var bt = Thread.backtrace(this.context, Backtracer.ACCURATE)
                        .map(DebugSymbol.fromAddress).join("\n  ");
                    console.log("  Backtrace:\n  " + bt);
                    
                    if (ipStr === "192.168.1.13" && port === 0) {
                        console.log("[!] OVERRIDING PORT 0 -> 8888 FOR " + ipStr + "!");
                        sockaddr.add(2).writeU16(htons(8888));
                    }
                }
            } catch(e) {
                console.log("[-] Error in connect hook: " + e);
            }
        },
        onLeave: function(retval) {
            console.log("[*] connect() returned: " + retval.toInt32());
        }
    });
} else {
    console.log("[-] connect() not found in libc.so");
}
