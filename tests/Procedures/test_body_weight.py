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


class TestBodyWeight(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = body_weight.BodyWeightProcedure(self.logs_dir)
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        body_weight.input = mock_input
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
        Provides mock user input for a body weight entry.
        """
        self.input_values = ['100']
        result, name = self.procedure.get_new_data()
        self.assertEqual(result, [100])
        self.assertEqual(name, ['body_weight'])

    def test_get_new_data_bad_input(self):
        """
        The first input value shall be rejected and the second accepted.
        :return:
        """
        self.input_values = ['a', '100']
        result, name = self.procedure.get_new_data()
        self.assertEqual(result, [100])

    # ------------------------------------------------------------------------------------------------------------------
    # view_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_view_data_nominal(self):
        """
        Creates a plot from body weight entries.
        """
        for _ in range(1, 10):
            unique_id = db_api.add_new_row(self.connection, self.procedure.table)
            db_api.update_item(self.connection, self.procedure.table, (100, unique_id), ['body_weight'])
        self.procedure.view_data(self.connection)
        plot_name = 'body_weight_body_weight_%s.png' % datetime.datetime.now().strftime('%m_%d')
        self.assertTrue(os.path.exists(os.path.join(self.logs_dir, plot_name)))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
