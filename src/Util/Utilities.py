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


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
