# ----------------------------------------------------------------------------------------------------------------------
#    Unit Test Master File
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import os
from Util import test_database_api as test_db
# from .Util.test_database_api import TestDatabaseApi


def suite():
    """
    Adds the file specific test cases to the test suite.

    :return: The suite of tests.
    """
    modules_to_test = []
    test_dir = os.listdir('.')
    print(test_dir)
    for test in test_dir:
        if test.startswith('test') and test.endswith('.py'):
            modules_to_test.append(test.rstrip('.py'))

    print(modules_to_test)
    my_suite = unittest.TestSuite()
    my_suite.addTest(test_db.TestDatabaseApi('test_nominal'))
    return my_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
