# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

from src.Util import utilities as util

table = 'nutrition'


def get_new_data():
    """
    Gathers user input about macros and water intake. Appends values to database file.
    """
    while True:
        macros_text = input("Enter your protein, tat, carbs (g), and water intake separated by spaces:\n")
        try:
            if macros_text == "":
                print("Nothing was entered, please try again.")
            else:
                macros_list = macros_text.split(" ")
                if len(macros_list) != 4:
                    print("Invalid number of entries for macros entry, please try again")
                    continue
                all_values = []
                for value in macros_list:
                    all_values.append(int(value))
                all_values.append((all_values[0] * 4) + (all_values[1] * 9) + (all_values[2] * 4))
                return all_values
        except ValueError:
            result = util.read_file_values(macros_text)
            if result is None:
                print('Invalid option, please enter a valid number or valid path.')
            else:
                raise


def view_data(db_path, output_path, column_names=None):
    """
    Creates a separate plot for all nutrition columns by default.

    :param db_path: The path to the DB file.
    :param str output_path: The desired output directory for created plots.
    :param List column_names: Optional to only plot certain nutrition items.
    """
    columns = ["protein", "fat", "carbs", "calories", "water"]
    if column_names is not None:
        columns = column_names
    util.plot_data(db_path, table, columns, output_path)

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
