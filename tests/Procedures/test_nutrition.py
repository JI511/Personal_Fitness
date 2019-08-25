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

table = 'weight_lifting'


class TestNutrition(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'nutrition'
        self.query = constants.nutrition_query
        self.names = ["protein", "fat", "carbs", "calories", "water"]
        db_api.create_table(self.db_path, self.table, self.query)

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # get_new_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_new_data_nominal(self):
        """
        Adds a new entry into the nutrition table.
        """
        with mock.patch('builtins.input', return_value='1 2 3 4'):
            result = nutrition.get_new_data()
            self.assertEqual(result, [1, 2, 3, 4, 34])
            unique_id = db_api.add_new_row(self.db_path, self.table)
            result.append(unique_id)
            db_api.update_item(self.db_path, self.table, tuple(result), self.names)
            self.assertTrue(os.path.exists(self.db_path))

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates separate plots for all nutrition items
        """
        unique_id = db_api.add_new_row(self.db_path, self.table)
        macro_values = (5, 5, 5, 5, 5, unique_id)
        db_api.update_item(self.db_path, self.table, macro_values, self.names)
        unique_id = db_api.add_new_row(self.db_path, self.table)
        macro_values = (10, 10, 10, 10, 10, unique_id)
        db_api.update_item(self.db_path, self.table, macro_values, self.names)
        nutrition.view_data(self.db_path, self.logs_dir)
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein.png')))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat.png')))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs.png')))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories.png')))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water.png')))

    def test_view_data_not_all_columns(self):
        """
        Creates a plot for only one nutrition item. The others should not be created.
        """
        unique_id = db_api.add_new_row(self.db_path, self.table)
        macro_values = (5, 5, 5, 5, 5, unique_id)
        db_api.update_item(self.db_path, self.table, macro_values, self.names)
        unique_id = db_api.add_new_row(self.db_path, self.table)
        macro_values = (10, 10, 10, 10, 10, unique_id)
        db_api.update_item(self.db_path, self.table, macro_values, self.names)
        nutrition.view_data(self.db_path, self.logs_dir, column_names=['protein'])
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein.png')))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat.png')))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs.png')))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories.png')))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water.png')))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
