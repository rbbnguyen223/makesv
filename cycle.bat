@echo off
rem cycle.bat - MOT LAN CHAY LAM TAT CA: dam bao root + hosts + server, xoa cache, mo game, tu bam vao game,
rem chup man hinh moi 3 giay, thu log, roi tom tat vao cycle_report.txt (chi can gui "xong" cho Claude).
rem Khong can chay rebuild.py hay set_hosts.bat truoc: file nay tu lam.
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo === CYCLE %date% %time% === > cycle_report.txt
echo cdn_mode: >> cycle_report.txt
type cdn_mode.txt >> cycle_report.txt 2>nul
echo. >> cycle_report.txt

echo [1/8] Bat root + ghi de hosts
adb.exe root >nul 2>&1
timeout /t 3 /nobreak >nul
adb.exe shell id >> cycle_report.txt 2>&1
> hosts_new.txt echo 127.0.0.1 localhost
>> hosts_new.txt echo 192.168.1.13 lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn
adb.exe push hosts_new.txt /data/local/tmp/hosts_new >nul 2>&1
adb.exe shell "mount -o bind /data/local/tmp/hosts_new /system/etc/hosts" >nul 2>&1
echo hosts hien tai: >> cycle_report.txt
adb.exe shell cat /system/etc/hosts >> cycle_report.txt 2>&1

echo [2/8] Bao dam server dang chay
netstat -ano | findstr ":80 " | findstr LISTENING >nul
if errorlevel 1 (
  echo   Server chua chay -> khoi dong rebuild.py trong cua so moi
  start "rebuild server" cmd /k python rebuild.py
  timeout /t 6 /nobreak >nul
) else (
  echo   Server dang chay
)
set L0=0
for /f %%a in ('powershell -NoProfile -Command "if (Test-Path server.log) { (Get-Content server.log).Count } else { 0 }"') do set L0=%%a

echo [3/8] Kiem tra .so dang cai trong LDPlayer
echo. >> cycle_report.txt
echo === .so dang cai trong LDPlayer === >> cycle_report.txt
adb.exe shell "ls -la /data/app/lmah.vn-1/lib/arm/libApplicationMain.so" >> cycle_report.txt 2>&1
adb.exe shell "ls -la /data/app/lmah.vn-2/lib/arm/libApplicationMain.so" >> cycle_report.txt 2>&1

echo [4/8] Xoa cache game va mo game
adb.exe shell am force-stop lmah.vn
adb.exe shell "rm -f /data/data/lmah.vn/files/*.png"
adb.exe logcat -c
adb.exe shell am start -n lmah.vn/lmah.vn.MainActivity >nul 2>&1

echo [5/8] Tu bam vao game
timeout /t 12 /nobreak >nul
adb.exe shell input tap 270 729
timeout /t 5 /nobreak >nul
adb.exe shell input tap 270 773

echo [6/8] Chup man hinh moi 3 giay (45 giay)
if not exist shots mkdir shots
del /q shots\*.png >nul 2>&1
for /l %%i in (1,1,15) do (
  timeout /t 3 /nobreak >nul
  adb.exe exec-out screencap -p > shots\s%%i.png
)

echo [7/8] Thu log
adb.exe logcat -d -b crash > crash_cycle.txt
adb.exe logcat -d -v time | findstr /i /c:"lmah" /c:"houdini" /c:"FBSession" /c:"NME" /c:"TCP" /c:"GLThread" > game_cycle.txt

echo [8/8] Tom tat vao cycle_report.txt
echo. >> cycle_report.txt
echo === pid game (trong = da chet) === >> cycle_report.txt
adb.exe shell pidof lmah.vn >> cycle_report.txt 2>&1
echo. >> cycle_report.txt
echo === crash === >> cycle_report.txt
findstr /c:"Fatal signal" /c:"Process uptime" /c:"fault addr" crash_cycle.txt >> cycle_report.txt 2>&1
findstr /i /c:"illegal address" /c:"arm backtrace" /c:"  #0" game_cycle.txt >> cycle_report.txt 2>&1
echo. >> cycle_report.txt
echo === thanh ghi + bo nho luc crash (GLThread, de Claude doc r4/eax..edi/ebp truc tiep, khong doan tu disasm) === >> cycle_report.txt
powershell -NoProfile -Command "$c=Get-Content crash_cycle.txt; $i=($c | Select-String 'GLThread' | Select-Object -First 1).LineNumber; if($i){ $c[($i-1)..([Math]::Min($c.Count-1,$i+59))] } else { 'khong tim thay GLThread trong crash_cycle.txt' }" >> cycle_report.txt 2>&1
echo. >> cycle_report.txt
echo === request server trong lan chay nay === >> cycle_report.txt
powershell -NoProfile -Command "Get-Content server.log | Select-Object -Skip %L0%" >> cycle_report.txt 2>&1
echo. >> cycle_report.txt
echo === captures TCP (co ket noi TCP khong?) === >> cycle_report.txt
adb.exe shell "ls -la /data/local/tmp/ | grep -i cap" >> cycle_report.txt 2>&1
dir /b captures\ >> cycle_report.txt 2>&1
echo. >> cycle_report.txt
echo === anh chup: shots\s1.png ... s15.png (moi 3 giay) === >> cycle_report.txt

echo.
echo Xong. Nhan "xong" cho Claude. (cycle_report.txt, shots\, crash_cycle.txt)
pause
