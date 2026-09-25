@echo off
rem grab_crash.bat - Lay logcat sau khi game van, ghi vao logcat_new.txt
rem Cach dung: 1) chay rebuild.py  2) chay file nay  3) mo game cho toi khi van  4) nhan phim bat ky o cua so nay
cd /d "%~dp0"
echo === Thiet bi adb dang thay ===
adb.exe devices
echo.
adb.exe logcat -c
echo Da xoa logcat cu.
echo Bay gio mo game trong LDPlayer, cho toi khi game van.
echo Sau khi van, quay lai cua so nay va nhan phim bat ky.
pause
adb.exe logcat -d -b all > logcat_new.txt
echo.
echo Da ghi logcat_new.txt. Nhan "xong" cho Claude.
pause
