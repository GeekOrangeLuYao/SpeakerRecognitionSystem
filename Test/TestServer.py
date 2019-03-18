import socket
from multiprocessing import Process


class MainServer(object):

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, host, port):
        self.server.bind((host, port))

    def start(self):
        self.server.listen(128)

        while True:
            client_socket, client_address = self.server.accept()
            print("用户连接上了: ", client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        pass


