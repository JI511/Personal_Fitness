# ----------------------------------------------------------------------------------------------------------------------
#             Personal Fitness Application                  #
#                                                           #
#            Store and track progress for multiple          #
#           different fitness areas. Current plans          #
#            are body weight, calories, and lifted          #
#             weights.                                      #
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os
from procedures import calories as calories
from procedures import weight_lifting as weight_lifting
from procedures import body_weight as body_weight
from Util import Utilities
from Util import database_api as db_api
from Util import Constants



def weight_procedure():
    print("Body weight calculations.")
    body_weight_text = input("Would you like to view data or add a new entry?\n1: New entry\n2: View data\n")
    if body_weight_text == '1':
        Utilities.new_entry("body_weight")
    elif body_weight_text == '2':
        Utilities.retrieve_data("body_weight")


def calorie_procedure():
    print("Calorie track and calculations.")
    calorie_text = input("Would you like to view data or add a new entry?\n1: New entry\n2: View data\n")
    if calorie_text == '1':
        Utilities.new_entry("calorie")
    elif calorie_text == '2':
        Utilities.retrieve_data("calorie")


def lifting_procedure():
    print("Weight lifting tracking and calculations")
    lifting_text = input("Would you like to view data or add a new entry?\n1: New entry\n2: View data\n")
    if lifting_text == '1':
        Utilities.new_entry("weight_lifting")
    elif lifting_text == '2':
        Utilities.retrieve_data("weight_lifting")


def morning_lifts_procedure():
    print("Morning lifts tracking")
    lifting_text = input("Would you like to view data or add a new entry?\n"
                         "1: New entry\n"
                         "2: View data\n")
    table = "morning_lifts"
    if lifting_text == '1':
        db_api.create_table(Constants.database_path, table, Constants.morning_lifts_query)
        db_api.add_new_row(Constants.database_path, table)
        # todo, how to add actual data
    elif lifting_text == '2':
        db_api.get_table_rows(Constants.database_path, table)


if __name__ == '__main__':
    print("Starting Fitness Application...")
    while True:
        procedure_text = input(
            "Which application would you like to run?\n"
            "1: Body Weight\n"
            "2: Calories\n"
            "3: Weight Lifting\n"
            "4: Morning Lifts\n"
            "q: Quit\n")
        if procedure_text == '1':
            weight_procedure()
        elif procedure_text == '2':
            calorie_procedure()
        elif procedure_text == '3':
            lifting_procedure()
        elif procedure_text == '4':
            morning_lifts_procedure()
        elif procedure_text == 'q':
            print("Goodbye.")
            break
        else:
            print("No valid option entered.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
