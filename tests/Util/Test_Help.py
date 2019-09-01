import unittest
import os

from tests.Util.test_database_api import TestDatabaseApi
from tests.Util.test_utilities import TestUtilities
from tests.Procedures.test_body_weight import TestBodyWeight
from tests.Procedures.test_nutrition import TestNutrition
from tests.Procedures.test_morning_lifts import TestMorningLifts
from tests.Procedures.test_weight_lifting import TestWeightLifting


def suite(starting_name=None):
    """
    Adds the file specific test cases to the test suite.

    :param starting_name: The test files must contain this in the name to be added to the suite.
    :return: The suite of tests.
    """
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.getcwd(), 'tests')):
        for name in filenames:
            if name.startswith('test') and name.endswith('.py'):
                pass

    test_classes = [("DatabaseApi", TestDatabaseApi),
                    ("Utilities", TestUtilities),
                    ("BodyWeight", TestBodyWeight),
                    ("Nutrition", TestNutrition),
                    ("MorningLifts", TestMorningLifts),
                    ("WeightLifting", TestWeightLifting)
                    ]
    test_list = None
    if starting_name is not None:
        test_list = []
        for test_class in test_classes:
            if starting_name in test_class[0].lower():
                test_list.append(test_class)
    my_tests = test_list if test_list is not None else test_classes
    print(my_tests)
    my_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for item in my_tests:
        my_suite.addTests(loader.loadTestsFromTestCase(item[1]))
    print("Starting " + str(my_suite.countTestCases()) + " unit tests...\n")
    return my_suite
