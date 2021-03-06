# ----------------------------------------------------------------------------------------------------------------------
#    Constants
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os


def generate_sets_item_query(names, sets):
    """
    Builds a query with a specified number of sets.

    :param list names: The name of the workout item.
    :param int sets: The number of sets to generate in the query.
    :return: SQL compatible query as a string.
    """
    master_tuple_list = []
    for name in names:
        for index in range(1, sets + 1):
            master_tuple_list.append(('%s_set_%s' % (name, index), 'real'))
            master_tuple_list.append(('%s_set_%s_reps' % (name, index), 'integer'))
    return master_tuple_list


def generate_query(query_tuples):
    """
    Builds a query from a list of tuples.

    :param List query_tuples: Lists of tuples to build query item.
    :return: SQL compatible query as a string.
    """
    # prepend ID and date items
    master_query = ("ID integer PRIMARY KEY ASC NOT NULL,"
                    "date text,")
    for name in query_tuples:
        master_query += '%s %s,' % (name[0], name[1])
    return master_query[:-1]


class Constants(object):
    database_path = os.path.join(os.getcwd(), 'health_database.db')
    output_path = os.path.join(os.getcwd(), 'output_files')
    csv_path = ""
    logs_path = ""
    water_option = 'mL'

    config_defaults = {
        "OPTIONS": {
            "water": "oz",
            "backup_rate": '7'
        }
    }

    user_prompt = "Would you like to view data or add a new entry?\n" \
                  "1: New entry\n" \
                  "2: Multiple entries via file\n" \
                  "3: View plots\n" \
                  "4: Dump data to csv\n" \
                  "q: Return to title\n"

    weight_lifting_accessories_query_tuple = [('elliptical', 'integer'),
                                              ('chin_up', 'integer'),
                                              ('chin_up_sets_reps', 'text'),
                                              ('dips', 'integer'),
                                              ('dips_sets_reps', 'text'),
                                              ('grip_roller_sets_reps', 'text'),
                                              ('face_pulls', 'integer'),
                                              ('face_pulls_sets_reps', 'text')]

    body_weight_query_tuple = [('body_weight', 'integer')]

    max_lifts_query_tuple = [('bench_press_max', 'integer'),
                             ('squat_max', 'integer'),
                             ('shoulder_press_max', 'integer'),
                             ('deadlift_max', 'integer')]

    nutrition_query_tuple = [('calories', 'integer'),
                             ('protein', 'integer'),
                             ('carbs', 'integer'),
                             ('fat', 'integer'),
                             ('water', 'integer')]

    morning_lifts_query_tuple = [('shoulder_lateral_raise', 'text'),
                           ('shoulder_front_raises', 'text'),
                           ('shoulder_arnold_press', 'text'),
                           ('bicep_hammer_curl', 'text'),
                           ('bicep_curl', 'text'),
                           ('legs_dumbbell_squat', 'text'),
                           ('abs_ab_roller', 'text'),
                           ('abs_ab_shrugs', 'text')]

    morning_lifts_query = generate_query(query_tuples=morning_lifts_query_tuple)

    nutrition_query = generate_query(query_tuples=nutrition_query_tuple)

    max_lifts_query = generate_query(query_tuples=max_lifts_query_tuple)

    body_weight_query = generate_query(query_tuples=body_weight_query_tuple)

    weight_lifting_accessories_query = generate_query(query_tuples=weight_lifting_accessories_query_tuple)

    weight_lifting_compound_query = generate_query(query_tuples=generate_sets_item_query(names=['bench_press',
                                                                                                'squat',
                                                                                                'shoulder_press',
                                                                                                'deadlift'],
                                                                                         sets=6))


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
