
import socket

TARGET_IP = "192.168.100.5"
TARGET_PORT = 5006

nama="Informatika"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(nama.encode()),(TARGET_IP,TARGET_PORT))