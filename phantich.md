# PHÂN TÍCH KỸ THUẬT & HƯỚNG DẪN ĐIỀU TRA REVERSE-ENGINEERING

═══════════════════════════════════════════
0. KIẾN TRÚC MẠNG CHUẨN CỦA DỰ ÁN (CẬP NHẬT 23/09/2026)
═══════════════════════════════════════════
- Không sử dụng IP LAN tĩnh `192.168.1.13` (dễ bị thay đổi theo DHCP của router Wi-Fi).
- Toàn bộ kết nối chuyển hướng về **`127.0.0.1`**:
  - File `/system/etc/hosts` trên LDPlayer:
    `127.0.0.1 localhost lienminh.g6-mobile.zing.vn lienminh.static.g6.zing.vn me.zing.vn`
  - Cổng mạng được đảo chiều bằng ADB:
    `adb -s emulator-5554 reverse tcp:80 tcp:80`
    `adb -s emulator-5554 reverse tcp:8888 tcp:8888`
  - Fallback iptables nếu port < 1024 bị chặn:
    `iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-ports 8080`

═══════════════════════════════════════════
1. ĐỐI TƯỢNG VÀ TRẠNG THÁI HIỆN TẠI CỦA CLIENT
═══════════════════════════════════════════
1. **Khởi tạo đối tượng**:
   Logcat LDPlayer xác nhận đối tượng `PlayerBase` đã được khởi tạo thành công khi bấm "Chơi ngay":
   `D lmah.vn : PlayerBase::PlayerBase()`
   `D lmah.vn : TrackPlayerBase::TrackPlayerBase()`
2. **Gói tin TCP đầu tiên sau handshake**:
   Client gửi `cmd=0x01` với `req_cmd='register'` và tham số `hid: 0` (chưa có tướng ban đầu).
3. **Phản hồi từ Server**:
   Giao thức nhị phân của Haxe OpenFL yêu cầu dữ liệu kiểu số nguyên phải được đóng gói đúng chuẩn type byte `0x04` (int32) thay vì chuỗi type `0x01`.
   Đồng thời dữ liệu Gateway (`listS`) cần thống nhất cấu trúc nhân vật với TCP server để tránh client bị treo ở trạng thái chờ tạo tướng.

═══════════════════════════════════════════
2. QUY TRÌNH KIỂM THỬ CHUẨN
═══════════════════════════════════════════
1. Chạy file kịch bản `run_test_cycle.py` (phiên bản v2.0.0 đã trỏ `127.0.0.1` và gắn định danh `emulator-5554`).
2. Quan sát log TCP hiển thị trên console `rebuild.py`.
3. Kiểm tra ảnh chụp màn hình kéo về tại `current_screen.png`.