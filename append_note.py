with open('TONG_HOP.md', 'a', encoding='utf-8') as f:
    f.write('\n\n**Kiến thức quan trọng về Frida trên LDPlayer (Houdini):** "Frida x86 không enumerate được module ARM qua Houdini do bỏ qua linker host; phải lấy base address qua `/proc/pid/maps` + hook bằng raw pointer." (Xác nhận ngày 23/09, không dùng frida-server ARM vì sẽ bị `Exec format error` trên kernel x86).\n')
