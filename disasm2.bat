@echo off
rem disasm2.bat - Tim ten ham/lop cua cac diem crash va vá trong libApplicationMain.so goc. Ket qua: disasm2.txt
cd /d "%~dp0"
python disasm2.py
echo.
echo Xong. Nhan "xong" cho Claude. (disasm2.txt)
pause
