from socket import *
import socket
import threading
import logging
import time
import sys
from protokol import Protocol

pr = Protocol()
class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b'')
        arr = []
        while True:
            while True:
                data = self.connection.recv(32)
                file = file + data
                arr.append(data)
                bit = int(sys.getsizeof(data))

                if bit != 1057:
                    print(bit)
                    break
                else:
                    print(bit)
                    self.connection.sendall(b'halo')
            data = file
            if data:
                d = data.decode()
                result = pr.process(d)
                result = result
                self.connection.sendall(result.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('localhost', 8282))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

