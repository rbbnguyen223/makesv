@echo off
rem test_cycle.bat - Xoa cache game, mo game, doi 40 giay, luu log
rem Truoc khi chay: python rebuild.py phai dang chay.
cd /d "%~dp0"

echo [0/5] Thiet bi adb:
adb.exe devices
echo.

echo [1/5] Liet ke cache cua game TRUOC khi xoa -^> cache_list_before.txt
adb.exe shell "ls -laR /sdcard/Android/data/lmah.vn /data/data/lmah.vn 2>&1" > cache_list_before.txt

echo [2/5] Xoa du lieu game (pm clear)
adb.exe shell pm clear lmah.vn

echo [3/5] Xoa logcat cu
adb.exe logcat -c

echo [4/5] Mo game
adb.exe shell monkey -p lmah.vn -c android.intent.category.LAUNCHER 1
echo Cho 40 giay (neu game van som hon van cu cho het gio)...
timeout /t 40 /nobreak >nul

echo [5/5] Luu log
adb.exe logcat -d -b all > logcat_new.txt
adb.exe logcat -d -b crash > crash_only.txt
adb.exe shell "ls -laR /sdcard/Android/data/lmah.vn /data/data/lmah.vn 2>&1" > cache_list_after.txt

echo.
echo Xong. Cac file: cache_list_before.txt, cache_list_after.txt, logcat_new.txt, crash_only.txt, server.log
echo Nhan "xong" cho Claude.
pause
