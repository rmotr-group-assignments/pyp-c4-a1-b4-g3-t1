class Table:
    def __init__(self, columns):
        self.columns = columns
        self.map = {col: {} for col in columns}

    def __key_exists(self, column_id, key):
        return key in self.map[self.columns[column_id]]

    def __insert_new_key(self, column_id, key, val):
        self.map[self.columns[column_id]][key] = [val]

    def __append_to_key(self, column_id, key, val):
        self.map[self.columns[column_id]][key].append(val)

    def insert(self, *args):
        for i in range(len(args)):
            if self.__key_exists(i, args[i]):
                self.__append_to_key(i, args[i], args)
            else:
                self.__insert_new_key(i, args[i], args)

    def query(self, **kwargs):
        pass
