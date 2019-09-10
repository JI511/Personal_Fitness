# imports
import unittest
import tempfile
import os
import shutil
import datetime
from src.Util import database_api as db_api
from src.Procedures import body_weight
from src.Procedures import procedure


class TestProcedure(unittest.TestCase):
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

        procedure.input = mock_input
        db_api.create_table(connection=self.connection,
                            table=self.procedure.table,
                            query=self.procedure.query)

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

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
        self.assertEqual(column_dict['body_weight'], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
