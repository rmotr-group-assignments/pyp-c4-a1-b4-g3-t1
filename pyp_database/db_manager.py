import pyp_database.db as db
import os
import pickle

databases = {}

def create_database(name):
    if name in databases:
        err = "Name for new database <{}> already in use".format(name)
        raise ValueError(err)
    databases[name] = db.Database(name)

def use(name):
    if name not in databases:
        err = "No database currently loaded with the name <{}>".format(name)
        raise ValueError(err)
    return databases[name]

def save_database(db_name, file_name):
    pass

def load_database(file_name):
    pass
