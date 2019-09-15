# ----------------------------------------------------------------------------------------------------------------------
#    Unit Test Master File
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import argparse

print("##########################################################\n"
      "######                                              ######\n"
      "######      ##    ##  ##    ##   ##   ######        ######\n"
      "######      ##    ##  ###   ##   ##     ##          ######\n"
      "######      ##    ##  ## #  ##   ##     ##          ######\n"
      "######      ##    ##  ##  # ##   ##     ##          ######\n"
      "######      ##    ##  ##   ###   ##     ##          ######\n"
      "######      ########  ##    ##   ##     ##          ######\n"
      "######                                              ######\n"
      "######                     tests                    ######\n"
      "######                                              ######\n"
      "##########################################################\n")

parser = argparse.ArgumentParser()
parser.add_argument("-t", help='Specify the tests to run by test name.')
args = parser.parse_args()
name = 'test_' + args.t + '*.py' if args.t is not None else 'test*.py'

loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity=2)
runner.run(loader.discover(start_dir='tests', pattern=name))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
