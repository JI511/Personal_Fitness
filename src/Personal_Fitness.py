# ----------------------------------------------------------------------------------------------------------------------
# Personal Fitness Application
#
# Store and track progress for multiple different fitness areas.
# Current plans are body weight, calories, morning lifts and lifted weights.
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
# import pathlib
from procedures import nutrition
from procedures import weight_lifting
from procedures import body_weight
from Util import Utilities
from Util import database_api as db_api
from Util import constants
from Util import config

# from .procedures import nutrition
# from .procedures import weight_lifting
# from .procedures import body_weight
# from .Util import Utilities
# from .Util import database_api as db_api
# from .Util import Constants


def weight_lifting_procedure():
    print("Weight lifting tracking and calculations.")
    weight_lifting_text = input("Would you like to view data or add a new entry?\n"
                                "1: New entry\n"
                                "2: View data\n"
                                "3: Update max lift values\n"
                                "4: Dump data to CSV\n"
                                )
    if weight_lifting_text == '1':
        weight_lifting.add_new_data()
    elif weight_lifting_text == '2':
        print('Not implemented!')
    elif weight_lifting_text == '3':
        weight_lifting.update_max_lifts()
    elif weight_lifting_text == '4':
        db_api.table_to_csv(constants.database_path, "weight_lifting")


def nutrition_procedure():
    print("Nutrition tracking and calculations.")
    calorie_text = input(constants.user_prompt)
    if calorie_text == '1':
        nutrition.add_new_data()
    elif calorie_text == '2':
        nutrition.view_data()
    elif calorie_text == '3':
        db_api.table_to_csv(constants.database_path, "nutrition")


def body_weight_procedure():
    print("Body weight tracking and calculations")
    body_weight_text = input(constants.user_prompt)
    if body_weight_text == '1':
        body_weight.add_new_data()
    elif body_weight_text == '2':
        body_weight.view_data()
    elif body_weight_text == '3':
        db_api.table_to_csv(constants.database_path, "body_weight")


def morning_lifts_procedure():
    print("Morning lifts tracking")
    lifting_text = input(constants.user_prompt)
    table = "morning_lifts"
    if lifting_text == '1':
        db_api.create_table(constants.database_path, table, constants.morning_lifts_query)
        db_api.add_new_row(constants.database_path, table)
        # todo, how to add actual data
    elif lifting_text == '2':
        db_api.get_table_rows(constants.database_path, table)
    elif lifting_text == '3':
        db_api.table_to_csv(constants.database_path, "morning_lifts")


if __name__ == '__main__':
    print("Starting Fitness Application...")

    # if not pathlib.Path(r'.\Util\config.cfg').exists():
    #     print("No config found... Creating")
    #     config.init_cfg()

    config.read_cfg()

    while True:
        procedure_text = input(
            "Which application would you like to run?\n"
            "1: Body Weight\n"
            "2: Nutrition\n"
            "3: Weight Lifting\n"
            "4: Morning Lifts\n"
            "q: Quit\n")
        if procedure_text == '1':
            body_weight_procedure()
        elif procedure_text == '2':
            nutrition_procedure()
        elif procedure_text == '3':
            weight_lifting_procedure()
        elif procedure_text == '4':
            morning_lifts_procedure()
        elif procedure_text.lower() == 'q':
            print("Goodbye.")
            break
        else:
            print("No valid option entered.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
