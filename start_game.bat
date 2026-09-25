@echo off
title LMHB Offline Auto Launcher
chcp 65001 >nul
cls

set DEVICE=emulator-5554

echo ===================================================
echo [1/4] Dang kiem tra va cap quyen Root cho LDPlayer...
echo ===================================================
adb -s %DEVICE% root >nul 2>&1
timeout /t 1 >nul

echo ===================================================
echo [2/4] Cau hinh Hosts va Reverse Port (80 & 8888)...
echo ===================================================
adb -s %DEVICE% shell "mount -o rw,remount /system >nul 2>&1 || mount -o rw,remount / >nul 2>&1"
adb -s %DEVICE% shell "echo '127.0.0.1 localhost lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn' > /etc/hosts"
adb -s %DEVICE% shell "echo '127.0.0.1 localhost lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn' > /system/etc/hosts"

adb -s %DEVICE% reverse --remove-all >nul 2>&1
adb -s %DEVICE% reverse tcp:80 tcp:80 >nul 2>&1
adb -s %DEVICE% reverse tcp:8888 tcp:8888 >nul 2>&1

:: Fallback phong truong hop LDPlayer bi loi Permission denied o port 80
adb -s %DEVICE% reverse tcp:8080 tcp:80 >nul 2>&1
adb -s %DEVICE% shell "iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-ports 8080 >nul 2>&1"

echo ===================================================
echo [3/4] Khoi dong Mock Server (rebuild.py)...
echo ===================================================
start "LMHB Local Server" python rebuild.py

echo ===================================================
echo [4/4] Mo game tren LDPlayer...
echo ===================================================
adb -s %DEVICE% shell am force-stop lmah.vn
adb -s %DEVICE% shell am start -n lmah.vn/lmah.vn.MainActivity >nul 2>&1

echo.
echo >>> HOAN TAT! Game da duoc mo, chuc Anh choi game vui ve!
timeout /t 3 >nul
exit