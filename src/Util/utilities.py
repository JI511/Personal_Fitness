# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
import numpy as np
import logging
import datetime
from matplotlib import pyplot as plt


def plot_data(table, column_dict, output_path):
    """
    Gathers and plots all data points within the specified table

    :param str table: Name of table within the DB file.
    :param List column_dict: Column names within the database.
    :param str output_path: Path to where plots should be saved.
    """
    for column in column_dict.keys():
        x = np.arange(len(column_dict[column]))
        y = np.asarray(column_dict[column])
        plt.title(table)
        plt.plot(x, y)
        try:
            my_path = os.path.join(output_path, "%s_%s_%s.png" % (table,
                                                                  column,
                                                                  datetime.datetime.now().strftime('%m_%d')))
            plt.savefig(my_path)
            logging.getLogger(__name__).info('Plot %s created.' % my_path)
        except Exception:
            raise


def read_file_values(file_path):
    """
    Parses an input file containing integer values and appends each line to a list.

    :param file_path: Path to the txt file
    :return: List of ints
    """
    # todo fix this, check path
    values = None
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        values = []
        for line in file:
            try:
                number = int(line)
                values.append(number)
            except ValueError:
                print("There was an invalid number present.")
                return None
    return values

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
