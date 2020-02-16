import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
i=1
while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print(f"connection from {client_address}")
	file_name = open('received_'+ str(i)+ ".jpg", 'wb')
	i=i+1
	# Receive the data in small chunks and retransmit it
	while True:
		data = connection.recv(500)
		print (f"received file from {client_address}")
		while(data):
			file_name.write(data)
			data = connection.recv(500)
		if not data:
			file_name.close()
			break
	# Clean up the connection
	connection.close()
socket.close()
