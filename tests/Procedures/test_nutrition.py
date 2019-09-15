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
from src.Util.constants import Constants


class TestNutrition(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(db_path=os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = nutrition.NutritionProcedure(output_dir=self.logs_dir)
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        nutrition.input = mock_input
        db_api.create_table(connection=self.connection,
                            table=self.procedure.table,
                            query=self.procedure.query)
        for _ in range(1, 10):
            unique_id = db_api.add_new_row(connection=self.connection,
                                           table=self.procedure.table)
            db_api.update_item(connection=self.connection,
                               table=self.procedure.table,
                               value_tuple=(1, 2, 3, 4, 5, unique_id),
                               column_names=[a[0] for a in Constants.nutrition_query_tuple])

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
        result, name = self.procedure.get_new_data(connection=self.connection)
        # calories value calculated from provided input
        self.assertEqual(result, [1, 2, 3, 4, 34])
        self.assertEqual(name, ['protein', 'fat', 'carbs', 'calories', 'water'])

    def test_get_new_data_bad_input(self):
        """
        Adds a new entry after one failed attempt.
        """
        self.input_values = ['a', '1 2 3 4']
        result, name = self.procedure.get_new_data(connection=self.connection)
        # calories value calculated from provided input
        self.assertEqual(result, [1, 2, 3, 4, 34])
        self.assertEqual(name, ['protein', 'fat', 'carbs', 'calories', 'water'])

    def test_get_new_data_quit(self):
        """
        User aborts adding a new nutrition entry.
        """
        self.input_values = ['q']
        result, name = self.procedure.get_new_data(connection=self.connection)
        self.assertEqual(result, [])

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates separate plots for all nutrition items
        """
        self.procedure.view_data(connection=self.connection)
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
        self.procedure.view_data(connection=self.connection,
                                 column_names=['protein'])
        date_item = datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water_%s.png' % date_item)))

    def test_view_data_bad_columns(self):
        """
        Tries to create a plot with an invalid database column.
        """
        self.procedure.view_data(connection=self.connection,
                                 column_names=['bad'])
        date_item = datetime.datetime.now().strftime('%m_%d')
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_protein_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_fat_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_carbs_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_calories_%s.png' % date_item)))
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, 'nutrition_water_%s.png' % date_item)))

    # ------------------------------------------------------------------------------------------------------------------
    # table_to_csv tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_dump_csv_nominal(self):
        """
        Creates a csv file from values within the database table.
        """
        csv_name = db_api.table_to_csv(connection=self.connection,
                                       table=self.procedure.table,
                                       output_dir=self.logs_dir)
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, csv_name)))

    def test_dump_csv_bad_path(self):
        """
        Attempts to create a csv file but a bad output path is provided.
        :return:
        """
        csv_name = db_api.table_to_csv(connection=self.connection,
                                       table=self.procedure.table,
                                       output_dir='bad_path')
        self.assertEqual(None, csv_name)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
