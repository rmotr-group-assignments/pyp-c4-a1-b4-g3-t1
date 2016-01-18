import pyp_database.table as table

class Database:
    def create_table(self, name, columns):
        return table.Table([])

# test code to make sure imports are working
testtable = table.Table([])
