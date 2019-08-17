# ----------------------------------------------------------------------------------------------------------------------
#    Constants
# ----------------------------------------------------------------------------------------------------------------------

database_path = ""
csv_path = ""
logs_path = ""


user_prompt = "Would you like to view data or add a new entry?\n"\
              "1: New entry\n"\
              "2: View plots\n"\
              "3: Dump data to csv\n"\

weight_lifting_compound_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "bench_press_set_one integer,"
    "bench_press_set_one_reps integer,"
    "bench_press_set_two integer,"
    "bench_press_set_two_reps integer,"
    "bench_press_set_three integer,"
    "bench_press_set_three_reps integer,"
    "bench_press_set_four integer,"
    "bench_press_set_four_reps integer,"
    "bench_press_set_five integer,"
    "bench_press_set_five_reps integer,"
    "bench_press_set_six integer,"
    "bench_press_set_six_reps integer,"
    "squat_set_one integer,"
    "squat_set_one_reps integer,"
    "squat_set_two integer,"
    "squat_set_two_reps integer,"
    "squat_set_three integer,"
    "squat_set_three_reps integer,"
    "squat_set_four integer,"
    "squat_set_four_reps integer,"
    "squat_set_five integer,"
    "squat_set_five_reps integer,"
    "squat_set_six integer,"
    "squat_set_six_reps integer,"
    "shoulder_press_set_one integer,"
    "shoulder_press_set_one_reps integer,"
    "shoulder_press_set_two integer,"
    "shoulder_press_set_two_reps integer,"
    "shoulder_press_set_three integer,"
    "shoulder_press_set_three_reps integer,"
    "shoulder_press_set_four integer,"
    "shoulder_press_set_four_reps integer,"
    "shoulder_press_set_five integer,"
    "shoulder_press_set_five_reps integer,"
    "shoulder_press_set_six integer,"
    "shoulder_press_set_six_reps integer,"
    "deadlift_set_one integer,"
    "deadlift_set_one_reps integer,"
    "deadlift_set_two integer,"
    "deadlift_set_two_reps integer,"
    "deadlift_set_three integer,"
    "deadlift_set_three_reps integer,"
    "deadlift_set_four integer,"
    "deadlift_set_four_reps integer,"
    "deadlift_set_five integer,"
    "deadlift_set_five_reps integer,"
    "deadlift_set_six integer,"
    "deadlift_set_six_reps integer"
)

weight_lifting_bench_press = [
    "bench_press_set_one",
    "bench_press_set_one_reps",
    "bench_press_set_two",
    "bench_press_set_two_reps",
    "bench_press_set_three",
    "bench_press_set_three_reps",
    "bench_press_set_four",
    "bench_press_set_four_reps",
    "bench_press_set_five",
    "bench_press_set_five_reps",
    "bench_press_set_six",
    "bench_press_set_six_reps"
]

weight_lifting_squats = [
    "squat_set_one",
    "squat_set_one_reps",
    "squat_set_two",
    "squat_set_two_reps",
    "squat_set_three",
    "squat_set_three_reps",
    "squat_set_four",
    "squat_set_four_reps",
    "squat_set_five",
    "squat_set_five_reps",
    "squat_set_six",
    "squat_set_six_reps"
]

weight_lifting_shoulder_press = [
    "shoulder_press_set_one",
    "shoulder_press_set_one_reps",
    "shoulder_press_set_two",
    "shoulder_press_set_two_reps",
    "shoulder_press_set_three",
    "shoulder_press_set_three_reps",
    "shoulder_press_set_four",
    "shoulder_press_set_four_reps",
    "shoulder_press_set_five",
    "shoulder_press_set_five_reps",
    "shoulder_press_set_six",
    "shoulder_press_set_six_reps"
]

weight_lifting_deadlift = [
    "deadlift_set_one",
    "deadlift_set_one_reps",
    "deadlift_set_two",
    "deadlift_set_two_reps",
    "deadlift_set_three",
    "deadlift_set_three_reps",
    "deadlift_set_four",
    "deadlift_set_four_reps",
    "deadlift_set_five",
    "deadlift_set_five_reps",
    "deadlift_set_six",
    "deadlift_set_six_reps"
]

weight_lifting_accessories_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "elliptical integer,"
    "chin_up integer,"
    "chin_up_sets_reps text,"
    "dips integer,"
    "dips_sets_reps text,"
    "grip_roller real,"
    "grip_roller_sets_reps text,"
    "face_pulls integer,"
    "face_pulls_sets_reps text"
)

body_weight_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "body_weight integer"
)

max_lifts_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "bench_press_max integer,"
    "squat_max integer,"
    "shoulder_press_max integer,"
    "deadlift_max integer"
)

morning_lifts_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "shoulder_lateral_raise text,"
    "shoulder_front_raises text,"
    "shoulder_arnold_press text,"
    "bicep_hammer_curl text,"
    "bicep_curl text,"
    "legs_dumbbell_squat text,"
    "abs_ab_roller text,"
    "abs_ab_shrugs text"
)

nutrition_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "calories integer,"
    "protein integer,"
    "carbohydrates integer,"
    "fat integer,"
    "water integer"
)


config_defaults = { 
    "DATA" : {
        "DatabasePath" : r"..\data\health_database.db",
        "CsvPath" : r"..\data\csv",
        "LogsPath" : r"..\data\logs.txt"
        },

    "VALUES" : {
        "Water" : "oz"
    }
}

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
