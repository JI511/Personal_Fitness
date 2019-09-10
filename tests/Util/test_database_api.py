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

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # create_connection tests
    # ------------------------------------------------------------------------------------------------------------------
    def create_connection_nominal(self):
        """
        A standard database connection shall be created when provided a valid path.
        """
        connection = db_api.create_connection(connection=self.db_path)
        self.assertTrue(connection is not None)

    def create_connection_bad_path(self):
        """
        A return of None shall occur when a bad path is given.
        """
        connection = db_api.create_connection(connection=self.logs_dir)
        self.assertTrue(connection is None)

    # ------------------------------------------------------------------------------------------------------------------
    # create_table tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_create_table_nominal(self):
        """
        Creates a test database with nominal values.
        """
        db_api.create_table(connection=db_api.create_connection(db_path=self.db_path),
                            table=self.table,
                            query=self.query)
        tables = db_api.get_table_names(connection=db_api.create_connection(db_path=self.db_path))
        self.assertTrue(self.table in tables)

    def test_create_table_bad_path(self):
        """
        Tries to create a test database with invalid path.
        """
        db_api.create_table(connection=self.logs_dir,
                            table=self.table,
                            query=self.query)
        tables = db_api.get_table_names(connection=db_api.create_connection(db_path=self.db_path))
        self.assertFalse(self.table in tables)

    def test_create_table_no_date_query(self):
        """
        Tries to create a test database without the required column name date.
        """
        self.query = "ID integer PRIMARY KEY ASC NOT NULL"
        db_api.create_table(connection=db_api.create_connection(db_path=self.db_path),
                            table=self.table,
                            query=self.query)
        tables = db_api.get_table_names(connection=db_api.create_connection(db_path=self.db_path))
        self.assertFalse(self.table in tables)

    def test_create_table_no_id_query(self):
        """
        Tries to create a test database without the required column name ID.
        """
        self.query = "date text"
        db_api.create_table(connection=self.db_path,
                            table=self.table,
                            query=self.query)
        tables = db_api.get_table_names(connection=db_api.create_connection(db_path=self.db_path))
        self.assertFalse(self.table in tables)

    def test_create_table_already_exists(self):
        """
        Tries to create a table that already exists.
        """
        db_api.create_table(connection=db_api.create_connection(db_path=self.db_path),
                            table=self.table,
                            query=self.query)
        db_api.create_table(connection=db_api.create_connection(db_path=self.db_path),
                            table=self.table,
                            query=self.query)
        self.assertTrue(os.path.exists(self.db_path))

    # ------------------------------------------------------------------------------------------------------------------
    # add_new_row tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_add_new_row_nominal(self):
        """
        Creates a default row.
        """
        connection = db_api.create_connection(db_path=self.db_path)
        db_api.create_table(connection=connection,
                            table=self.table,
                            query=self.query)
        unique_id = db_api.add_new_row(connection=connection,
                                       table=self.table)
        result = db_api.get_all_table_entries(connection=connection,
                                              table=self.table)
        self.assertEqual(unique_id, 1)
        self.assertEqual(result[0][0], 1)

    # ------------------------------------------------------------------------------------------------------------------
    # update_item tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_update_item_nominal(self):
        """
        Updates database file at the specified column and table.
        """
        connection = db_api.create_connection(db_path=self.db_path)
        db_api.create_table(connection=connection,
                            table=self.table,
                            query=self.query)
        unique_id = db_api.add_new_row(connection=connection,
                                       table=self.table)
        db_api.update_item(connection=connection,
                           table=self.table,
                           value_tuple=('a', 5, unique_id),
                           column_names=['text_item', 'number_item'])
        result = db_api.get_all_table_entries(connection=connection,
                                              table=self.table)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][2], 'a')
        self.assertEqual(result[0][3], 5)

    # ------------------------------------------------------------------------------------------------------------------
    # get_all_table_items tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_all_table_items_nominal(self):
        """
        Gets all entries within the specified table.
        """
        connection = db_api.create_connection(db_path=self.db_path)
        db_api.create_table(connection=connection,
                            table=self.table,
                            query=self.query)
        unique_id = db_api.add_new_row(connection=connection,
                                       table=self.table)
        unique_id_2 = db_api.add_new_row(connection=connection,
                                         table=self.table)
        db_api.update_item(connection=connection,
                           table=self.table,
                           value_tuple=('a', 5, unique_id),
                           column_names=['text_item', 'number_item'])
        db_api.update_item(connection=connection,
                           table=self.table,
                           value_tuple=('b', 10, unique_id_2),
                           column_names=['text_item', 'number_item'])
        result = db_api.get_all_table_entries(connection=connection,
                                              table=self.table)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[1][0], 2)
        self.assertEqual(result[1][3], 10)
        self.assertEqual(result[1][2], 'b')

    # ------------------------------------------------------------------------------------------------------------------
    # table_to_csv tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_table_columns_nominal(self):
        """
        Gets the entries as a dictionary at the specified columns.
        """
        connection = db_api.create_connection(db_path=self.db_path)
        db_api.create_table(connection=connection,
                            table=self.table,
                            query=self.query)
        unique_id = db_api.add_new_row(connection=connection,
                                       table=self.table)
        db_api.update_item(connection=connection,
                           table=self.table,
                           value_tuple=('a', 5, unique_id),
                           column_names=['text_item', 'number_item'])
        result = db_api.get_table_columns_dict(connection=connection,
                                               table=self.table,
                                               column_names=['text_item', 'number_item'])
        self.assertEqual(result['text_item'][0], 'a')
        self.assertEqual(result['number_item'][0], 5)

    # ------------------------------------------------------------------------------------------------------------------
    # update_item tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_table_to_csv(self):
        """
        Outputs all of the specified table to a csv file.
        """
        connection = db_api.create_connection(db_path=self.db_path)
        db_api.create_table(connection=connection,
                            table=self.table,
                            query=self.query)
        unique_id = db_api.add_new_row(connection=connection,
                                       table=self.table)
        db_api.update_item(connection=connection,
                           table=self.table,
                           value_tuple=('a', 5, unique_id),
                           column_names=['text_item', 'number_item'])
        name = db_api.table_to_csv(connection=connection,
                                   table=self.table,
                                   output_dir=self.logs_dir)
        self.assertTrue(os.path.exists(name))
        self.assertEqual(os.path.join(self.logs_dir, '%s.csv' % self.table), name)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
