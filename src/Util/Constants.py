# ----------------------------------------------------------------------------------------------------------------------
#    Constants
# ----------------------------------------------------------------------------------------------------------------------

database_path = r"C:\Users\User\Desktop\Python\Personal_Fitness\health_database.db"

weight_lifting_query = (
    "ID integer PRIMARY KEY ASC NOT NULL,"
    "date text,"
    "elliptical integer,"
    "bench_press integer,"
    "bench_press_sets_reps text,"
    "squat integer,"
    "squat_sets_reps text,"
    "chin_up integer,"
    "chin_up_sets_reps text,"
    "dips integer,"
    "dips_sets_reps text,"
    "grip_roller real,"
    "grip_roller_sets_reps text,"
    "face_pulls integer,"
    "face_pulls_sets_reps text"
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

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
