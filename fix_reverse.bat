@echo off
rem fix_reverse.bat - Dung lai duong ket noi game -> server sau khi LDPlayer/adb khoi dong lai.
rem File hosts cua LDPlayer tro cac ten mien cua game ve 127.0.0.1, nen moi lan LDPlayer/adb restart
rem phai chay lai file nay (roi moi mo game). python rebuild.py phai dang chay.
rem Cong 80 tren may ao la cong "dac quyen": chi bind duoc khi LDPlayer bat quyen ROOT.
cd /d "%~dp0"

echo --- Quyen hien tai cua adb shell (uid=0 la root, OK; uid=2000 la shell, KHONG du):
adb.exe shell id
echo.

adb.exe reverse tcp:8888 tcp:8888
adb.exe reverse tcp:80 tcp:80
if errorlevel 1 (
  echo.
  echo *** KHONG bind duoc cong 80: LDPlayer chua bat quyen Root. ***
  echo Cach sua: LDPlayer ^> Cai dat ^> Cai dat khac ^> "Quyen Root" = BAT ^> Luu ^> khoi dong lai LDPlayer.
  echo Xong chay lai file nay.
) else (
  echo.
  echo Reverse cong 80: OK
)
echo.
echo Cac reverse dang co:
adb.exe reverse --list
echo.
echo Can thay CA "tcp:80 tcp:80" va "tcp:8888 tcp:8888" trong danh sach tren.
pause
