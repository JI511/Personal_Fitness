# ----------------------------------------------------------------------------------------------------------------------
#    Unit Test Master File
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import os

from tests.Util.test_database_api import TestDatabaseApi
from tests.Util.test_utilities import TestUtilities
from tests.Procedures.test_body_weight import TestBodyWeight
from tests.Procedures.test_nutrition import TestNutrition
from tests.Procedures.test_morning_lifts import TestMorningLifts
from tests.Procedures.test_weight_lifting import TestWeightLifting


def suite():
    """
    Adds the file specific test cases to the test suite.

    :return: The suite of tests.
    """
    test_dir = os.listdir(os.path.join(os.getcwd(), 'tests'))
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.getcwd(), 'tests')):
        for name in filenames:
            if name.startswith('test') and name.endswith('.py'):
                pass

    test_classes = [TestDatabaseApi, TestUtilities, TestBodyWeight, TestNutrition, TestMorningLifts, TestWeightLifting]
    my_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for item in test_classes:
        my_suite.addTests(loader.loadTestsFromTestCase(item))
    print("Starting " + str(my_suite.countTestCases()) + " unit tests...\n")
    return my_suite


if __name__ == '__main__':
    print("##########################################################\n"
          "######                                              ######\n"
          "######      ##    ##  ##    ##   ##   ######        ######\n"
          "######      ##    ##  ###   ##   ##     ##          ######\n"
          "######      ##    ##  ## #  ##   ##     ##          ######\n"
          "######      ##    ##  ##  # ##   ##     ##          ######\n"
          "######      ##    ##  ##   ###   ##     ##          ######\n"
          "######      ########  ##    ##   ##     ##          ######\n"
          "######                                              ######\n"
          "######                 tests                        ######\n"
          "##########################################################\n" )

    log_file = os.path.join(os.getcwd(), "logs.txt")
    fail_count = 0
    with open(log_file, "w") as file:
        runner = unittest.TextTestRunner(file)
        for test in suite():
            result = runner.run(test)
            if result.wasSuccessful():
                print(str(test) + "           PASS")
            else:
                fail_count += 1
    if fail_count == 0:
        print("\n##################\n"
              "#                #\n"
              "#    All tests   #\n"
              "#   successful!  #\n"
              "#                #\n"
              "##################")
    else:
        print("###\n"
              "###\n"
              "###\n"
              "###\n"
              "###\n"
              "###\n"
              "\n"
              "###\n"
              "###")

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
