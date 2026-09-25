@echo off
rem disasm.bat - Cai capstone (thu vien dich nguoc) roi dich nguoc cac vung quan trong trong libApplicationMain.so goc
rem Can Internet cho lan cai dau tien. Ket qua: disasm.txt
cd /d "%~dp0"
python -m pip install capstone
echo.
python disasm.py
echo.
echo Xong. Nhan "xong" cho Claude. (disasm.txt)
pause
