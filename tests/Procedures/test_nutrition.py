# ----------------------------------------------------------------------------------------------------------------------
#    Nutrition test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
import datetime
from src.Procedures import nutrition
from src.Util import database_api as db_api


class TestNutrition(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = nutrition.NutritionProcedure(self.logs_dir)
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        nutrition.input = mock_input
        db_api.create_table(self.connection, self.procedure.table, self.procedure.query)

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # get_new_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_new_data_nominal(self):
        """
        Adds a new entry into the nutrition table.
        """
        self.input_values = ['1 2 3 4']
        result, name = self.procedure.get_new_data()
        # calories value calculated from provided input
        self.assertEqual(result, [1, 2, 3, 4, 34])
        self.assertEqual(name, ['protein', 'fat', 'carbs', 'calories', 'water'])

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates separate plots for all nutrition items
        """
        self.input_values = ['5 5 5 5']
        result, name = self.procedure.get_new_data()
        unique_id = db_api.add_new_row(self.connection, self.procedure.table)
        result.append(unique_id)
        db_api.update_item(self.connection, self.procedure.table, tuple(result), name)
        self.input_values = ['10 10 10 10']
        result, name = self.procedure.get_new_data()
        unique_id = db_api.add_new_row(self.connection, self.procedure.table)
        result.append(unique_id)
        db_api.update_item(self.connection, self.procedure.table, tuple(result), name)
        self.procedure.view_data(self.connection)
        date_item = datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein_%s.png' % date_item)))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat_%s.png' % date_item)))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs_%s.png' % date_item)))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories_%s.png' % date_item)))
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water_%s.png' % date_item)))

    def test_view_data_not_all_columns(self):
        """
        Creates a plot for only one nutrition item. The others should not be created.
        """
        self.input_values = ['5 5 5 5']
        result, name = self.procedure.get_new_data()
        unique_id = db_api.add_new_row(self.connection, self.procedure.table)
        result.append(unique_id)
        db_api.update_item(self.connection, self.procedure.table, tuple(result), name)
        self.input_values = ['10 10 10 10']
        result, name = self.procedure.get_new_data()
        unique_id = db_api.add_new_row(self.connection, self.procedure.table)
        result.append(unique_id)
        db_api.update_item(self.connection, self.procedure.table, tuple(result), name)
        self.procedure.view_data(self.connection, column_names=['protein'])
        date_item = datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water_%s.png' % date_item)))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
