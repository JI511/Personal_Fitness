# ----------------------------------------------------------------------------------------------------------------------
#    Nutrition test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
from unittest import mock

from src.Procedures import nutrition
from src.Util import database_api as db_api
from src.Util import constants


class TestNutrition(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'test_table'
        self.query = constants.nutrition_query
        self.names = ["protein", "fat", "carbohydrates", "calories", "water"]

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    def test_add_new_data_nominal(self):
        """
        Adds a new entry into the nutrition table.
        """
        db_api.create_table(self.db_path, self.table, self.query)
        with mock.patch('builtins.input', return_value='1 2 3 4'):
            result = nutrition.add_new_data()
            self.assertEqual(result, [1, 2, 3, 4, 34])
            unique_id = db_api.add_new_row(self.db_path, self.table)
            result.append(unique_id)
            db_api.update_item(self.db_path, self.table, tuple(result), self.names)
            self.assertTrue(os.path.exists(self.db_path))


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
