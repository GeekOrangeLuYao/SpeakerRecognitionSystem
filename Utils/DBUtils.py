from Utils.DBManager import SimpleDBManager

db_names = {
    "simple" : SimpleDBManager
}

def getDBManager(db_name):
    if db_name not in db_names.keys():
        raise ValueError("DB not existed")
    else:
        for db in db_names.keys():
            if db == db_name:
                return db_names.get(db)()

