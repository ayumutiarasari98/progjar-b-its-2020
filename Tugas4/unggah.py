import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8282)
print('connecting to %s port %s' % server_address)

sock.connect(server_address)
message = ("upload coba.txt")
file_name = "".join(message.split()[1])

f = open(file_name, "rb")
length = len(file_name) + 1
file_content = base64.encodebytes(f.read())
f.close()

f = open("base64encode","wb")
f.write(file_content)
f.close

f = open("base64encode","rb")
l = message.encode() + (b" ") + f.read(1024)
print(l)

while (l):
    sock.send(l)
    l =f.read(1024)
    data = sock.recv(1024)
print(data)

sock.close()