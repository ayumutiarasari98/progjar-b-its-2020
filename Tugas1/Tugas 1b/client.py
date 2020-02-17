import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    file_name ="pic.jpg"
    print(f"sending request")
    sock.sendall(file_name.encode())
    while True:
        data = sock.recv(500)
        filenew = open('new' + file_name, 'a+b')
        if not data:
            filenew.close()
            break
        filenew.write(data)

finally:
    print ('closing socket')
    sock.close()