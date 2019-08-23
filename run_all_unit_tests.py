# ----------------------------------------------------------------------------------------------------------------------
#    Unit Test Master File
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import os

from tests.Util.Test_Help import suite


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
    runner = unittest.TextTestRunner(file)
    for test in suite():
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
