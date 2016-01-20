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

    def __get(self, col_name, col_val):
        return self.map[col_name][col_val]

    def insert(self, *args):
        for i in range(len(args)):
            if self.__key_exists(i, args[i]):
                self.__append_to_key(i, args[i], args)
            else:
                self.__insert_new_key(i, args[i], args)

    def query(self, **kwargs):
        column_ids = [self.columns.index(key) for key in kwargs.keys()[1:]]
        init_col_name, init_col_val = kwargs.items()[0]
        qry = self.__get(init_col_name, init_col_val)

        # filter out the query based on the rest of the kwargs
        filter_kwargs = kwargs.items()[1:]
        for col_name, col_val in filter_kwargs:
            col_id = self.columns.index(col_name)
            qry = [e for e in qry if e[col_id] == col_val]
        return qry


        
