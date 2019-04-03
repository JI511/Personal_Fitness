#############################################################
#             Personal Fitness Application                  #
#                                                           #
#            Store and track progress for multiple          #
#           different fitness areas. Current plans          #
#            are body weight, calories, and lifted          #
#             weights.                                      #
#############################################################

# imports
from procedures import calories as calories
from procedures import weight_lifting as weight_lifting
from procedures import body_weight as body_weight
import Utilities


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


if __name__ == '__main__':
    print("Starting Fitness Application...")
    procedure_text = input(
        "Which application would you like to run?\n1: Body Weight\n2: Calories\n3: Weight Lifting\nq: Quit\n")
    while procedure_text != "q":
        if procedure_text == '1':
            weight_procedure()
        elif procedure_text == '2':
            calorie_procedure()
        elif procedure_text == '3':
            lifting_procedure()
        elif procedure_text == 'q':
            print("Goodbye.")
        else:
            print("No valid option entered.")
        procedure_text = input(
            "What would you like to do next?\n1: Body Weight\n2: Calories\n3: Weight Lifting\nq: Quit\n")
