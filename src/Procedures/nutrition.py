# ----------------------------------------------------------------------------------------------------------------------
#    Calories
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util import utilities as util
from src.Procedures.procedure import Procedure
from src.Util.constants import Constants

# table = 'nutrition'


class NutritionProcedure(Procedure):
    """
    Handles the specific procedures for nutrition gathering and display.
    """
    def __init__(self, output_dir=None):
        """
        Setup for nutrition procedure.

        :param output_dir: Optional output directory if not the default.
        """
        super(NutritionProcedure, self).__init__(table='nutrition',
                                                 output_dir=output_dir,
                                                 query=Constants.nutrition_query,
                                                 logger=logging.getLogger(__name__),
                                                 names=["protein", "fat", "carbs", "calories", "water"])
        self.logger.info('Nutrition tracking and calculations.')

    def get_new_data(self, connection):
        """
        Gathers user input about macros and water intake. Appends values to database file.
        """
        while True:
            macros_text = input("Enter your protein, fat, carbs (g), and water intake separated by spaces:\n")
            try:
                if macros_text == "":
                    print("Nothing was entered, please try again.")
                else:
                    all_values = [int(a) for a in macros_text.split(" ")]
                    if len(all_values) != 4:
                        continue
                    calories = (all_values[0] * 4) + (all_values[1] * 9) + (all_values[2] * 4)
                    all_values.append(calories)
                    self.append_new_entry(connection=connection,
                                          values=all_values,
                                          column_names=self.names)
                    return all_values, self.names
            except ValueError:
                result = util.read_file_values(file_path=macros_text,
                                               logger=self.logger)
                if result is None:
                    print('Invalid option, please enter a valid number or valid path.')
                else:
                    raise

    def get_new_data_from_file(self, connection):
        pass


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
