from pyp_database import db_manager
import unittest

class TestDBManager(unittest.TestCase):
    def test_database_creation(self):
        db_name = 'test-db'
        pyp_database.create_database(db_name)
        db = pyp_database.use(db_name)
        self.assertTrue(db.name, '')

if __name__ == '__main__':
    unittest.main()
