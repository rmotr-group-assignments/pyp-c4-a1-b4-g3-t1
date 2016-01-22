from datetime import date
import pyp_database.table
import unittest

class TestDatabaseTables(unittest.TestCase):
    def test_insert_and_query(self):
        test_table = pyp_database.table.Table(['id', 'name', 'dob'])
        test_table.insert(1, 'Kevin Bacon', date(1958, 7, 8))
        self.assertEquals(len(test_table.query(name='Kevin Bacon')), 1)
        test_table.insert(2, 'Kevin Bacon', date(1995, 5, 5))
        self.assertEquals(len(test_table.query(name='Kevin Bacon')), 2)
        self.assertEquals(len(test_table.query(name='Kevin Bacon', id=1)), 1)
