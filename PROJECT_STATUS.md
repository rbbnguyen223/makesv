# MASTER TECHNICAL STATUS REPORT: REBUILD OFFLINE "LIÊN MINH ANH HÙNG" (lmah.vn)

> **Document Version**: 1.2.0 (Cập nhật 23/09/2026: Chuyển toàn bộ kiến trúc mạng từ IP LAN cũ sang Loopback 127.0.0.1 + ADB Reverse trên LDPlayer)  
> **Status**: [IN PROGRESS] — Pipeline ZCE -> Gateway -> CDN -> Đăng nhập -> Chọn Server -> Chọn Tướng -> TCP Handshake -> Gói tin Register đã hoạt động 100% trên `127.0.0.1`.

---

# 1. PROJECT OVERVIEW

- **Tên project**: Rebuild Game Offline "Liên Minh Anh Hùng" (LMHB / lmah.vn)
- **Mục tiêu**: Chạy offline 100% không cần Internet client game Android `Liên Minh Anh Hùng 2.1.1` trên giả lập LDPlayer, kết nối server cục bộ (fake server), vượt qua xác thực ZCE, Gateway, CDN, đăng nhập, chọn server, khởi tạo/chọn nhân vật, tải dữ liệu nhân vật, trang bị, bản đồ và vào thế giới game.
- **Game / APK**: `Liên+Minh+Anh+Hùng_2.1.1_APKPure.apk`
- **Package name**: `lmah.vn`
- **Main Activity**: `lmah.vn.MainActivity`
- **Version**: `2.1.1`
- **Engine**: Haxe 3.x + OpenFL (NME / hxcpp runtime, compiled native C++)
- **Architecture**: ARMv7-A 32-bit (`armeabi`), chạy trên Android x86 thông qua Intel `libhoudini` binary translator
- **Runtime Environment**: LDPlayer 9 (Android 9/14, ABI x86, screen resolution 540x960 portrait)
- **Fake Server**: `rebuild.py` (FastAPI HTTP Server + Asyncio TCP Socket Server v3.9.7)
- **Server IP**: `127.0.0.1` (kết hợp `adb -s emulator-5554 reverse`)
- **Server Ports**:
  - HTTP: `80` (Gateway API, CDN Static Asset Server, Zing Auth)
  - TCP: `8888` (Game Socket Protocol)

---

# 2. CURRENT STATUS

Game đã khởi động thành công, nạp file `.so` patched an toàn, vượt qua toàn bộ xác thực ZCE/Gateway, tải CDN asset dự phòng, hiển thị màn hình đăng nhập, chọn server "Ca Cao", vào giao diện "CHỌN TƯỚNG" (hoặc nhận diện nhân vật), và kết nối socket TCP tới `127.0.0.1:8888`. Server và Client đã thực hiện bắt tay (handshake `0x63`) thành công, trao đổi khóa mã hóa đối xứng XOR.

**CHECKPOINT HIỆN TẠI: ĐỒNG BỘ DỮ LIỆU NHÂN VẬT SAU GÓI REGISTER/LOGINGAME**  
Client nhận gói phản hồi từ server nhưng giữ màn hình nạp dữ liệu ("Tải dữ liệu nhân vật" / "Xin chờ giây lát") và chưa gửi tiếp các bản tin đồng bộ bản đồ / giao diện chính.

---

# 3. COMPLETE FLOW MAP