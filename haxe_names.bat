@echo off
rem haxe_names.bat - Liet ke ten ham Haxe quanh cac diem crash/vá. Ket qua: func_names_focus.txt
cd /d "%~dp0"
python haxe_names.py
echo.
echo Xong. Nhan "xong" cho Claude. (func_names_focus.txt)
pause
