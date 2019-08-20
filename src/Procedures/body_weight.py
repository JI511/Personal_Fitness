# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import database_api as db_api
from src.Util import constants
from src.Util import utilities as util

table = 'body_weight'


def add_new_data():
    while True:
        weight_text = input("What did you weigh today?\n"
                            "Optional: Input a file path to add multiple values (.txt)\n")
        try:
            result = int(weight_text)
            break
        except ValueError:
            result = util.read_file_values(weight_text)
            if result is None:
                print('Invalid option, please enter a valid number or valid path.')
            else:
                raise
    db_api.create_table(constants.database_path, table, constants.body_weight_query)
    if not isinstance(result, list):
        result = [result]
    for item in result:
        unique_id = db_api.add_new_row(constants.database_path, table)
        values = (item, unique_id)
        names = ["body_weight"]
        db_api.update_item(constants.database_path, table, values, names)
    db_api.get_table_rows(constants.database_path, table)


def view_data():
    util.plot_data(constants.database_path, table, ['body_weight'])

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
