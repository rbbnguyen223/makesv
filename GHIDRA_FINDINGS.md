# GHIDRA FINDINGS & REVERSE ENGINEERING KNOWLEDGE BASE

## 1. Module Overview & Memory Mapping
- **Binary**: `libApplicationMain.so` (15,265,008 bytes)
  - ELF Base: `0x00000000`
  - Ghidra Image Base: `0x00010000`
  - Address Translation: `Ghidra Address = ELF File Offset + 0x00010000`
  - Architecture: ARMv7-A 32-bit (ARM mode / Thumb interwork)
- **Haxe Runtime Standard Library**: `libstd.so` (149,068 bytes)
  - Contains C-FFI primitives for networking: `socket_connect__3`, `socket_new__1`, `socket_send__4`, `socket_recv__4`.
  - Loaded dynamically via `dlopen("libstd.so")`.

---

## 2. Network Subsystem & Socket Protocol

### A. Socket Initialization & Connection Chain
1. **Trigger**:
   - `GameStateNewbie_obj::CreateCharacter` (ELF: `0x7B2AF4`, Ghidra: `0x007C2AF4`) -> Gọi `LoginHandler_obj::Connect`
   - `LoginHandler_obj::Connect(LoginData_obj, Dynamic, Dynamic)` (ELF: `0x00cfb504`, Ghidra: `0x00d0b504`)
   - `FBClientSocket_obj::connect(String host, int port)` (ELF: `0x00d0f834`, Ghidra: `0x00d1f834`)
   - `socket_connect__3` in `libstd.so` (ELF: `0x0000c970`) -> gọi `connect(sockfd, &addr, 16)`.

### B. Object Field Layout: `FBClientSocket_obj`
Reverse engineered from `__SetField` (`0x008a7dc8`) and `__Mark` (`0x008a82ac`):
- `+0x04`: `_socketHandler`
- `+0x08`: `online` (bool, 1 = connected)
- `+0x0c`: `_sock` (socket object)
- `+0x10`: `host` (String)
- `+0x18`: `port` (int)
- `+0x1c`: `_buf` (haxe.io.Bytes buffer)
- `+0x20`: `maxBufLength` (int)
- `+0x24`: `_dataLength` (int)
- `+0x28`: `_lenghtFeild` (int)
- `+0x2c`: `connectSession` (haxe.io.Bytes encryption session key)
- `+0x30`: `_mainThread` (Thread event dispatcher)
- `+0x34`: `_ioThread` (Background socket worker thread)
- `+0x38`: `timeSendAlive` (double / int64 heartbeat)
- Global `DAT_00ebbd6c`: `isBigEndian` (bool)

### C. Handshake & Symmetric XOR Cipher
Reverse engineered from `FBClientSocket_extractMessage` (`0x008a9230`), `_onReceiveSession` (`0x008a70d4`), `FUN_00b18d80`, and `FUN_00b18e44` / `FUN_00b18f3c`:
1. **Handshake**:
   - C2S Handshake: `0x63 0x00 0x00` (`cmd = 'c'`, length = 0).
   - S2C Handshake Response: `0x63` + `len` (uint16 BE) + `session_key` (e.g. 16 bytes).
   - Client stores `session_key` into `this.connectSession`, sets `online = true`, and wakes main thread.
2. **Cipher Algorithm**:
   - Key derivation (`FUN_00b18d80`):
     ```python
     sum_b = sum(session_bytes) & 0xFF
     cipher_key = bytes([b ^ sum_b for b in session_bytes])
     ```
   - Encryption / Decryption (`FUN_00b18f3c` / `FUN_00b18e44`):
     ```python
     klen = len(cipher_key)
     output = bytes([data[i] ^ ((~cipher_key[i % klen]) & 0xFF) for i in range(len(data))])
     ```

### D. Packet Framing & Serialization Format
- **Framing**:
  - Byte 0: `cmd` (uint8)
  - Bytes 1-2: `body_len` (uint16 Big Endian)
  - Bytes 3..: `body` (XOR encrypted with `connectSession`)
- **Map Serialization Format** (`haxe.ds.StringMap_obj`):
  - Key: `key_len` (uint8) + `key_bytes` (UTF-8)
  - Value:
    - Type `0x01`: String (`len`: uint16 BE + `utf8_bytes`)
    - Type `0x02`: Boolean / Byte (uint8)
    - Type `0x04`: Int32 (int32 BE)
    - Type `0x07`: Int16 / Short (int16 BE)

---

## 3. Protocol Analysis: Packet C2S #2 (Character Registration)
- **Raw Packet**: `cmd = 0x01`, `body_len = 231`.
- **Decrypted Fields**:
  - `cmd`: `'register'`
  - `ver`: `'2.1.1'`
  - `did`: `'3587103607882432-null0'` (Device ID)
  - `lgp`: `168` (Login provider)
  - `hid`: `1` (Hero ID: 1 = Xạ Thủ, 2 = Cận Chiến, 3 = Pháp Sư)
  - `typ`: `1`
  - `rers`: `''`
  - `osver`: `'unknown'`
  - `dev`: `'SAMSUNG SM-S9470'`
  - `fir`: `'REL'`
  - `con`: `'WIFI'`
  - `car`: `'Viettel Telecom'`
  - `rers2`: `'GLOBAL_ANDROID'`
  - `la`: `'VN'`
  - `pig`: `'3587103607882432-null0'`

---

## 4. Client State Map
```
[Startup / Splash]
       ↓ (HTTP GET /lmadmin/gateway2.php?func=listS)
[Server List Loaded: "Ca Cao"]
       ↓ (Tap "VÀO GAME")
[Character Selection: "CHỌN TƯỚNG"] (Xạ Thủ, Cận Chiến, Pháp Sư)
       ↓ (Tap "Tham Gia")
[TCP Connection: 192.168.1.13:8888]
       ↓ (Send Handshake: 63 00 00)
[Server S2C Handshake: 63 00 10 + SESSION_KEY]
       ↓
[Client Decrypts / connectSession Verified]
       ↓ (Send C2S #2: cmd="register", hid=1)
[Awaiting S2C Register Response -> Transition to Main Game]
```

