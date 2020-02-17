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
print("Server listening...")
while True:
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print(f"connection from {client_address}")
	receiv = connection.recv(500)
	fileOp = open(receiv.decode(), 'rb')
	data = fileOp.read(500)
	while (data):
		print("sending data to client")
		connection.sendall(data)
		data=fileOp.read(500)
	fileOp.close()

	# Clean up the connection
	print("Done sending")
	connection.close()
