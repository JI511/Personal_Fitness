# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import utilities as util
from src.Util import constants
from src.Procedures.procedure import Procedure

table = 'body_weight'


class BodyWeightProcedure(Procedure):
    """

    """
    def __init__(self):
        """

        """
        super(BodyWeightProcedure, self).__init__('body_weight', constants.output_path,
                                                  constants.body_weight_query)

    def get_new_data(self):
        """
        Get the input value from the user for body weight procedure.
        :return:
        """
        while True:
            weight_text = input("What did you weigh today?\n"
                                "Optional: Input a file path to add multiple values (.txt)\n")
            try:
                return [int(weight_text)]
            except ValueError:
                result = util.read_file_values(weight_text)
                if result is None:
                    print('Invalid option, please enter a valid number or valid path.')
                else:
                    return result


def view_data(db_path, output_path):
    """
    Creates a plot for all body weight entries.

    :param db_path: The path to the DB file.
    :param output_path: The desired output path for plots.
    """
    util.plot_data(db_path, table, ['body_weight'], output_path)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
