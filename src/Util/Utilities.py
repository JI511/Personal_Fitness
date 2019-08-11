# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
import numpy as np
from matplotlib import pyplot as plt


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


def retrieve_data(procedure):
    print("Retrieve %s data" % procedure)
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sine wave form")

    # Default plot for now
    plt.plot(x, y)
    plt.show()


def read_file_values(path):
    """
    Parses an input file and appends each line to a list.

    :param path: Path to the txt file
    :return: List of ints
    """
    file = open(path, 'r')
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
