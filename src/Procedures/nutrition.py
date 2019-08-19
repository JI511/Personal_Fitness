# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

from Util import database_api as db_api
from Util import constants
from Util import utilities as util

table = 'nutrition'


def add_new_data():

    while True:
        macros_text = input("Enter your Protein, Fat, and Carbs intake (g) separated by spaces:\n")
        water_text = input("Please enter your water intake in ml:\n")
        try:
            if macros_text == "" or water_text == "":
                print("Nothing was entered, please try again.")
            else:
                macros_list = macros_text.split(" ")
                if len(macros_list) != 3:
                    print("Invalid number of entries for macros entry, please try again")
                    continue
                water = int(water_text)
                all_values = [water]
                for value in macros_list:
                    all_values.append(int(value))
                protein, fat, carbohydrates = int(macros_list[0]), int(macros_list[1]), int(macros_list[2])
                break
        except ValueError:
            result = util.read_file_values(macros_text)
            if result is None:
                print('Invalid option, please enter a valid number or valid path.')
            else:
                raise
    # calculate calories
    all_values.append((protein * 4) + (fat * 9) + (carbohydrates * 4))
    names = ["protein", "fat", "carbohydrates", "calories", "water"]
    db_api.create_table(constants.database_path, table, constants.nutrition_query)
    unique_id = db_api.add_new_row(constants.database_path, table)
    all_values.append(unique_id)
    db_api.update_item(constants.database_path, table, tuple(all_values), names)
    db_api.get_table_rows(constants.database_path, table)


def view_data():
    util.plot_data(constants.database_path, table, ['nutrition'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
