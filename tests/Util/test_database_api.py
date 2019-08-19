# ----------------------------------------------------------------------------------------------------------------------
#    Database API tests
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
from src.Util import database_api as db_api


class TestDatabaseApi(unittest.TestCase):
    """
    Test cases for database_api.py

    """
    def setUp(self):
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'test_table'
        self.query = (
            "ID integer PRIMARY KEY ASC NOT NULL,"
            "text_item text,"
            "number_item int"
        )

    def tearDown(self):
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    def test_nominal(self):
        print(os.getcwd())
        db_api.create_table(self.db_path, self.table, self.query)
        self.assertEqual('test', 'test')

    def test_nominal_2(self):
        self.assertTrue(True)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
