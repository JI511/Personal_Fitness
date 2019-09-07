# ----------------------------------------------------------------------------------------------------------------------
#    Unit Test Master File
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import os
import datetime
import argparse

from tests.Util.Test_Help import suite

parser = argparse.ArgumentParser()
parser.add_argument("-t", help='Specify the tests to run by test name.')
args = parser.parse_args()
name = args.t if args.t is not None else None
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

log_file = os.path.join(os.getcwd(), "unit_test_logs.txt")
fail_list = []
error_list = []
with open(log_file, "w") as file:
    file.write(str(datetime.datetime.now()))
    runner = unittest.TextTestRunner(file)
    for test in suite(name):
        result = runner.run(test)
        if result.wasSuccessful():
            print(str(test) + "           PASS")
        else:
            print(str(test) + "           FAIL")
            if len(result.failures) != 0:
                fail_list.append(str(test))
                for failure in result.failures[0]:
                    print(failure)
            if len(result.errors) != 0:
                error_list.append(str(test))
                for error in result.errors[0]:
                    print(error)
if len(fail_list) == 0 and len(error_list) == 0:
    print("\n##################\n"
          "#                #\n"
          "#    All tests   #\n"
          "#   successful!  #\n"
          "#                #\n"
          "##################")
else:
    print("\n    ###\n"
          "    ###\n"
          "    ###\n"
          "    ###        Errors!\n"
          "    ###\n"
          "    ###\n"
          "\n"
          "    ###\n"
          "    ###\n")
    if len(fail_list) != 0:
        print('\nFailures:')
        for f in fail_list:
            print(f)
    if len(error_list) != 0:
        print('\nErrors:')
        for e in error_list:
            print(e)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
