@echo off
rem push_so.bat - wrapper gọi push_so.py
cd /d "%~dp0"
echo === PUSH SO: %date% %time% ===
python push_so.py
if errorlevel 1 (
    echo.
    echo FAILED. Xem loi o tren.
    pause
    exit /b 1
)
pause
