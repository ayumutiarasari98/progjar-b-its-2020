import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8282)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

file_name = 'chocolate.png'
print(f"sending request")
request = (b'download '+file_name.encode())


f = open(file_name,'wb')
file = (b'')
sock.send(request)
data = sock.recv(1024)

while True:
    file = file + data
    print(data)
    if sys.getsizeof(data) != 1057:
        break
    else:
        data = sock.recv(1024)

file = base64.decodebytes(file)
f.write(file)
f.close()


print('Your file successfully downloaded')
sock.close()