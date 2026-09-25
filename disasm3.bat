@echo off
rem disasm3.bat - Dich nguoc backtrace crash moi (ban 1-patch)
cd /d "%~dp0"
python disasm3.py
if errorlevel 1 (
    echo FAILED. Thu: pip install capstone
    pause
)
echo.
echo Xong. Doc disasm3.txt roi gui cho Claude.
pause
