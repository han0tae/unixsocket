import socket
import struct
import sys
import time

# Unix 도메인 소켓 경로
SOCKET_PATH = '/tmp/ntp_proxy.sock'

# NTP 패킷 포맷
NTP_PACKET_FORMAT = "!12I"

def get_ntp_time_from_proxy():
    # Unix 도메인 소켓을 통해 NTP 요청 전송
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(SOCKET_PATH)
        sock.sendall(b'Request NTP time')
        response = sock.recv(1024)

    # 받은 NTP 패킷 해석
    unpacked = struct.unpack(NTP_PACKET_FORMAT, response)
    # 첫 번째 워드는 1900년 1월 1일부터의 초
    seconds_since_1900 = unpacked[10]
    # 1970년 1월 1일부터의 초로 변환
