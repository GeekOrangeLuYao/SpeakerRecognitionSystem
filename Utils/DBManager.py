"""
    use json file to manager the data:
        1. Student Info
        2. Student Audio
"""
from Utils import config
import json
from Entity.Student import Student
import sqlite3

class SimpleDBManager:
    """
        TO-DO
        Don't use it !!!
    """
    def __init__(self):
        print("SimpleDBManager")
        with open(config.get_SimpleDB_db() , "r") as fr:
            self.json = json.load(fr)


class SqliteManager:
    def __init__(self):
        self.connection = sqlite3.connect(config.get_SqliteDB_db())


    def close(self):
        self.connection.close()



def main():
    manager = SimpleDBManager()



if __name__ == '__main__':
    main()