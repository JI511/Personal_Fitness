# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
import datetime
from src.Util import database_api as db_api
from src.Procedures import body_weight
from src.Procedures import procedure


class TestBodyWeightProcedure(unittest.TestCase):
    """
    Class for testing the body weight procedure.
    """
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(db_path=os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = body_weight.BodyWeightProcedure(output_dir=self.logs_dir)
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        body_weight.input = mock_input
        procedure.input = mock_input
        db_api.create_table(connection=self.connection,
                            table=self.procedure.table,
                            query=self.procedure.query)
        for _ in range(5):
            unique_id = db_api.add_new_row(connection=self.connection,
                                           table=self.procedure.table)
            db_api.update_item(connection=self.connection,
                               table=self.procedure.table,
                               value_tuple=(100, unique_id),
                               column_names=['body_weight'])

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
        Provides mock user input for a body weight entry.
        """
        self.input_values = ['100']
        result, name = self.procedure.get_new_data(connection=self.connection)
        self.assertEqual(result, [100])
        self.assertEqual(name, ['body_weight'])

    def test_get_new_data_bad_input(self):
        """
        The first input value shall be rejected and the second accepted.
        :return:
        """
        self.input_values = ['a', '100']
        result, name = self.procedure.get_new_data(connection=self.connection)
        self.assertEqual(result, [100])

    def test_get_new_data_quit(self):
        """
        The user needs to be able to exit the input prompt screen why a 'q' is provided.
        """
        self.input_values = ['q']
        result, name = self.procedure.get_new_data(connection=self.connection)
        self.assertEqual(result, [])

    # ------------------------------------------------------------------------------------------------------------------
    # get_new_data_from_file tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_new_data_from_file_nominal(self):
        """
        Adds multiple values to database via text file.
        """
        path = os.path.join(os.getcwd(), r'tests\support_files\body_weight_inputs.txt')
        self.input_values = [str(path)]
        self.procedure.get_new_data_from_file(connection=self.connection)
        column_dict = db_api.get_table_columns_dict(connection=self.connection,
                                                    table=self.procedure.table,
                                                    column_names=['body_weight'])
        self.assertEqual(column_dict['body_weight'], [100, 100, 100, 100, 100, 10, 20, 30, 40,
                                                      50, 60, 70, 80, 90, 100])

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates a plot from body weight entries.
        """
        self.procedure.view_data(connection=self.connection)
        plot_name = 'body_weight_body_weight_%s.png' % datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, plot_name)))

    def test_view_data_bad_column_names(self):
        """
        Attempts to create a plot with an invalid column name.
        """
        self.procedure.view_data(connection=self.connection,
                                 column_names=['bad'])
        plot_name = 'body_weight_body_weight_%s.png' % datetime.datetime.now().strftime('%m_%d')
        self.assertFalse(os.path.exists(os.path.join(self.logs_dir, plot_name)))

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
