# ----------------------------------------------------------------------------------------------------------------------
#    Weight Lifting test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil

from src.Util import database_api as db_api
from src.Procedures import weight_lifting
from src.Util.constants import Constants
from src.Util import constants as const


class TestWeightLifting(unittest.TestCase):
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.connection = db_api.create_connection(os.path.join(self.logs_dir, 'test_database.db'))
        self.procedure = weight_lifting.WeightLiftingProcedure()
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        weight_lifting.input = mock_input
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
        Adds a new entry into the weight lifting table.
        """
        self.input_values = ['9', 'y']
        result, names = self.procedure.get_new_data(self.connection)
        self.assertEqual(result, list(range(0, 24)))
        self.assertEqual(names, [a[0] for a in const.generate_sets_item_query(['bench_press', 'deadlift'], 6)])

    def test_get_new_data_nominal_all(self):
        """
        Adds a new entry into the weight lifting table.
        """
        self.input_values = ['15', 'y']
        result, names = self.procedure.get_new_data(self.connection)
        self.assertEqual(result, list(range(0, 48)))
        # sort items since order doesn't matter
        self.assertEqual(names.sort(), [a[0] for a in const.generate_sets_item_query(['bench_press',
                                                                                      'deadlift',
                                                                                      'shoulder_press',
                                                                                      'squat'],
                                                                                     6)].sort())

    def test_get_new_data_bad_muscle_group_entry(self):
        """
        Adds a new entry into the weight lifting table after one failed attempt on selecting muscle group.
        """
        self.input_values = ['a', '9', 'y']
        result, names = self.procedure.get_new_data(self.connection)
        self.assertEqual(result, list(range(0, 24)))
        self.assertEqual(names, [a[0] for a in const.generate_sets_item_query(['bench_press', 'deadlift'], 6)])

    # ------------------------------------------------------------------------------------------------------------------
    # get_max_lift_updates tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_max_lift_updates_nominal(self):
        """
        Updates the max lift values for the weight lifting procedure.
        """
        self.input_values = ['9', '100', '200']
        result, names = self.procedure.get_max_lift_updates()
        self.assertEqual(result, [100, 200])
        table = 'max_lifts'
        db_api.create_table(self.connection, table, Constants.max_lifts_query)
        unique_id = db_api.add_new_row(self.connection, table)
        result.append(unique_id)
        db_api.update_item(self.connection, table, tuple(result), names)

    # ------------------------------------------------------------------------------------------------------------------
    # get_workout_item_names tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_get_workout_item_names_nominal(self):
        """
        Gets the desired column names based off selected compound lifts.
        """
        group = ['bench', 'deadlift']
        result = self.procedure.get_workout_item_names(group)
        self.assertEqual(result, [a[0] for a in const.generate_sets_item_query(group, 6)])

    def test_get_workout_item_names_empty_group(self):
        """
        Gets no columns when no groups are passed in.
        :return:
        """
        result = self.procedure.get_workout_item_names([])
        self.assertEqual([], result)

    # ------------------------------------------------------------------------------------------------------------------
    # determine_muscle_group tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_determine_muscle_group_nominal(self):
        """
        Gets a list of compound activities based on a binary input.
        """
        self.input_values = ['9']
        result = self.procedure.determine_muscle_group(question_text='Irrelevant question text')
        self.assertEqual(result, ['bench_press', 'deadlift'])

    def test_determine_muscle_group_bad_number(self):
        """
        An 0 is entered and should not be accepted since no groups will be returned.
        """
        self.input_values = ['0', '9']
        result = self.procedure.determine_muscle_group('')
        self.assertEqual(result, ['bench_press', 'deadlift'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
