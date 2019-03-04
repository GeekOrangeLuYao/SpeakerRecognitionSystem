import configparser

file_path = "..\\setting.ini"

conf = configparser.ConfigParser()
conf.read(file_path)


def get_Server_host():
    return conf.get("server", "server_port")


def get_Server_port():
    return int(conf.get('server', 'server_port'))


if __name__ == '__main__':
    print(get_Server_port())
