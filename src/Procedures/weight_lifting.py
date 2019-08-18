# ----------------------------------------------------------------------------------------------------------------------
#    Lifting
# ----------------------------------------------------------------------------------------------------------------------

# imports
from Util import database_api as db_api
from Util import constants


def add_new_data():
    """
    Adds a new entry into the weight lifting table within the health_database database.

    """
    table = 'weight_lifting'
    names = get_workout_item_names(determine_muscle_group('Which muscle groups did you work today?'))
    while True:
        use_default = input("Would you like to use default values based on current max?\n"
                            "y: yes\n"
                            "n: no\n")
        if use_default == 'y':
            values = get_default_lift_values(names)
            break
        elif use_default == 'n':
            # todo, allow for custom input
            values = get_default_lift_values(names)
            break
        print('Please enter a valid option')
    db_api.create_table(constants.database_path, table, constants.weight_lifting_compound_query)
    unique_id = db_api.add_new_row(constants.database_path, table)
    values = values + (unique_id,)
    db_api.update_item(constants.database_path, table, values, names)
    db_api.get_table_rows(constants.database_path, table)


def update_max_lifts():
    """
    Updates the user selected max lift values by getting input from the user.

    """
    table = 'max_lifts'
    names = determine_muscle_group('Which max values would you like to update?')
    max_lift_names = list()
    if 'bench' in names:
        max_lift_names.append('bench_press_max')
    if 'squat' in names:
        max_lift_names.append('squat_max')
    if 'shoulder_press' in names:
        max_lift_names.append('shoulder_press_max')
    if 'deadlift' in names:
        max_lift_names.append('deadlift_max')
    max_lift_values = tuple()
    for row in max_lift_names:
        while True:
            max_text = input("New " + row + "value:\n")
            try:
                max_update = int(max_text)
                max_lift_values = max_lift_values + (max_update,)
                break
            except ValueError:
                print('Invalid literal, please enter a number.')
    db_api.create_table(constants.database_path, table, constants.max_lifts_query)
    unique_id = db_api.add_new_row(constants.database_path, table)
    db_api.get_table_rows(constants.database_path, table)
    max_lift_values = max_lift_values + (unique_id,)
    db_api.update_item(constants.database_path, table, max_lift_values, max_lift_names)
    db_api.get_table_rows(constants.database_path, table)


def get_default_lift_values(names):
    """
    Get the current program lifting values for the day. This is to speed up input if the user is following
    a program.

    :param names:
    :return: The default values
    """
    values = tuple()
    for index, name in enumerate(names):
        values = values + (index,)
    return values


def get_workout_item_names(group):
    """
    Gets the column names for the specified workout group.

    :param List group: The user chosen compound lifts.
    :return: A list of Strings containing the column names to update.
    """
    rows = list()
    if 'squat' in group:
        rows = rows + constants.weight_lifting_squats
    if 'bench' in group:
        rows = rows + constants.weight_lifting_bench_press
    if 'shoulder_press' in group:
        rows = rows + constants.weight_lifting_shoulder_press
    if 'deadlift' in group:
        rows = rows + constants.weight_lifting_deadlift
    return rows


def determine_muscle_group(question_text):
    """
    Gets a binary input from the user to select the chosen compound lifts to update.

    :param question_text: Question for the user to determine which procedure is asking about compounds.
    :return: A list of Strings containing the chosen compound lifts.
    """
    while True:
        groups = input(question_text + " (Binary Entry)\n"
                       "8: Bench\n"
                       "4: Squat\n"
                       "2: Shoulder Press\n"
                       "1: Deadlift\n")
        try:
            result = int(groups)
            break
        except ValueError:
            print('Invalid literal, please enter a number.')
    muscle_groups = list()
    if (result & Vars.Bench) == 8:
        muscle_groups.append("bench")
    if (result & Vars.Squat) == 4:
        muscle_groups.append("squat")
    if (result & Vars.Shoulder_Press) == 2:
        muscle_groups.append("shoulder_press")
    if (result & Vars.Deadlift) == 1:
        muscle_groups.append("deadlift")
    return muscle_groups


def determine_accessories():
    """
    Similar to determine_muscle_group(), this gets the user chosen accessory values.

    :return: todo
    """
    while True:
        accessories = input("Would you life to use default accessories?\n"
                            "y: yes\n"
                            "n: no\n")
        if accessories == 'y':
            break
        elif accessories == 'n':
            break


class Vars(object):
    """
    Class to store the enum values for compound lifts.
    """

    Bench = 8
    Squat = 4
    Shoulder_Press = 2
    Deadlift = 1


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
