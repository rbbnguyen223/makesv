# ==============================================================================
# Project: Offline Local Mock Server for LMHB (lmah.vn)
# Version: 3.7.0 - Safe Socket Hold & Clean UTF-8 Master
# ==============================================================================

import asyncio
import logging
import struct
import zlib
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("LMHB_Server")

app = FastAPI(title="LMHB Server v3.7.0", version="3.7.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOCAL_IP  = "192.168.1.13"
HTTP_PORT = 80
GAME_PORT = 8888

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

SERVER_ITEM = {
    "id": 1,
    "serverId": 1,
    "server_id": 1,
    "serverName": "Ca Cao",
    "server_name": "Ca Cao",
    "name": "Ca Cao",
    "ip": LOCAL_IP,
    "host": LOCAL_IP,
    "port": GAME_PORT,
    "stt": 1,
    "status": 1,
    "state": 1,
    "stt_lb": "Hot",
    "live": 1,
    "updated": 1,
    "health": 100,
    "userLv": 1,
    "session": "mock_offline_session_12345",
    "include": 1,
    "pass": "",
    "isOverride": 0,
    "language": "VN"
}

ACCOUNT_ITEM = {
    "userId": "10001",
    "accid": "10001",
    "username": "Ca Cao",
    "user_name": "Ca Cao",
    "user_name_lb": "Ca Cao",
    "name": "Ca Cao",
    "userLv": 1,
    "level": 1,
    "serverId": 1,
    "server_id": 1,
    "heroId": 1,
    "session": "mock_offline_session_12345",
    "pass": "",
    "loginType": 0,
    "serverAddress": f"{LOCAL_IP}:{GAME_PORT}"
}

# ==============================================================================
# 1. CDN Assets Fallback
# ==============================================================================

@app.get("/cdn/{rest_of_path:path}")
async def serve_cdn(request: Request, rest_of_path: str):
    filename = rest_of_path.split("/")[-1]
    logger.info(f"[CDN 512 OK] {filename} -> 200 OK")
    return Response(content=SAFE_512_PNG, media_type="image/png", status_code=200)

# ==============================================================================
# 2. Zing ZCE & Authentication Routes
# ==============================================================================

@app.post("/apps/mobile/android")
@app.get("/apps/mobile/android")
@app.post("/id/mobile/android")
@app.get("/id/mobile/android")
@app.post("/sdk/mobile/android")
@app.get("/sdk/mobile/android")
@app.post("/oauth/mobile/android")
@app.get("/oauth/mobile/android")
async def handle_zce(request: Request):
    logger.info(f"[ZCE] {request.url.path}")
    return JSONResponse(content={
        "return_code": 1,
        "code": 1,
        "status": 1,
        "ErrorCode": 0,
        "error": 0,
        "message": "success",
        "data": {
            "session": "mock_offline_session_token",
            "access_token": "mock_access_token_12345",
            "uid": "10001",
            "zce_status": 1,
            "status": 1,
            "result": 1
        }
    })

@app.post("/mzt/h")
@app.get("/mzt/h")
async def handle_mzt(request: Request):
    return JSONResponse(content={
        "error": 0,
        "code": 0,
        "status": 1,
        "ErrorCode": 0,
        "Message": "success",
        "data": {
            "session": "mock_offline_session_token",
            "uid": "10001",
            "mzt": "mock_mzt_token_12345"
        }
    })

# ==============================================================================
# 3. Game Gateway
# ==============================================================================

@app.api_route("/lmadmin/gateway2.php", methods=["GET", "POST"])
async def handle_gateway2(request: Request):
    params = dict(request.query_params)
    func = params.get("func", "")
    version = params.get("version", "2.1.1")
    snsid = params.get("snsid", "10001")
    server_id = int(params.get("serverId", 1))
    logger.info(f"[Gateway] func={func} | params={params}")

    if func == "listS":
        return JSONResponse(content={
            "Transactions": [],
            "ErrorCode": 0,
            "Message": "success",
            "accid": "10001",
            "lastServerId": 1,
            "servers": [SERVER_ITEM],
            "accounts": {"1": ACCOUNT_ITEM},
            "sessionId": "mock_offline_session_12345",
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
            "accid": "10001",
            "sessionId": "mock_offline_session_12345",
            "userId": "10001",
            "serverId": server_id,
            "ip": LOCAL_IP,
            "host": LOCAL_IP,
            "port": GAME_PORT,
            "data": {
                "userId": "10001",
                "sessionId": "mock_offline_session_12345",
                "ip": LOCAL_IP,
                "host": LOCAL_IP,
                "port": GAME_PORT
            }
        })

    if func == "getServerConstant":
        return JSONResponse(content={
            "ErrorCode": 0,
            "Message": "success",
            "status": 1,
            "data": {
                "VERSION": "2.1.1",
                "needUpdate": 0,
                "forceUpdate": 0,
                "SHOW_EVENT": 0,
                "SHOW_BANNER": 0
            }
        })

    if func == "mapping":
        return JSONResponse(content={
            "ErrorCode": 0,
            "Message": "success",
            "accid": "10001",
            "snsid": snsid
        })

    return JSONResponse(content={"ErrorCode": 0, "status": 1, "code": 0, "Message": "success"})

@app.api_route("/admin/getConstance.php", methods=["GET", "POST"])
async def get_constance(request: Request):
    return JSONResponse(content={
        "ErrorCode": 0,
        "Message": "success",
        "status": 1,
        "data": {
            "VERSION": "2.1.1",
            "needUpdate": 0,
            "forceUpdate": 0,
            "SHOW_EVENT": 0,
            "SHOW_BANNER": 0
        }
    })

@app.api_route("/lmadmin/cluster/{path:path}", methods=["GET", "POST"])
async def handle_cluster(request: Request, path: str = ""):
    return JSONResponse(content={
        "ErrorCode": 0,
        "status": 1,
        "Message": "success",
        "host": LOCAL_IP,
        "ip": LOCAL_IP,
        "port": GAME_PORT,
        "data": {"host": LOCAL_IP, "ip": LOCAL_IP, "port": GAME_PORT}
    })

@app.api_route("/server/sdk_config_v2.php", methods=["GET", "POST"])
@app.api_route("/client_v2/{path:path}", methods=["GET", "POST"])
async def sdk_config(request: Request):
    return JSONResponse(content={
        "status": 1,
        "code": 1,
        "ErrorCode": 0,
        "data": {
            "login_url": f"http://{LOCAL_IP}/login",
            "pay_url": f"http://{LOCAL_IP}/pay",
            "enable_guest": 1,
            "enable_login": 1
        }
    })

@app.api_route("/me/{path:path}", methods=["GET", "POST"])
@app.api_route("/graphapi/{path:path}", methods=["GET", "POST"])
async def zing_graph(request: Request):
    return JSONResponse(content={
        "error": 0,
        "ErrorCode": 0,
        "message": "success",
        "data": {
            "userId": "10001",
            "userName": "Ca Cao",
            "displayName": "Ca Cao",
            "sessionKey": "fake_offline_session_key_12345",
            "uid": "10001"
        }
    })

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(request: Request, full_path: str):
    return JSONResponse(content={
        "status": 1,
        "code": 200,
        "ErrorCode": 0,
        "Message": "success",
        "data": {"result": 1, "status": 1}
    })

# ==============================================================================
# 4. TCP Game Socket Server (Keep-alive an toàn, không bắn byte rác)
# ==============================================================================

async def handle_game_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    logger.info(f"[TCP Socket] Client kết nối: {addr}")
    try:
        while True:
            data = await asyncio.wait_for(reader.read(4096), timeout=120.0)
            if not data:
                break
            logger.info(f"[TCP Socket] Client gửi {len(data)}B: {data.hex()[:80]}")
            # Duy trì kết nối TCP mở, chờ đúng gói tin request từ client
    except Exception as e:
        logger.info(f"[TCP Socket State] {addr}: {e}")
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass
        logger.info(f"[TCP Socket] Đóng kết nối: {addr}")

async def run_tcp_server():
    srv = await asyncio.start_server(handle_game_client, "0.0.0.0", GAME_PORT)
    logger.info(f"TCP Game Socket Server đang lắng nghe trên 0.0.0.0:{GAME_PORT}...")
    async with srv:
        await srv.serve_forever()

# ==============================================================================
# Main
# ==============================================================================

async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=HTTP_PORT, log_level="warning")
    http_server = uvicorn.Server(config)
    logger.info(f"Starting LMHB Dual Server v3.7.0 (HTTP: {HTTP_PORT}, TCP: {GAME_PORT})...")
    await asyncio.gather(http_server.serve(), run_tcp_server())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Đã dừng server.")