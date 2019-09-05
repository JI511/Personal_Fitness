# ----------------------------------------------------------------------------------------------------------------------
#    Constants
# ----------------------------------------------------------------------------------------------------------------------

# imports
import os


def generate_sets_item_query(names, sets):
    """
    Builds a query with a specified number of sets.

    :param List names: The name of the workout item.
    :param int sets: The number of sets to generate in the query.
    :return: SQL compatible query as a string.
    """
    master_query = []
    for name in names:
        for index in range(sets):
            master_query.append(('%s_set_%s' % (name, index), 'real,'))
            master_query.append(('%s_set_%s_reps' % (name, index), 'integer,'))
    print(master_query)
    return master_query


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

    user_prompt = "Would you like to view data or add a new entry?\n" \
                  "1: New entry\n" \
                  "2: View plots\n" \
                  "3: Dump data to csv\n" \
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

    morning_lifts_query = generate_query(morning_lifts_query_tuple)

    nutrition_query = generate_query(nutrition_query_tuple)

    max_lifts_query = generate_query(max_lifts_query_tuple)

    body_weight_query = generate_query(body_weight_query_tuple)

    weight_lifting_accessories_query = generate_query(weight_lifting_accessories_query_tuple)

    weight_lifting_compound_query = generate_query(generate_sets_item_query(names=['bench_press',
                                                                                   'squat',
                                                                                   'shoulder_press',
                                                                                   'deadlift'],
                                                                            sets=6))

    config_defaults = {
        "OPTIONS": {
            "Water": "oz"
        }
    }



# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
