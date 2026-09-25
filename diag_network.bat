@echo off
rem diag_network.bat - Chan doan vi sao game "khong co mang" / khong toi duoc server. Ket qua: net_diag.txt + so_strings.txt
rem Truoc khi chay: python rebuild.py phai dang chay (de kiem tra LDPlayer goi duoc toi server).
cd /d "%~dp0"

echo Chan doan mang LDPlayer - %date% %time% > net_diag.txt

echo. >> net_diag.txt & echo === adb devices === >> net_diag.txt
adb.exe devices >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === adb shell id (root hay khong) === >> net_diag.txt
adb.exe shell id >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === /system/etc/hosts === >> net_diag.txt
adb.exe shell "cat /system/etc/hosts" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === adb reverse --list === >> net_diag.txt
adb.exe reverse --list >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === adb forward --list === >> net_diag.txt
adb.exe forward --list >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === http_proxy (settings) === >> net_diag.txt
adb.exe shell settings get global http_proxy >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === ip addr + route === >> net_diag.txt
adb.exe shell "ip -4 addr; ip route" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === getprop dns/proxy === >> net_diag.txt
adb.exe shell "getprop | grep -iE 'dns|proxy'" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === VPN / Drony trong connectivity === >> net_diag.txt
adb.exe shell "dumpsys connectivity | grep -iE 'VPN|Drony|VALIDATED' | head -20" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === tien trinh drony/proxy/vpn === >> net_diag.txt
adb.exe shell "ps -A | grep -iE 'drony|proxy|vpn'" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === ping 192.168.1.13 === >> net_diag.txt
adb.exe shell "ping -c 1 -W 2 192.168.1.13" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === goi thang HTTP toi 192.168.1.13:80 (nc) === >> net_diag.txt
adb.exe shell "printf 'GET /lmadmin/gateway2.php?func=listS HTTP/1.0\r\n\r\n' | nc -w 3 192.168.1.13 80 | head -c 300" >> net_diag.txt 2>&1

echo. >> net_diag.txt & echo === Xong === >> net_diag.txt
python find_domains.py

echo.
echo Xong. Nhan "xong" cho Claude. (net_diag.txt, so_strings.txt, server.log)
pause
