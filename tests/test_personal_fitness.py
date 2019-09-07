# ----------------------------------------------------------------------------------------------------------------------
#    Personal Fitness test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil

from src.Util import database_api as db_api
from src.Personal_Fitness import PersonalFitness


class TestPersonalFitness(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = None
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        PersonalFitness.input = mock_input

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    def test_nominal(self):
        self.assertTrue(True)
# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
