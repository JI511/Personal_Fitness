# ----------------------------------------------------------------------------------------------------------------------
#    Weight Lifting test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil

from src.Util import constants
from src.Util import database_api as db_api
from src.Procedures import weight_lifting


class TestWeightLifting(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.logs_dir, 'test_database.db')
        self.table = 'weight_lifting'
        self.query = constants.weight_lifting_compound_query
        self.names = constants.weight_lifting_bench_press + constants.weight_lifting_deadlift
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        weight_lifting.input = mock_input
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
        Adds a new entry into the weight lifting table.
        """
        self.input_values = ['9', 'y']
        result, names = weight_lifting.get_new_data()
        self.assertEqual(result, list(range(0, 24)))
        unique_id = db_api.add_new_row(self.db_path, self.table)
        result.append(unique_id)
        db_api.update_item(self.db_path, self.table, tuple(result), names)
        self.assertTrue(os.path.exists(self.db_path))

    # ------------------------------------------------------------------------------------------------------------------
    # get_max_lift_updates tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_max_lift_updates_nominal(self):
        """
        Updates the max lift values for the weight lifting procedure.
        """
        self.input_values = ['9', '100', '200']
        result, names = weight_lifting.get_max_lift_updates()
        self.assertEqual(result, [100, 200])
        table = 'max_lifts'
        db_api.create_table(self.db_path, table, constants.max_lifts_query)
        unique_id = db_api.add_new_row(self.db_path, table)
        result.append(unique_id)
        db_api.update_item(self.db_path, table, tuple(result), names)

    # ------------------------------------------------------------------------------------------------------------------
    # get_workout_item_names tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_workout_item_names_nominal(self):
        """
        Gets the desired column names based off selected compound lifts.
        """
        group = ['bench', 'deadlift']
        result = weight_lifting.get_workout_item_names(group)
        self.assertEqual(result, self.names)

    def test_get_workout_item_names_empty_group(self):
        """
        Gets no columns when no groups are passed in.
        :return:
        """
        result = weight_lifting.get_workout_item_names([])
        self.assertEqual([], result)

    # ------------------------------------------------------------------------------------------------------------------
    # determine_muscle_group tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_determine_muscle_group_nominal(self):
        """
        Gets a list of compound activities based on a binary input.
        """
        self.input_values = ['9']
        result = weight_lifting.determine_muscle_group('')
        self.assertEqual(result, ['bench', 'deadlift'])

    def test_determine_muscle_group_bad_number(self):
        """
        An 0 is entered and should not be accepted since no groups will be returned.
        """
        self.input_values = ['0', '9']
        result = weight_lifting.determine_muscle_group('')
        self.assertEqual(result, ['bench', 'deadlift'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
