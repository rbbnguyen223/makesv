@echo off
rem set_hosts.bat - Phuong an B: khong dung adb reverse cong 80. Thay vao do "ghi de" file hosts cua LDPlayer
rem de 3 ten mien cua game tro thang ve 192.168.1.13 (may chay rebuild.py).
rem Can quyen root TREN MAY AO (su). Script thu nhieu cach va in ket qua tung buoc.
rem Ghi de bang bind mount nen MAT khi khoi dong lai LDPlayer -> chay lai file nay sau moi lan restart.
cd /d "%~dp0"

echo ===== 1. adb root =====
adb.exe root
timeout /t 3 /nobreak >nul
adb.exe shell id
echo.

echo ===== 2. su co dung duoc khong? =====
adb.exe shell "su -c id"
adb.exe shell "su 0 id"
echo.

echo ===== 3. Tao file hosts moi va day len may ao =====
> hosts_new.txt echo 127.0.0.1 localhost
>> hosts_new.txt echo 192.168.1.13 lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn
adb.exe push hosts_new.txt /data/local/tmp/hosts_new
echo.

echo ===== 4. Ghi de /system/etc/hosts (thu 3 cach) =====
adb.exe shell "mount -o bind /data/local/tmp/hosts_new /system/etc/hosts"
adb.exe shell "su -c 'mount -o bind /data/local/tmp/hosts_new /system/etc/hosts'"
adb.exe shell "su 0 mount -o bind /data/local/tmp/hosts_new /system/etc/hosts"
echo.

echo ===== 5. Ket qua: noi dung /system/etc/hosts hien tai =====
adb.exe shell cat /system/etc/hosts
echo.
echo Neu dong tren co 192.168.1.13 thi da OK: mo game va nhin cua so rebuild.py.
echo Neu van la 127.0.0.1 thi ca 3 cach deu that bai (may ao khong co root).
pause
