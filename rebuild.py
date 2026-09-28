# ==============================================================================
# Project: Offline Local Mock Server for LMHB (lmah.vn)
# Version: 3.9.7 - Full Code: Force Pre-existing Character on Gateway & TCP
# Deep protocol analysis pending
# ==============================================================================

import asyncio
import json
import logging
import mimetypes
import struct
import zlib
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(BASE_DIR / "server.log", mode="w", encoding="utf-8"),
    ],
)
logger = logging.getLogger("LMHB_Server")

app = FastAPI(title="LMAH Server v3.9.7", version="3.9.7")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOCAL_IP  = "127.0.0.1"
HTTP_PORT = 80
GAME_PORT = 8888

CDN_DIRS = [
    BASE_DIR / "cdn_assets",
    BASE_DIR / "repo_apk_extracted" / "assets" / "assets",
    BASE_DIR / "noembed_files",
]

CAPTURE_DIR = BASE_DIR / "captures"
DATA_FILE = BASE_DIR / "game_data.json"
CDN_MODE_FILE = BASE_DIR / "cdn_mode.txt"

LEGACY_CDN = False
_BLANK_CACHE = {}

def load_game_data() -> dict:
    if DATA_FILE.is_file():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            logger.error(f"Lỗi đọc game_data.json: {e}")
    return {
        "user": {
            "uid": 10001,
            "userId": 10001,
            "accid": 10001,
            "name": "Anh Hoàng Đẹp Trai",
            "username": "Anh Hoàng Đẹp Trai",
            "level": 1,
            "userLv": 1,
            "serverId": 1,
            "gold": 9999999,
            "coin": 9999999,
            "gem": 999999,
            "diamond": 999999,
            "vip": 10,
            "exp": 0,
            "energy": 999,
            "heroes": "2:1:0"
        },
        "session": {
            "sid": "10001_offline_sid",
            "sessionId": "mock_offline_session_12345"
        }
    }

def generate_safe_png(width=512, height=512) -> bytes:
    raw_data = b"".join(b"\x00" + b"\x00\x00\x00\x00" * width for _ in range(height))
    compressed = zlib.compress(raw_data)

    def chunk(tag: bytes, data: bytes) -> bytes:
        length = struct.pack(">I", len(data))
        crc = struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        return length + tag + data + crc

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")

SAFE_512_PNG = generate_safe_png(512, 512)

# ==============================================================================
# 0. Middleware: Log mọi HTTP request
# ==============================================================================
@app.middleware("http")
async def log_all_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info(f"[HTTP] {request.method} {request.url.path} host={request.headers.get('host')} -> {response.status_code}")
    return response

# ==============================================================================
# 1. Phục vụ CDN Assets
# ==============================================================================
def find_cdn_file(filename: str):
    if not filename:
        return None
    for d in CDN_DIRS:
        if not d.is_dir():
            continue
        f = d / filename
        if f.is_file():
            return f
    return None

def get_cdn_mode() -> str:
    try:
        return CDN_MODE_FILE.read_text(encoding="utf-8").strip().lower() or "blank512"
    except Exception:
        return "blank512"

def get_blank_png(size: int) -> bytes:
    if size not in _BLANK_CACHE:
        _BLANK_CACHE[size] = SAFE_512_PNG if size == 512 else generate_safe_png(size, size)
    return _BLANK_CACHE[size]

@app.get("/cdn/{rest_of_path:path}")
async def serve_cdn(request: Request, rest_of_path: str):
    filename = rest_of_path.replace("\\", "/").split("/")[-1]
    if LEGACY_CDN:
        return Response(content=SAFE_512_PNG, media_type="image/png", status_code=200)
    f = find_cdn_file(filename)
    if f is not None:
        mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        logger.info(f"[CDN HIT ] {filename} ({f.stat().st_size} B) <- {f.parent.name}")
        return Response(content=f.read_bytes(), media_type=mime, status_code=200)

    mode = get_cdn_mode()
    if filename.lower().endswith(".png") and mode.startswith("blank"):
        try:
            size = int(mode[5:])
        except ValueError:
            size = 512
        logger.warning(f"[CDN MISS] {filename} -> PNG trắng {size}x{size} (mode={mode})")
        return Response(content=get_blank_png(size), media_type="image/png", status_code=200)

    logger.warning(f"[CDN MISS] {filename} -> 404 (mode={mode})")
    return Response(status_code=404)

# ==============================================================================
# 2. Zing Authentication Routes
# ==============================================================================
@app.api_route("/apps/mobile/android", methods=["GET", "POST"])
@app.api_route("/id/mobile/android", methods=["GET", "POST"])
@app.api_route("/sdk/mobile/android", methods=["GET", "POST"])
@app.api_route("/oauth/mobile/android", methods=["GET", "POST"])
async def handle_zce(request: Request):
    return JSONResponse(content={
        "return_code": 1, "code": 1, "status": 1, "ErrorCode": 0, "error": 0, "message": "success",
        "data": {"session": "mock_offline_session_token", "access_token": "mock_access_token_12345", "uid": "10001", "status": 1}
    })

@app.api_route("/mzt/h", methods=["GET", "POST"])
async def handle_mzt(request: Request):
    return JSONResponse(content={
        "error": 0, "code": 0, "status": 1, "ErrorCode": 0, "Message": "success",
        "data": {"session": "mock_offline_session_token", "uid": "10001", "mzt": "mock_mzt_token_12345"}
    })

# ==============================================================================
# 3. Game Gateway (listS, login, constants)
# ==============================================================================
@app.api_route("/lmadmin/gateway2.php", methods=["GET", "POST"])
async def handle_gateway2(request: Request):
    params = dict(request.query_params)
    func = params.get("func", "")
    version = params.get("version", "2.1.1")
    gdata = load_game_data()
    u = gdata["user"]
    s = gdata["session"]

    logger.info(f"[Gateway] func={func} | params={params}")

    role_info = {
        "userId": str(u.get("uid", 10001)),
        "accid": str(u.get("accid", 10001)),
        "username": u.get("username", "Anh Hoàng Đẹp Trai"),
        "userName": u.get("username", "Anh Hoàng Đẹp Trai"),
        "user_name": u.get("username", "Anh Hoàng Đẹp Trai"),
        "name": u.get("name", "Anh Hoàng Đẹp Trai"),
        "roleName": u.get("name", "Anh Hoàng Đẹp Trai"),
        "userLv": u.get("level", 1),
        "level": u.get("level", 1),
        "id": 1,
        "serverId": 1,
        "server_id": 1,
        "heroId": 2,
        "hid": 2,
        "hasRole": 1,
        "isNew": 0,
        "vip": u.get("vip", 10),
        "session": s.get("sessionId", "mock_offline_session_12345"),
        "sessionId": s.get("sessionId", "mock_offline_session_12345"),
        "pass": "",
        "health": 100,
        "loginType": 0,
        "ip": LOCAL_IP,
        "host": LOCAL_IP,
        "port": GAME_PORT,
        "serverPort": GAME_PORT,
        "serverAddress": f"{LOCAL_IP}:{GAME_PORT}"
    }

    server_item = {
        "id": 1, "serverId": 1, "server_id": 1,
        "serverName": "Ca Cao", "server_name": "Ca Cao", "name": "Ca Cao",
        "ip": LOCAL_IP, "host": LOCAL_IP, "port": GAME_PORT,
        "serverPort": GAME_PORT, "server_port": GAME_PORT,
        "serverAddress": f"{LOCAL_IP}:{GAME_PORT}", "server_address": f"{LOCAL_IP}:{GAME_PORT}",
        "stt": 1, "status": 1, "state": 1, "stt_lb": "Hot", "live": 1, "updated": 1, "health": 100,
        "userLv": u.get("level", 1), "level": u.get("level", 1),
        "userId": str(u.get("uid", 10001)), "userName": u.get("username", "Anh Hoàng Đẹp Trai"),
        "session": s.get("sessionId", "mock_offline_session_12345"),
        "sessionId": s.get("sessionId", "mock_offline_session_12345"),
        "include": 1, "pass": "", "isOverride": 0, "language": "VN",
        "accounts": [role_info]
    }

    if func == "listS":
        return JSONResponse(content={
            "Transactions": [],
            "ErrorCode": 0,
            "Message": "success",
            "accid": str(u.get("accid", 10001)),
            "lastServerId": 1,
            "servers": [server_item],
            "accounts": [role_info],
            "roles": [role_info],
            "lastRole": role_info,
            "hasRole": 1,
            "heroId": 2,
            "sessionId": s.get("sessionId", "mock_offline_session_12345"),
            "startConnect": 1,
            "version": version,
            "forceUpdate": 0,
            "needUpdate": 0,
            "maintenance": 0,
            "events": [],
            "banners": []
        })

    if func == "login":
        return JSONResponse(content={
            "ErrorCode": 0,
            "Message": "success",
            "accid": str(u.get("accid", 10001)),
            "sessionId": s.get("sessionId", "mock_offline_session_12345"),
            "userId": str(u.get("uid", 10001)),
            "serverId": 1,
            "ip": LOCAL_IP,
            "host": LOCAL_IP,
            "port": GAME_PORT,
            "hasRole": 0,
            "heroId": 0,
            "role": role_info,
            "data": {
                "userId": str(u.get("uid", 10001)),
                "sessionId": s.get("sessionId", "mock_offline_session_12345"),
                "ip": LOCAL_IP,
                "host": LOCAL_IP,
                "port": GAME_PORT,
                "heroId": 0,
                "hasRole": 0
            }
        })

    if func in ("getServerConstant", "getConstance"):
        return JSONResponse(content={
            "ErrorCode": 0, "Message": "success", "status": 1,
            "data": {"VERSION": version, "needUpdate": 0, "forceUpdate": 0, "SHOW_EVENT": 0, "SHOW_BANNER": 0}
        })

    return JSONResponse(content={"ErrorCode": 0, "status": 1, "code": 0, "Message": "success"})

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(request: Request, full_path: str):
    return JSONResponse(content={"status": 1, "code": 200, "ErrorCode": 0, "Message": "success", "data": {"result": 1}})

# ==============================================================================
# 4. TCP Game Socket Protocol Engine
# ==============================================================================
_conn_counter = 0
SESSION_KEY = b"1234567812345678"

def make_cipher_key(session: bytes) -> bytes:
    sum_b = sum(session) & 0xFF
    return bytes([b ^ sum_b for b in session])

def xor_crypt(data: bytes, session: bytes) -> bytes:
    key = make_cipher_key(session)
    klen = len(key)
    out = bytearray(len(data))
    for i in range(len(data)):
        bVar7 = (~key[i % klen]) & 0xFF
        out[i] = data[i] ^ bVar7
    return bytes(out)

def serialize_map(d: dict) -> bytes:
    out = bytearray()
    for k, v in d.items():
        k_b = str(k).encode("utf-8")
        out.append(len(k_b))
        out.extend(k_b)
        if isinstance(v, str):
            v_b = v.encode("utf-8")
            out.append(1)
            out.extend(struct.pack(">H", len(v_b)))
            out.extend(v_b)
        elif isinstance(v, bool):
            out.append(2)
            out.append(1 if v else 0)
        elif isinstance(v, int):
            out.append(4)
            out.extend(struct.pack(">i", v))
        elif isinstance(v, bytes):
            out.append(1)
            out.extend(struct.pack(">H", len(v)))
            out.extend(v)
    return bytes(out)

def parse_map(data: bytes) -> dict:
    pos = 0
    obj = {}
    while pos < len(data):
        klen = data[pos]
        pos += 1
        key = data[pos:pos + klen].decode("utf-8", errors="replace")
        pos += klen
        if pos >= len(data):
            break
        vtype = data[pos]
        pos += 1
        if vtype == 1:
            if pos + 2 > len(data):
                break
            slen = struct.unpack(">H", data[pos:pos + 2])[0]
            pos += 2
            val = data[pos:pos + slen].decode("utf-8", errors="replace")
            pos += slen
        elif vtype == 4:
            if pos + 4 > len(data):
                break
            val = struct.unpack(">i", data[pos:pos + 4])[0]
            pos += 4
        elif vtype == 7:
            if pos + 2 > len(data):
                break
            val = struct.unpack(">h", data[pos:pos + 2])[0]
            pos += 2
        elif vtype == 2:
            if pos >= len(data):
                break
            val = data[pos]
            pos += 1
        else:
            break
        obj[key] = val
    return obj

async def handle_game_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    global _conn_counter
    _conn_counter += 1
    conn_id = _conn_counter
    addr = writer.get_extra_info("peername")

    session_dir = CAPTURE_DIR / f"{datetime.now():%Y%m%d_%H%M%S}_conn{conn_id:03d}"
    session_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"[TCP #{conn_id}] Client kết nối từ: {addr}")

    seq = 0
    try:
        while True:
            data = await asyncio.wait_for(reader.read(65536), timeout=300.0)
            if not data:
                break
            seq += 1

            # 1. Bắt tay Handshake (cmd == 0x63, 'c')
            if len(data) >= 3 and data[0] == 0x63:
                s2c_resp = b"\x63" + struct.pack(">H", len(SESSION_KEY)) + SESSION_KEY
                writer.write(s2c_resp)
                await writer.drain()
                logger.info(f"[TCP #{conn_id}] Handshake hoàn tất (0x63)!")
                
                # PUSH session packet immediately after handshake
                session_push = {
                    "cmd": "session",
                    "session": "mock_offline_session_12345",
                    "sid": "mock_offline_session_12345",
                    "sessionId": "mock_offline_session_12345"
                }
                ser_push = serialize_map(session_push)
                enc_push = xor_crypt(ser_push, SESSION_KEY)
                # cmd for push is usually 0x01 (or maybe it doesn't matter for routing, it uses "cmd" field)
                # Wait, the client's FBClient_onMessage reads byte [0] as the command type!
                writer.write(bytes([0x01]) + struct.pack(">H", len(enc_push)) + enc_push)
                await writer.drain()
                logger.info(f"[TCP #{conn_id}] PUSHED session packet to client")
                
                continue

            # 2. Xử lý gói tin Game Logic
            if len(data) >= 3:
                cmd = data[0]
                body_len = struct.unpack(">H", data[1:3])[0]
                body_raw = data[3:3 + body_len]
                decrypted = xor_crypt(body_raw, SESSION_KEY)
                req_map = parse_map(decrypted)
                req_cmd = req_map.get("cmd", "")
                logger.info(f"[TCP #{conn_id}] REQ: cmd={cmd:#04x} | req_cmd='{req_cmd}' | map={req_map}")

                gdata = load_game_data()
                u = gdata["user"]
                s = gdata["session"]
                uid = int(u.get("uid", 10001))
                assigned_hero = 2

                if req_cmd == "register":
                    resp_map = {
                        "cmd": req_cmd,
                        "error": 0,
                        "hasRole": 1,
                        "isNew": 0,
                        "loginType": 1,
                        "uid": uid,
                        "userId": uid,
                        "roleName": str(u.get("name", "Anh Hoàng Đẹp Trai"))
                    }
                    ser_resp = serialize_map(resp_map)
                    enc_resp = xor_crypt(ser_resp, SESSION_KEY)
                    writer.write(bytes([cmd]) + struct.pack(">H", len(enc_resp)) + enc_resp)
                    await writer.drain()
                    logger.info(f"[TCP #{conn_id}] RESP: Gửi phản hồi thành công cho '{req_cmd}'")
                    
                    await asyncio.sleep(0.5)
                    # PUSH loginGame as a FLAT map with 'sid' to trigger MessageEvent.DATA
                    push_map = {
                        "cmd": "loginGame",
                        "sid": "mock_offline_session_12345",
                        "session": "mock_offline_session_12345",
                        "stt": 1,
                        "status": 1,
                        "result": 1,
                        "error": 0,
                        "code": 0,
                        "userId": uid,
                        "accid": uid,
                        "username": "Anh Hoàng Đẹp Trai",
                        "userName": "Anh Hoàng Đẹp Trai",
                        "user_name": "Anh Hoàng Đẹp Trai",
                        "name": "Anh Hoàng Đẹp Trai",
                        "roleName": "Anh Hoàng Đẹp Trai",
                        "userLv": 1,
                        "level": 1,
                        "id": 1,
                        "serverId": 1,
                        "server_id": 1,
                        "heroId": 2,
                        "hid": 2,
                        "hasRole": 1,
                        "isNew": 0,
                        "vip": 10,
                        "health": 100,
                        "loginType": 1,
                        "ip": "127.0.0.1",
                        "host": "127.0.0.1",
                        "port": 8888,
                        "serverPort": 8888,
                        "serverAddress": "127.0.0.1:8888"
                    }
                    ser_push = serialize_map(push_map)
                    enc_push = xor_crypt(ser_push, SESSION_KEY)
                    writer.write(bytes([0x03]) + struct.pack(">H", len(enc_push)) + enc_push)
                    await writer.drain()
                    logger.info(f"[TCP #{conn_id}] RESP: PUSHED flat 'loginGame'")
                    continue
                else:
                    resp_map = {
                        "cmd": req_cmd,
                        "stt": 1,
                        "status": 1,
                        "result": 1,
                        "error": 0,
                        "code": 0,
                        "data": 1,
                        "uid": uid,
                        "userId": uid,
                        "accid": uid,
                        "name": str(u.get("name", "Anh Hoàng Đẹp Trai")),
                        "username": str(u.get("username", "Anh Hoàng Đẹp Trai")),
                        "level": int(u.get("level", 1)),
                        "userLv": int(u.get("userLv", 1)),
                        "heroId": int(req_map.get('hid')) if int(req_map.get('hid', 0)) > 0 else assigned_hero,
                        "hid": int(req_map.get('hid')) if int(req_map.get('hid', 0)) > 0 else assigned_hero,
                        "serverId": 1,
                        "gold": int(u.get("gold", 9999999)),
                        "coin": int(u.get("coin", 9999999)),
                        "gem": int(u.get("gem", 999999)),
                        "diamond": int(u.get("diamond", 999999)),
                        "vip": int(u.get("vip", 10)),
                        "exp": 0,
                        "energy": int(u.get("energy", 999)),
                        "maxEnergy": int(u.get("maxEnergy", 999)),
                        "stage": 1,
                        "maxStage": 1,
                        "firstLogin": 1,
                        "isNew": 1,
                        "hasRole": 1,
                        "heroes": f"{int(req_map.get('hid')) if int(req_map.get('hid', 0)) > 0 else assigned_hero}:1:0",
                        "items": ""
                    }
                resp_map["sid"] = str(s.get("sid", "10001_offline_sid"))

                ser_resp = serialize_map(resp_map)
                enc_resp = xor_crypt(ser_resp, SESSION_KEY)
                writer.write(bytes([cmd]) + struct.pack(">H", len(enc_resp)) + enc_resp)
                await writer.drain()
                logger.info(f"[TCP #{conn_id}] RESP: Gửi phản hồi thành công cho '{req_cmd}'")

    except Exception as e:
        logger.info(f"[TCP #{conn_id}] Đóng kết nối ({type(e).__name__})")
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass

async def run_tcp_server():
    srv = await asyncio.start_server(handle_game_client, "0.0.0.0", GAME_PORT)
    logger.info(f"TCP Game Server đang lắng nghe trên 0.0.0.0:{GAME_PORT}")
    async with srv:
        await srv.serve_forever()

async def main():
    CAPTURE_DIR.mkdir(exist_ok=True)
    config = uvicorn.Config(app, host="0.0.0.0", port=HTTP_PORT, log_level="warning", log_config=None)
    http_server = uvicorn.Server(config)
    logger.info(f"Starting LMHB Dual Server v3.9.7 (HTTP: {HTTP_PORT}, TCP: {GAME_PORT})...")
    await asyncio.gather(http_server.serve(), run_tcp_server())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Đã dừng server.")