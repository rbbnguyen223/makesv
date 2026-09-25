# ==============================================================================
# Project: Offline Local Mock Server for LMHB (lmah.vn)
# Version: 6.2.1 - Chameleon Gateway (Chống văng bằng cấu trúc JSON đa tầng)
# ==============================================================================

import asyncio
import json
import logging
import mimetypes
import struct
import zlib
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

app = FastAPI(title="LMHB Server v6.2.1", version="6.2.1")
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

def generate_safe_png(width=512, height=512) -> bytes:
    raw_data = b"".join(b"\x00" + b"\xFF\xFF\xFF\xFF" * width for _ in range(height))
    compressed = zlib.compress(raw_data)
    def chunk(tag: bytes, data: bytes) -> bytes:
        length = struct.pack(">I", len(data))
        crc = struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        return length + tag + data + crc
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")

SAFE_512_PNG = generate_safe_png(512, 512)

@app.middleware("http")
async def log_all_requests(request: Request, call_next):
    response = await call_next(request)
    if "/cdn/" not in request.url.path:
        logger.info(f"[HTTP] {request.method} {request.url.path} host={request.headers.get('host')} -> {response.status_code}")
    return response

@app.get("/cdn/{rest_of_path:path}")
async def serve_cdn(request: Request, rest_of_path: str):
    filename = rest_of_path.replace("\\", "/").split("/")[-1]
    for d in CDN_DIRS:
        if d.is_dir() and (d / filename).is_file():
            mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            return Response(content=(d / filename).read_bytes(), media_type=mime, status_code=200)
    return Response(content=SAFE_512_PNG, media_type="image/png", status_code=200)

@app.api_route("/apps/mobile/android", methods=["GET", "POST"])
@app.api_route("/id/mobile/android", methods=["GET", "POST"])
@app.api_route("/mzt/h", methods=["GET", "POST"])
async def handle_auth(request: Request):
    return JSONResponse(content={
        "return_code": 1, "code": 1, "status": 1, "error": 0, "ErrorCode": 0, "message": "success",
        "data": {"session": "mock", "access_token": "mock", "uid": "10001", "status": 1}
    })

@app.api_route("/lmadmin/gateway2.php", methods=["GET", "POST"])
async def handle_gateway2(request: Request):
    params = dict(request.query_params)
    func = params.get("func", "")
    version = params.get("version", "2.1.1")
    logger.info(f"[Gateway] func={func} | params={params}")

    role_info = {
        "userId": "10001", "accid": "10001", "id": 1, "roleId": 1,
        "serverId": 1, "server_id": 1, "hasRole": 0, "isNew": 1, 
        "name": "Anh Hoàng Đẹp Trai", "level": 1, "userLv": 1,
        "ip": LOCAL_IP, "port": GAME_PORT,
    }
    
    server_item = {
        "id": 1, "serverId": 1, "server_id": 1,
        "serverName": "S1 - Ca Cao", "name": "S1 - Ca Cao",
        "ip": LOCAL_IP, "port": GAME_PORT, 
        "stt": 1, "status": 1, "state": 1, "stt_lb": "Hot",
        "is_hot": 1, "is_new": 0, "maintenance": 0,
        "hasRole": 0, "accounts": [role_info], "roles": [role_info]
    }

    # Bọc đa tầng các key khả dĩ để client kiểu gì cũng tìm thấy
    mega_payload = {
        "Transactions": [], "ErrorCode": 0, "error": 0, "code": 0, "status": 1, "Message": "success",
        "accid": "10001", "lastServerId": 1,
        "servers": [server_item], "serverList": [server_item], "listServer": [server_item], "zone_list": [server_item],
        "accounts": {"1": role_info}, "accountList": [role_info],
        "roles": [role_info], "characters": [role_info], "roleList": [role_info],
        "lastRole": role_info, "hasRole": 0, "isNew": 1, "heroId": 0, "version": version,
        "res_url": f"http://{LOCAL_IP}/cdn/2.1.1/android/",
        "api_url": f"http://{LOCAL_IP}/lmadmin/gateway2.php",
        "cdn_url": f"http://{LOCAL_IP}/cdn/2.1.1/android/",
        "data": {
            "servers": [server_item], "serverList": [server_item], "hasRole": 0, "isNew": 1,
            "role": role_info, "accounts": [role_info], "roles": [role_info]
        }
    }

    if func == "listS":
        return JSONResponse(content=mega_payload)

    if func == "login":
        mega_payload["role"] = role_info
        return JSONResponse(content=mega_payload)

    if func in ("getServerConstant", "getConstance"):
        return JSONResponse(content={
            "ErrorCode": 0, "error": 0, "Message": "success", "status": 1, 
            "data": {"VERSION": version, "needUpdate": 0, "forceUpdate": 0, "SHOW_EVENT": 0}
        })

    return JSONResponse(content=mega_payload)

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(request: Request, full_path: str):
    return JSONResponse(content={"status": 1, "code": 200, "ErrorCode": 0, "error": 0, "Message": "success", "data": {"result": 1}})

# ==============================================================================
# 4. TCP Game Socket Protocol Engine
# ==============================================================================
SESSION_KEY = b"1234567812345678"

def make_cipher_key(session: bytes) -> bytes:
    sum_b = sum(session) & 0xFF
    return bytes([b ^ sum_b for b in session])

def xor_crypt(data: bytes, session: bytes) -> bytes:
    key = make_cipher_key(session)
    klen = len(key)
    out = bytearray(len(data))
    for i in range(len(data)): out[i] = data[i] ^ ((~key[i % klen]) & 0xFF)
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
    pos = 0; obj = {}
    while pos < len(data):
        klen = data[pos]; pos += 1
        key = data[pos:pos + klen].decode("utf-8", errors="replace"); pos += klen
        if pos >= len(data): break
        vtype = data[pos]; pos += 1
        if vtype == 1:
            slen = struct.unpack(">H", data[pos:pos + 2])[0]; pos += 2
            val = data[pos:pos + slen].decode("utf-8", errors="replace"); pos += slen
        elif vtype == 4:
            val = struct.unpack(">i", data[pos:pos + 4])[0]; pos += 4
        elif vtype == 7:
            val = struct.unpack(">h", data[pos:pos + 2])[0]; pos += 2
        elif vtype == 2:
            val = data[pos]; pos += 1
        else: break
        obj[key] = val
    return obj

async def handle_game_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    logger.info(f"[TCP] Client kết nối từ: {addr}")
    try:
        while True:
            data = await asyncio.wait_for(reader.read(65536), timeout=300.0)
            if not data: break
            if len(data) >= 3 and data[0] == 0x63:
                writer.write(b"\x63" + struct.pack(">H", len(SESSION_KEY)) + SESSION_KEY)
                await writer.drain()
                continue
            if len(data) >= 3:
                cmd = data[0]
                body_len = struct.unpack(">H", data[1:3])[0]
                req_map = parse_map(xor_crypt(data[3:3 + body_len], SESSION_KEY))
                req_cmd = req_map.get("cmd", "")
                logger.info(f"[TCP] REQ: req_cmd='{req_cmd}'")

                role_details = {
                    "roleId": 1, "charId": 1, "id": 1, "uid": 10001, "userId": 10001, 
                    "name": "Anh Hoàng Đẹp Trai", "username": "Anh Hoàng",
                    "level": 1, "heroId": 2, "hid": 2, "serverId": 1, 
                    "gold": 9999999, "diamond": 999999, "vip": 10,
                    "hasRole": 1, "isNew": 0, "heroes": "2:1:0", "items": ""
                }

                resp_payload = {
                    "cmd": req_cmd, "stt": 1, "status": 1, "result": 1,
                    "error": 0, "code": 0, "sid": "10001_offline_sid",
                    **role_details,
                    "role": json.dumps(role_details),
                    "roles": json.dumps([role_details]),
                    "info": json.dumps(role_details)
                }

                ser_resp = serialize_map(resp_payload)
                enc_resp = xor_crypt(ser_resp, SESSION_KEY)
                writer.write(bytes([cmd]) + struct.pack(">H", len(enc_resp)) + enc_resp)
                await writer.drain()

                if req_cmd == "register":
                    for f_cmd in ["createRole", "loginGame", "enterGame"]:
                        await asyncio.sleep(0.5)
                        mock_fuzz = resp_payload.copy()
                        mock_fuzz["cmd"] = f_cmd
                        enc_fuzz = xor_crypt(serialize_map(mock_fuzz), SESSION_KEY)
                        writer.write(bytes([cmd]) + struct.pack(">H", len(enc_fuzz)) + enc_fuzz)
                        await writer.drain()
                        logger.info(f"[TCP] 💣 Fuzzing: Đã bắn bồi '{f_cmd}'")

    except Exception:
        pass
    finally:
        writer.close()

async def run_tcp_server():
    srv = await asyncio.start_server(handle_game_client, "0.0.0.0", GAME_PORT)
    async with srv: await srv.serve_forever()

async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=HTTP_PORT, log_level="warning")
    await asyncio.gather(uvicorn.Server(config).serve(), run_tcp_server())

if __name__ == "__main__":
    asyncio.run(main())