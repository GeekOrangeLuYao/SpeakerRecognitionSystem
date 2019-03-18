import configparser
import sys

sys.path.append("..")

file_path = "..\\setting.ini"

conf = configparser.ConfigParser()
conf.read(file_path)


def get_Server_host():
    return conf.get("server", "server_host")


def get_Server_port():
    return int(conf.get('server', 'server_port'))


def get_SimpleDB_db():
    return conf.get('SimpleDB', 'db')


def get_SqliteDB_db():
    return conf.get('SqliteDB', 'db')


def get_Audio_audio_address():
    return conf.get('Audio', 'audio_address')


if __name__ == '__main__':
    print(get_SimpleDB_db())
    print(get_Server_port())
    print(get_SqliteDB_db())
