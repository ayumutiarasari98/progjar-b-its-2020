import socket
import sys
from time import sleep
import base64
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8282)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

message = (b"list")

sock.send(message)
print("Request delivered")

data = sock.recv(1024)
print("List : \n"+data.decode())
sock.close()