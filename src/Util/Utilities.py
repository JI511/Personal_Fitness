# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
import datetime
import numpy as np
from matplotlib import pyplot as plt
from . import database_api as db_api

path = r"C:\Users\User\Desktop\Output"


def new_entry(procedure):
    print("New %s entry" % procedure)
    file_name = procedure + ".txt"
    full_path = os.path.join(path, file_name)
    file = open(full_path, "a")
    text = input("Enter a valid number\n")
    # todo add check for valid number
    file.write(text + "\n")
    file.close()


def plot_data(db_path, table, column_names):
    """
    Gathers and plots all data points within the specified table

    :param db_path: Path to the DB file.
    :param String table: Name of table within the DB file.
    :param List column_names: Column names within the database.
    """
    plot_values = db_api.get_column_items(db_path, table, column_names)
    for column in column_names:
        x = np.arange(len(plot_values[column]))
        y = np.asarray(plot_values[column])

        plt.title(table)
        plt.plot(x, y)
        save_text = input("Would you like to save the plot? y for yes:\n")
        if save_text == 'y':
            save_path = input("What path would you like to use?\n")
            try:
                my_path = os.path.join(save_path, (table + ".png"))
                plt.savefig(my_path)
            except Exception:
                raise
        plt.show()


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
