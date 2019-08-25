# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
from unittest import mock

from src.Util import constants
from src.Util import database_api as db_api
from src.Procedures import body_weight


class TestBodyWeight(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'body_weight'
        self.query = constants.body_weight_query
        self.names = ["body_weight"]
        db_api.create_table(self.db_path, self.table, self.query)

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # add_new_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_add_new_data_nominal(self):
        """
        Provides mock user input for a body weight entry.
        """
        with mock.patch('builtins.input', return_value='100'):
            result = body_weight.add_new_data()
            self.assertEqual(result, [100])
            unique_id = db_api.add_new_row(self.db_path, self.table)
            result.append(unique_id)
            db_api.update_item(self.db_path, self.table, tuple(result), self.names)
            self.assertTrue(os.path.exists(self.db_path))

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates a plot from body weight entries.
        """
        for _ in range(1,10):
            unique_id = db_api.add_new_row(self.db_path, self.table)
            db_api.update_item(self.db_path, self.table, (100, unique_id), ['body_weight'])
        body_weight.view_data(self.db_path, self.logs_dir)
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'body_weight_body_weight.png')))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
