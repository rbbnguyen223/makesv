console.log("[*] Searching for FBClientSocket functions...");

setTimeout(function () {
    try {
        var mod = Process.getModuleByName("libApplicationMain.so");
        var exports = mod.enumerateExports();
        var found = 0;
        for (var i = 0; i < exports.length; i++) {
            var exp = exports[i];
            if (exp.name.indexOf("FBClient") !== -1 || exp.name.indexOf("ParseMessage") !== -1) {
                console.log("Found: " + exp.name + " at " + exp.address);
                found++;
            }
        }
        console.log("Total found: " + found);
    } catch(e) {
        console.log("Error: " + e.stack);
    }
}, 500);
