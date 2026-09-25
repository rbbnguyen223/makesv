@echo off
rem analyze.bat - 1) keo ban libApplicationMain.so DANG CAI trong LDPlayer ve (installed.so)
rem               2) so sanh no voi cac ban va ban goc (so_report.txt)
rem               3) trich cac ten truong/lop lien quan server, phien, dang nhap tu ban goc (so_fields.txt)
cd /d "%~dp0"

adb.exe root >nul 2>&1
timeout /t 3 /nobreak >nul

set SOPATH=
for /f "delims=" %%P in ('adb.exe exec-out "ls /data/app/*/lmah.vn-*/lib/arm/libApplicationMain.so"') do set SOPATH=%%P
echo Ban .so dang cai tren may ao: %SOPATH%
if "%SOPATH%"=="" (
  echo Khong tim thay file .so tren may ao. Bo qua buoc keo ve.
) else (
  del installed.so >nul 2>&1
  adb.exe pull "%SOPATH%" installed.so
)

python so_report.py
python find_fields.py

echo.
echo Xong. Nhan "xong" cho Claude. (so_report.txt, so_fields.txt)
pause
