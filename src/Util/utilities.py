# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
import numpy as np
from matplotlib import pyplot as plt
from src.Util import database_api as db_api
import logging

path = r"C:\Users\User\Desktop\Output"


def plot_data(db_path, table, column_names, output_path):
    """
    Gathers and plots all data points within the specified table

    :param db_path: Path to the DB file.
    :param str table: Name of table within the DB file.
    :param List column_names: Column names within the database.
    :param str output_path: Path to where plots should be saved.
    """
    plot_values = db_api.get_table_columns(db_path, table, column_names)
    for column in column_names:
        x = np.arange(len(plot_values[column]))
        y = np.asarray(plot_values[column])

        plt.title(table)
        plt.plot(x, y)
        try:
            my_path = os.path.join(output_path, "%s_%s.png" % (table, column))
            plt.savefig(my_path)
            logging.getLogger(__name__).info('Plot %s created.' % my_path)
        except Exception:
            raise


def write_log_file():
    """

    :return:
    """


def read_file_values(file_path):
    """
    Parses an input file and appends each line to a list.

    :param file_path: Path to the txt file
    :return: List of ints
    """
    file = open(file_path, 'r')
    values = list()
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
