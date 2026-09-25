@echo off
rem run_matrix.bat (v3) - Thu 4 che do tra file CDN thieu, TU BAM vao game va chup man hinh tung buoc.
rem v3: KHONG dung pm clear nua (pm clear reset quyen -> hien man hinh "Tiep tuc" chan game).
rem     Chi xoa cac file .png game da luu tam, roi mo game va tu bam "Choi ngay" -> "VAO GAME".
rem
rem TRUOC KHI CHAY (chi 1 lan): mo game bang tay trong LDPlayer, bam "Tiep tuc" cho toi khi thay man hinh
rem   dang nhap (Zing me / facebook / Choi ngay), roi bam nut Home. Sau do moi chay file nay.
rem python rebuild.py phai dang chay. Moi che do ~55 giay, tong ~4 phut. Dung cham vao LDPlayer.
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo Ket qua thu nghiem CDN v3 - %date% %time% > results.txt
echo. >> results.txt
adb.exe root >nul 2>&1
timeout /t 3 /nobreak >nul
echo === quyen adb (uid=0 la root, can de xoa cache game) === >> results.txt
adb.exe shell id >> results.txt 2>&1
echo === hosts (phai la 192.168.1.13; neu la 127.0.0.1 thi chay set_hosts.bat truoc) === >> results.txt
adb.exe shell cat /system/etc/hosts >> results.txt 2>&1
echo. >> results.txt
echo === LDPlayer ping duoc may chay server? === >> results.txt
adb.exe shell "ping -c 1 -W 2 192.168.1.13" >> results.txt 2>&1
echo. >> results.txt

for %%M in (404 blank512 blank1024 blank2048) do (
  echo.
  echo ===== Che do: %%M =====
  > cdn_mode.txt echo %%M
  adb.exe shell am force-stop lmah.vn
  adb.exe shell "rm -f /data/data/lmah.vn/files/*.png"
  adb.exe logcat -c
  echo --- %%M >> results.txt
  adb.exe shell am start -n lmah.vn/lmah.vn.MainActivity >> results.txt 2>&1

  timeout /t 12 /nobreak >nul
  adb.exe exec-out screencap -p > shot_%%M_1_login.png
  adb.exe shell input tap 270 729
  timeout /t 5 /nobreak >nul
  adb.exe exec-out screencap -p > shot_%%M_2_sau_choingay.png
  adb.exe shell input tap 270 773
  timeout /t 5 /nobreak >nul
  adb.exe exec-out screencap -p > shot_%%M_3_sau_vaogame.png
  timeout /t 25 /nobreak >nul
  adb.exe exec-out screencap -p > shot_%%M_4_cuoi.png

  echo   cua so dang hien thi: >> results.txt
  adb.exe shell "dumpsys window | grep mCurrentFocus" >> results.txt 2>&1
  echo   pid game: >> results.txt
  adb.exe shell pidof lmah.vn >> results.txt 2>&1
  echo   so file png game da tai ve: >> results.txt
  adb.exe shell "ls /data/data/lmah.vn/files | grep -c png" >> results.txt 2>&1

  adb.exe logcat -d -b crash > crash_%%M.txt
  findstr /c:"Fatal signal" "crash_%%M.txt" >nul
  if errorlevel 1 (
    echo   khong co crash native >> results.txt
  ) else (
    echo   CRASH: >> results.txt
    findstr /c:"Fatal signal" /c:"Process uptime" "crash_%%M.txt" >> results.txt
  )
  adb.exe logcat -d -v time | findstr /i /c:"lmah" /c:"houdini" /c:"FBSession" /c:"NME" > game_%%M.txt
)

> cdn_mode.txt echo blank512
adb.exe shell am force-stop lmah.vn
echo.
echo Xong. Nhan "xong" cho Claude. (results.txt, shot_*.png, crash_*.txt, game_*.txt, server.log)
pause
