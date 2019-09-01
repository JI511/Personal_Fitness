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
print(name)
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
      "##########################################################\n")

log_file = os.path.join(os.getcwd(), "logs.txt")
fail_count = 0
with open(log_file, "w") as file:
    file.write(str(datetime.datetime.now()))
    runner = unittest.TextTestRunner(file)
    for test in suite(name):
        result = runner.run(test)
        if result.wasSuccessful():
            print(str(test) + "           PASS")
        else:
            print(str(test) + "           FAIL\n\n***** DEBUG *****\n")
            if len(result.failures) != 0:
                for failure in result.failures[0]:
                    print(failure)
            if len(result.errors) != 0:
                for error in result.errors[0]:
                    print(error)
            fail_count += 1
if fail_count == 0:
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
          "    ###")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
