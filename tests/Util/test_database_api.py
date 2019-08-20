# ----------------------------------------------------------------------------------------------------------------------
#    Database API tests
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
import inspect
from src.Util import database_api as db_api


class TestDatabaseApi(unittest.TestCase):
    """
    Test cases for database_api.py

    """
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'test_table'
        self.query = (
            "ID integer PRIMARY KEY ASC NOT NULL,"
            "date text,"
            "text_item text,"
            "number_item int"
        )
        print('\n' + str(self.__class__).split(".")[-1][:-2] + '.' + self._testMethodName)

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    def test_create_table_nominal(self):
        """
        Creates a test database with nominal values.
        """
        db_api.create_table(self.db_path, self.table, self.query)
        self.assertTrue(os.path.exists(self.db_path))

    def test_create_table_bad_path(self):
        """
        Tries to create a test database with invalid path.
        """
        db_api.create_table(self.logs_dir, self.table, self.query)
        self.assertFalse(os.path.exists(self.db_path))

    def test_add_new_row_nominal(self):
        db_api.create_table(self.db_path, self.table, self.query)
        unique_id = db_api.add_new_row(self.db_path, self.table)
        self.assertEqual(unique_id, 1)

    # todo add test for date not present


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
