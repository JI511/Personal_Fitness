# ----------------------------------------------------------------------------------------------------------------------
#    Lifting
# ----------------------------------------------------------------------------------------------------------------------


def determine_muscle_group():
    while True:
        groups = input("Which muscle groups did you work today? (Binary Entry)\n"
                       "8: Bench\n"
                       "4: Squat\n"
                       "2: Shoulder Press\n"
                       "1: Deadlift\n")
        accessories = input("Would you life to use default accessories?\n"
                            "y: yes\n"
                            "n: no\n")
        try:
            result = int(groups)
            break
        except ValueError:
            print('Invalid literal, please enter a number.')
    muscle_groups = list()
    if (result & Vars.Bench) == 8:
        muscle_groups.append("Bench")
    if (result & Vars.Squat) == 4:
        muscle_groups.append("Squat")
    if (result & Vars.Shoulder_Press) == 2:
        muscle_groups.append("Shoulder")
    if (result & Vars.Deadlift) == 1:
        muscle_groups.append("Deadlift")
    print(muscle_groups)


class Vars(object):
    Bench = 8
    Squat = 4
    Shoulder_Press = 2
    Deadlift = 1


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
