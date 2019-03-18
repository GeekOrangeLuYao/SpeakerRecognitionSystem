from Handler.ModelHandler import ModelHandler
import os
from Utils import config
import uuid



class MainHandler:
    def __init__(self, socket):
        self.socket = socket
        self.model = ModelHandler()
        self.file_handler = FileHandler(socket)
        self.text_handler = TextHandler(socket)

    def run(self):

        pass

    def register(self):
        # get student info
        # get register audio


        pass

    def verify(self):
        # get verify audio
        # use model to get a result

        pass

"""
    TextHandler is used to deal with the 
"""


class TextHandler:
    buffer_size = 1024
    def __init__(self, socket):
        self.socket = socket

"""
    FileHandler is used to deal with the file:
        * receive file by socket
        * save the file and manager them
"""
class FileHandler:
    buffer_size = 1024
    def __init__(self, socket):
        self.socket = socket

    def receiveFile(self , fileInfo):
        # studentName
        studentName = fileInfo['studentName']
        # Size is used to receive the file
        fileSize = fileInfo['fileSize']

        # construct ab absolute_address to save the audio
        absolute_address = config.get_Audio_audio_address() + '\\' + studentName + '_' + uuid.uuid1() + '.wav'

        # check the file is existed
        if os.path.isfile(absolute_address):
            fw = None
        else:
            fw = open(absolute_address, 'wb')
            self.socket.send(b'ready')

        if fw is not None:
            try:
                receive_size = 0
                while receive_size < fileSize:
                    # TO-DO
                    data = self.socket.recv(FileHandler.buffer_size)
                    fw.write(data)
                    receive_size += FileHandler.buffer_size

                fw.flush()
                self.socket.send(b'receive file success')
            except Exception as e:
                print(e)
                self.socket.send(b'receive file error')

        return absolute_address