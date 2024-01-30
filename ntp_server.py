import socket
import struct
import time

# NTP 서버 정보
NTP_SERVER = 'time.bora.net'
NTP_PORT = 123

# Unix 도메인 소켓 경로
SOCKET_PATH = '/tmp/ntp_proxy.sock'

# NTP 패킷 포맷
NTP_PACKET_FORMAT = "!12I"

def get_ntp_time():
    # Unix 도메인 소켓을 통해 NTP 요청 전송
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(SOCKET_PATH)
        sock.sendall(b'Request NTP time')
        response = sock.recv(1024)

    # 받은 NTP 패킷 해석
    unpacked = struct.unpack(NTP_PACKET_FORMAT, response)
