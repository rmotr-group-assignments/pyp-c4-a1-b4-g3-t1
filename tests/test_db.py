from pyp_database import db
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        self.my_db = db.Database('test-db')

    def test_table_creation(self):
        table1 = 'table1'
        table2 = 'table2'
        self.assertFalse(hasattr(self.my_db, table1))
        self.assertFalse(hasattr(self.my_db, table2))

        self.my_db.create_table(table1, columns=['id', 'age'])
        self.assertTrue(hasattr(self.my_db, table1))
        self.assertFalse(hasattr(self.my_db, table2))

        self.my_db.create_table(table2, columns=['job', 'salary', 'boss'])
        self.assertTrue(hasattr(self.my_db, table1))
        self.assertTrue(hasattr(self.my_db, table2))

if __name__ == '__main__':
    unittest.main()
