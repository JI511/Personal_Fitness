# ----------------------------------------------------------------------------------------------------------------------
#    Utilities test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
import datetime

from src.Util import database_api as db_api
from src.Util import utilities as util


class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(db_path=os.path.join(self.logs_dir, 'test_database.db'))
        self.table = 'test_table'
        self.query = ("ID integer PRIMARY KEY ASC NOT NULL,"
                      "date text,"
                      "item integer")
        db_api.create_table(connection=self.connection,
                            table=self.table,
                            query=self.query)
        for _ in range(1, 10):
            unique_id = db_api.add_new_row(connection=self.connection,
                                           table=self.table)
            db_api.update_item(connection=self.connection,
                               table=self.table,
                               value_tuple=(100, unique_id),
                               column_names=['item'])

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # function tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_plot_data_nominal(self):
        column_dict = db_api.get_table_columns_dict(connection=self.connection,
                                                    table=self.table,
                                                    column_names=['item'])
        util.plot_data(table=self.table,
                       column_dict=column_dict,
                       output_path=self.logs_dir)
        date = datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'test_table_item_%s.png' % date)))

    def test_read_file_values_nominal(self):
        self.assertTrue(True)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
