# ----------------------------------------------------------------------------------------------------------------------
#    Lifting
# ----------------------------------------------------------------------------------------------------------------------

# imports
from Util import database_api as db_api
from Util import constants


def add_new_data():
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
    # print(max_lift_names)
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
    # print(max_lift_values)
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
    while True:
        accessories = input("Would you life to use default accessories?\n"
                            "y: yes\n"
                            "n: no\n")
        if accessories == 'y':
            break
        elif accessories == 'n':
            break


class Vars(object):
    Bench = 8
    Squat = 4
    Shoulder_Press = 2
    Deadlift = 1


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
