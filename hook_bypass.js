// hook_bypass.js
// Muc dich: hook FUNC_SHOW (ham hien popup "Dang tai du lieu..."), lay con tro `this`
// cua doi tuong UI luc no duoc goi, roi sau 5s tu goi thang FUNC_HIDE tren cung `this`
// de ep dong popup - khong can biet ly do goc client khong tu dong.
//
// BAT BUOC DIEN TRUOC KHI CHAY (lay tu Ghidra - search_strings + get_xrefs_to theo
// dung Buoc 1 da mo ta trong phantich.md):
//   - FUNC_SHOW_OFFSET: offset (tinh tu base .so) cua ham HIEN popup
//   - FUNC_HIDE_OFFSET: offset cua ham AN/DONG popup (thuong cung class, ten gan giong,
//     hoac ham set visible(false)/removeChild len cung doi tuong UI)
// Base address KHONG hardcode trong file nay - duoc Python doc dong tu /proc/pid/maps
// va thay the vao placeholder __BASE_ADDRESS__ ngay truoc khi nap script (dung quy uoc
// da lap trong run_frida.py/prepare_frida.py cua du an).
//
// CANH BAO: day la hook vao dia chi ARM ben trong process x86 chay qua Houdini. Interceptor.attach
// tren ma ARM duoc Houdini dich JIT KHONG DAM BAO hoat dong nhu hook ham x86 thuong - neu
// hook khong bao gio bi kich hoat (khong thay log "FUNC_SHOW called"), day la thong tin
// quan trong can bao cao lai, khong phai loi code.

'use strict';

const BASE_ADDRESS      = ptr('__BASE_ADDRESS__');
const FUNC_SHOW_OFFSET   = ptr('__FUNC_SHOW_OFFSET__');
const FUNC_HIDE_OFFSET   = ptr('__FUNC_HIDE_OFFSET__');
const DELAY_MS           = 5000;

const funcShowAddr = BASE_ADDRESS.add(FUNC_SHOW_OFFSET);
const funcHideAddr = BASE_ADDRESS.add(FUNC_HIDE_OFFSET);

console.log('[*] BASE_ADDRESS   = ' + BASE_ADDRESS);
console.log('[*] FUNC_SHOW addr = ' + funcShowAddr);
console.log('[*] FUNC_HIDE addr = ' + funcHideAddr);

// Doi khop byte dau (bat buoc theo quy tac phantich.md - khong tin dia chi neu chua
// doi chieu duoc voi byte that trong Ghidra disassembly/decompile cua 2 ham nay).
try {
    console.log('[*] 8 byte dau FUNC_SHOW:\n' + hexdump(funcShowAddr, { length: 8, ansi: false }));
    console.log('[*] 8 byte dau FUNC_HIDE:\n' + hexdump(funcHideAddr, { length: 8, ansi: false }));
} catch (e) {
    console.log('[!] Khong doc duoc byte tai dia chi - offset hoac base address co the sai: ' + e);
}

let hideFn;
try {
    // Gia dinh calling convention: tham so dau tien (r0/ARM, tuong duong args[0] trong
    // Frida) la con tro `this` cua doi tuong UI. Kieu tra ve 'void' la gia dinh an toan.
    hideFn = new NativeFunction(funcHideAddr, 'void', ['pointer']);
} catch (e) {
    console.log('[!] Khong tao duoc NativeFunction cho FUNC_HIDE: ' + e);
}

let attached = false;
try {
    Interceptor.attach(funcShowAddr, {
        onEnter: function (args) {
            attached = true;
            const thisPtr = args[0];
            console.log('[+] FUNC_SHOW DUOC GOI! this=' + thisPtr + ' - se goi FUNC_HIDE sau ' + DELAY_MS + 'ms...');

            setTimeout(function () {
                if (!hideFn) {
                    console.log('[!] Bo qua - FUNC_HIDE chua duoc tao thanh cong o tren.');
                    return;
                }
                console.log('[*] Dang goi FUNC_HIDE(' + thisPtr + ') ...');
                try {
                    hideFn(thisPtr);
                    console.log('[+] Da goi FUNC_HIDE XONG. Kiem tra man hinh/screenshot NGAY BAY GIO.');
                } catch (e) {
                    console.log('[!] Loi khi goi FUNC_HIDE: ' + e);
                }
            }, DELAY_MS);
        }
    });
    console.log('[*] Da attach hook vao FUNC_SHOW. Dang cho popup xuat hien...');
} catch (e) {
    console.log('[!] Khong attach duoc Interceptor vao FUNC_SHOW: ' + e);
}

// Neu sau ~20s FUNC_SHOW khong bao gio duoc goi, in canh bao de biet dia chi/offset
// co the sai hoac ham nay khong nam tren luong thuc thi thuc te.
setTimeout(function () {
    if (!attached) {
        console.log('[!] CANH BAO: sau 20s FUNC_SHOW van chua duoc goi lan nao. ' +
                     'Co the offset sai, hoac popup da hien truoc khi script duoc nap, ' +
                     'hoac Interceptor khong hoat dong tren dia chi ARM nay qua Houdini.');
    }
}, 20000);
