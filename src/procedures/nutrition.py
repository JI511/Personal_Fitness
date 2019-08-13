# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

from Util import database_api as db_api
from Util import constants
from Util import Utilities as util

table = 'nutrition'


def add_new_data():

    while True:
        nutrition_text = input("Enter your Protein,Fat and Carbs intake (g) separated by spaces: ")
        water_text = input("Please enter your water intake in ml: ")

        try:
            macros_text = nutrition_text.split(" ")
            protein, fat, carbohydrates = int(macros_text[0]), int(macros_text[1]), int(macros_text[2])
            calories = ((protein*4) + (fat*9) + (carbohydrates*4))
            water = int(water_text)

            result = [protein, fat, carbohydrates, calories, water]
            names = ["protein", "fat", "carbohydrates", "calories", "water"]
            break
        except ValueError:
            result = util.read_file_values(nutrition_text)
            if result is None:
                print('Invalid option, please enter a valid number or valid path.')
            else:
                break

    db_api.create_table(constants.database_path, table, constants.nutrition_query)
    unique_id = db_api.add_new_row(constants.database_path, table)

    for indx, item in enumerate(result):
        values = (item, unique_id)
        db_api.update_item(constants.database_path, table, values, [names[indx]])

    db_api.get_table_rows(constants.database_path, table)


def view_data():
    util.plot_data(constants.database_path, table, ['nutrition'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
