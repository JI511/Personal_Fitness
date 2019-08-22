# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

from src.Util import database_api as db_api
from src.Util import constants
from src.Util import utilities as util

table = 'nutrition'


def add_new_data():
    """
    Gathers user input about macros and water intake. Appends values to database file.
    """
    while True:
        macros_text = input("Enter your protein, tat, carbs (g), and water intake separated by spaces:\n")
        # water_text = input("Please enter your water intake in ml:\n")
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
    # todo move where all this is done
    # calculate calories
    # all_values.append((protein * 4) + (fat * 9) + (carbohydrates * 4))
    # names = ["protein", "fat", "carbohydrates", "calories", "water"]
    # db_api.create_table(constants.database_path, table, constants.nutrition_query)
    # unique_id = db_api.add_new_row(constants.database_path, table)
    # all_values.append(unique_id)
    # db_api.update_item(constants.database_path, table, tuple(all_values), names)


def view_data():
    util.plot_data(constants.database_path, table, ['nutrition'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
