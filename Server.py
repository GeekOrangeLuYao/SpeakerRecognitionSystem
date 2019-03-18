import socketserver
from Handler.Handler import MainHandler


class MainServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                # use MainHandler to fit the front process
                handler = MainHandler(self.request)
                handler.run()

            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    from Utils import config

    ip_port = (config.get_Server_host(), config.get_Server_port())
    print("Start the server!\nThe server is on: ", ip_port)
    s = socketserver.ThreadingTCPServer(ip_port, MainServer)
    s.serve_forever()
