console.log("[*] Listing modules...");

setTimeout(function () {
    var modules = Process.enumerateModules();
    for (var i = 0; i < modules.length; i++) {
        if (modules[i].name.toLowerCase().indexOf("libapp") !== -1) {
            console.log("Module: " + modules[i].name + " at " + modules[i].base);
        }
    }
}, 500);
