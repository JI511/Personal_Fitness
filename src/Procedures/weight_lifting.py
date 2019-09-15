# ----------------------------------------------------------------------------------------------------------------------
#    Lifting
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util.constants import Constants
from src.Util import constants as const
from src.Procedures.procedure import Procedure


class WeightLiftingProcedure(Procedure):
    """
    Class for handling weight lifting procedures and functions.
    """
    def __init__(self, output_dir=None):
        """
        Setup for weight lifting procedure.

        :param output_dir: Optional output directory if not the default.
        """
        super(WeightLiftingProcedure, self).__init__(table='weight_lifting',
                                                     output_dir=output_dir,
                                                     query=Constants.weight_lifting_compound_query,
                                                     logger=logging.getLogger(__name__),
                                                     names=None)
        self.logger.info("Weight lifting tracking and calculations.")

    def get_new_data(self, connection):
        """
        Adds a new entry into the weight lifting table within the health_database database.

        :param connection: Connection to the database.
        """
        self.logger.info('Getting input for new weight lifting entry.')
        names = self.get_workout_item_names(
            group=self.determine_muscle_group('Which muscle groups did you work today?'))
        while True:
            use_default = input("Would you like to use default values based on current max?\n"
                                "y: yes\n"
                                "n: no\n")
            if use_default == 'y':
                self.append_new_entry(connection=connection,
                                      values=self.get_default_lift_values(names=names),
                                      column_names=names)
                return self.get_default_lift_values(names=names), names
            elif use_default == 'n':
                return NotImplementedError
            print('Please enter a valid option')

    def get_max_lift_updates(self):
        """
        Updates the user selected max lift values by getting input from the user.
        """
        names = self.determine_muscle_group(question_text='Which max values would you like to update?')
        max_lift_names = list()
        if 'bench_press' in names:
            max_lift_names.append('bench_press_max')
        if 'squat' in names:
            max_lift_names.append('squat_max')
        if 'shoulder_press' in names:
            max_lift_names.append('shoulder_press_max')
        if 'deadlift' in names:
            max_lift_names.append('deadlift_max')
        max_lift_values = []
        for row in max_lift_names:
            while True:
                max_text = input(("New " + row + "value:\n").replace("_", " "))
                try:
                    max_update = int(max_text)
                    max_lift_values.append(max_update)
                    break
                except ValueError:
                    print('Invalid literal, please enter a number.')
        return max_lift_values, max_lift_names

    @staticmethod
    def get_default_lift_values(names):
        """
        Get the current program lifting values for the day. This is to speed up input if the user is following
        a program.

        :param names:
        :return: The default values
        """
        values = []
        for i in range(len(names)):
            values.append(i)
        return values

    @staticmethod
    def get_workout_item_names(group):
        """
        Gets the column names for the specified workout group.

        :param List group: The user chosen compound lifts.
        :return: A list of Strings containing the column names to update.
        """
        names = [a[0] for a in const.generate_sets_item_query(names=group,
                                                              sets=6)]
        return names

    @staticmethod
    def determine_muscle_group(question_text=''):
        """
        Gets a binary input from the user to select the chosen compound lifts to update.

        :param str question_text: Question for the user to determine which procedure is asking about compounds.
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
                if result > 0:
                    break
                else:
                    print('Please enter a positive integer value.')
            except ValueError:
                print('Invalid literal, please enter a number.')
        muscle_groups = list()
        if (result & Vars.Bench) == 8:
            muscle_groups.append("bench_press")
        if (result & Vars.Squat) == 4:
            muscle_groups.append("squat")
        if (result & Vars.Shoulder_Press) == 2:
            muscle_groups.append("shoulder_press")
        if (result & Vars.Deadlift) == 1:
            muscle_groups.append("deadlift")
        return muscle_groups

    @staticmethod
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

    def view_data(self, connection, column_names=None):
        return NotImplementedError


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
