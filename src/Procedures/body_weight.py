# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util import utilities as util

table = 'body_weight'


def get_new_data():
    """
    Get the input value from the user for body weight procedure.
    :return:
    """
    while True:
        weight_text = input("What did you weigh today?\n"
                            "Optional: Input a file path to add multiple values (.txt)\n")
        try:
            result = [int(weight_text)]
            logging.getLogger(__name__).info('Weight text retrieved: %s' % weight_text)
            return result
        except ValueError:
            result = util.read_file_values(weight_text)
            if result is None:
                logging.getLogger(__name__).info('Invalid option, please enter a valid number or valid path.')
            else:

                return result


def view_data(db_path, output_path):
    """
    Creates a plot for all body weight entries.

    :param db_path: The path to the DB file.
    :param output_path: The desired output path for plots.
    """
    columns = ['body_weight']
    util.plot_data(db_path, table, columns, output_path)
    logging.getLogger(__name__).info('Plots created for %s table' % table)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
