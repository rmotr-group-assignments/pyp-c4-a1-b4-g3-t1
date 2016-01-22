import pyp_database.table as table

class Database:
    def __init__(self, name):
        self.name = name

    def create_table(self, name, columns):
        setattr(self, name, table.Table(columns))
