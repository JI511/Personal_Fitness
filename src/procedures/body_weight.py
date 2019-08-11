# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
from Util import database_api as db_api
from Util import constants
from Util import Utilities as util


def add_new_data():
    table = 'body_weight'
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
                break
    db_api.create_table(constants.database_path, table, constants.body_weight_query)
    if not isinstance(result, list):
        result = [result]
    print(result)
    for item in result:
        unique_id = db_api.add_new_row(constants.database_path, table)
        values = (item, unique_id)
        names = ["body_weight"]
        db_api.update_item(constants.database_path, table, values, names)
    db_api.get_table_rows(constants.database_path, table)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
