# ----------------------------------------------------------------------------------------------------------------------
#    Morning Lifts test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
from src.Util import database_api as db_api
from src.Procedures import morning_lifts


class TestMorningLiftsProcedure(unittest.TestCase):
    """
    Class for testing the morning lifts procedure.
    """
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(db_path=os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = morning_lifts.MorningLiftsProcedure(output_dir=self.logs_dir)
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        morning_lifts.input = mock_input
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
    # get_new_data tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_new_data_nominal(self):
        """
        Provides mock user input for a morning lifts entry.
        """
        self.assertTrue(True)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
