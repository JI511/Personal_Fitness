# ----------------------------------------------------------------------------------------------------------------------
# Personal Fitness Application
#
# Store and track progress for multiple different fitness areas.
# Current plans are body weight, calories, morning lifts and lifted weights.
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
from src.Procedures import nutrition
from src.Procedures import weight_lifting
from src.Procedures import body_weight
from src.Util import database_api as db_api
from src.Util import constants
from src.Util import config


def weight_lifting_procedure():
    print("Weight lifting tracking and calculations.")
    weight_lifting_text = input("Would you like to view data or add a new entry?\n"
                                "1: New entry\n"
                                "2: View data\n"
                                "3: Update max lift values\n"
                                "4: Dump data to CSV\n"
                                )
    table = 'weight_lifting'
    if weight_lifting_text == '1':
        db_api.create_table(constants.database_path, table, constants.weight_lifting_compound_query)
        unique_id = db_api.add_new_row(constants.database_path, table)
        results, names = weight_lifting.get_new_data()
        results.append(unique_id)
        db_api.update_item(constants.database_path, table, tuple(results), names)
    elif weight_lifting_text == '2':
        print('Not implemented!')
    elif weight_lifting_text == '3':
        table = 'max_lifts'
        db_api.create_table(constants.database_path, table, constants.max_lifts_query)
        unique_id = db_api.add_new_row(constants.database_path, table)
        results, names = weight_lifting.get_max_lift_updates()
        results.append(unique_id)
        db_api.update_item(constants.database_path, table, tuple(results), names)
    elif weight_lifting_text == '4':
        db_api.table_to_csv(constants.database_path, "weight_lifting")


def nutrition_procedure():
    print("Nutrition tracking and calculations.")
    calorie_text = input(constants.user_prompt)
    table = 'nutrition'
    names = ["protein", "fat", "carbohydrates", "calories", "water"]
    if calorie_text == '1':
        db_api.create_table(constants.database_path, table, constants.nutrition_query)
        unique_id = db_api.add_new_row(constants.database_path, table)
        results = nutrition.get_new_data()
        results.append(unique_id)
        db_api.update_item(constants.database_path, table, tuple(results), names)
    elif calorie_text == '2':
        nutrition.view_data(constants.database_path, constants.output_path)
    elif calorie_text == '3':
        db_api.table_to_csv(constants.database_path, "nutrition")


def body_weight_procedure():
    print("Body weight tracking and calculations")
    body_weight_text = input(constants.user_prompt)
    table = 'body_weight'
    names = ['body_weight']
    if body_weight_text == '1':
        db_api.create_table(constants.database_path, table, constants.body_weight_query)
        unique_id = db_api.add_new_row(constants.database_path, table)
        result = body_weight.get_new_data()
        result.append(unique_id)
        db_api.update_item(constants.database_path, table, tuple(result), names)
    elif body_weight_text == '2':
        body_weight.view_data(constants.database_path, constants.output_path)
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
        db_api.get_table_columns(constants.database_path, table)
    elif lifting_text == '3':
        db_api.table_to_csv(constants.database_path, "morning_lifts")


if __name__ == '__main__':
    print("Starting Fitness Application...")
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
