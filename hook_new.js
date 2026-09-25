var hooked = false;

function dumpHex(buf) {
    var arr = new Uint8Array(buf);
    var hex = "";
    for(var i=0; i<arr.length; i++) {
        var b = arr[i].toString(16);
        if(b.length == 1) b = "0" + b;
        hex += b + " ";
    }
    return hex;
}

function hookGame() {
    var base = MANUAL_BASE_ADDRESS;
    send("libApplicationMain.so Base from Python: " + base);
    
    // Trace the pointers used in handleRegister
    setInterval(function() {
        try {
            var eb45cc = base.add(0x00eb45cc).readPointer();
            var eb45d0 = base.add(0x00eb45d0).readPointer();
            var ec00f4 = base.add(0x00ec00f4).readPointer();
            var ec00f8 = base.add(0x00ec00f8).readPointer();
            
            send("eb45cc=" + eb45cc + (eb45cc.isNull() ? "" : " -> " + eb45cc.readUtf8String()));
            send("eb45d0=" + eb45d0 + (eb45d0.isNull() ? "" : " -> " + eb45d0.readUtf8String()));
            send("ec00f4=" + ec00f4 + (ec00f4.isNull() ? "" : " -> " + ec00f4.readUtf8String()));
            send("ec00f8=" + ec00f8 + (ec00f8.isNull() ? "" : " -> " + ec00f8.readUtf8String()));
        } catch(e) {
            send("Read error: " + e.message);
        }
    }, 2000);
}

hookGame();

