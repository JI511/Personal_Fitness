# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

from src.Util import utilities as util
from src.Procedures.procedure import Procedure
from src.Util import constants

# table = 'nutrition'


class NutritionProcedure(Procedure):
    """
    Handles the specific procedures for nutrition gathering and display.
    """
    def __init__(self):
        """
        Setup the nutrition specific values.
        """
        print("Nutrition tracking and calculations.")
        super(NutritionProcedure, self).__init__(table='nutrition',
                                                 output_path=constants.output_path,
                                                 query=constants.nutrition_query)

    @staticmethod
    def get_new_data():
        """
        Gathers user input about macros and water intake. Appends values to database file.
        """
        names = ["protein", "fat", "carbs", "calories", "water"]
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
                    return all_values, names
            except ValueError:
                result = util.read_file_values(macros_text)
                if result is None:
                    print('Invalid option, please enter a valid number or valid path.')
                else:
                    raise


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
