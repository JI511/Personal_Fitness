# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
from Util import database_api as db_api
from Util import constants


def add_new_data():
    table = 'body_weight'
    while True:
        text = input("What did you weigh today?\n")
        try:
            result = int(text)
            break
        except ValueError:
            print('Invalid literal, please enter a number.')
    db_api.create_table(constants.database_path, table, constants.body_weight_query)
    unique_id = db_api.add_new_row(constants.database_path, table)
    values = (result, unique_id)
    names = ["body_weight"]
    db_api.update_item(constants.database_path, table, values, names)
    db_api.get_table_rows(constants.database_path, table)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
