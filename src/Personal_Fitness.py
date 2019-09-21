# ----------------------------------------------------------------------------------------------------------------------
# Personal Fitness Application
#
# Store and track progress for multiple different fitness areas.
# Current plans are body weight, calories, morning lifts and lifted weights.
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
import shutil
import os
import datetime
from src.Procedures.nutrition import NutritionProcedure
from src.Procedures.weight_lifting import WeightLiftingProcedure
from src.Procedures.body_weight import BodyWeightProcedure
from src.Procedures.morning_lifts import MorningLiftsProcedure
from src.Util import database_api as db_api
from src.Util.constants import Constants
from src.Util.config import Config


class PersonalFitness(object):
    """
    Application to keep track of multiple fitness procedures.
    """
    def __init__(self, database_path=None, log_name='application_log.log', backup_path=os.getcwd()):
        """
        Setup for application.

        :param str database_path: Optional database location if not default.
        :param str log_name: Optional name for log file.
        :param str backup_path: Path to output the backup database file.
        """
        self.database_path = database_path if database_path is not None else Constants.database_path
        self.connection = db_api.create_connection(db_path=self.database_path)
        self.procedure = None
        self.procedure_prompt_text = None
        self.backup_path = backup_path
        logging.basicConfig(filename=log_name, level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run(self):
        """
        Starts the application.
        """
        self.logger.info("Starting Fitness Application...")
        config = Config(logger=self.logger,
                        output_path=Constants.output_path)
        config.read_cfg("Water")

        while True:
            procedure_text = input(
                "Which application would you like to run?\n"
                "1: Body Weight\n"
                "2: Nutrition\n"
                "3: Weight Lifting\n"
                "4: Morning Lifts\n"
                "5: Create backup database file\n"
                "q: Quit\n")
            if procedure_text == '1':
                self.procedure = BodyWeightProcedure()
            elif procedure_text == '2':
                self.procedure = NutritionProcedure()
            elif procedure_text == '3':
                self.procedure = WeightLiftingProcedure()
                self.procedure_prompt_text = "Would you like to view data or add a new entry?\n"\
                                             "1: New entry\n"\
                                             "2: Multiple entries via file\n"\
                                             "3: View data\n"\
                                             "4: Dump data to CSV\n"\
                                             "5: Update max lift values\n"\
                                             "q: Return to title\n"
            elif procedure_text == '4':
                self.procedure = MorningLiftsProcedure()
            if self.procedure is not None:
                self.logger.info('Procedure chosen: %s' % self.procedure)
                self.__run_procedure()
                self.procedure = None
            elif procedure_text == '5':
                backup_folder = os.path.join(self.backup_path, 'backup_db')
                if not os.path.exists(backup_folder):
                    self.logger.info("Backup folder created.")
                    os.mkdir(backup_folder)
                db_name = os.path.split(self.database_path)[-1][:-3]
                path = os.path.join(backup_folder, '%s_%s.db' % (
                    db_name, datetime.datetime.now().strftime('%m_%d')))
                shutil.copy(self.database_path, path)
                self.logger.info("backup database file created: %s" % path)
            elif procedure_text.lower() == 'q':
                print("Goodbye.")
                break
            else:
                print("No valid option entered.")
        self.connection = None

    def __run_procedure(self):
        """
        Performs procedure operations.
        """
        prompt = self.procedure_prompt_text if self.procedure_prompt_text is not None else Constants.user_prompt
        while True:
            input_text = input(prompt)
            if input_text == '1':
                self.logger.info('Adding a new entry with user entry')
                db_api.create_table(connection=self.connection,
                                    table=self.procedure.table,
                                    query=self.procedure.query)
                self.procedure.get_new_data(connection=self.connection)
            elif input_text == '2':
                self.logger.info('Adding new entries from file')
                db_api.create_table(connection=self.connection,
                                    table=self.procedure.table,
                                    query=self.procedure.query)
                self.procedure.get_new_data_from_file(connection=self.connection)
            elif input_text == '3':
                self.logger.info("Creating plots for user")
                self.procedure.view_data(connection=self.connection)
                pass
            elif input_text == '4':
                self.logger.info("Dumping tables to csv files")
                db_api.table_to_csv(connection=self.connection,
                                    table=self.procedure.table)
            elif input_text == '5':
                if isinstance(self.procedure, WeightLiftingProcedure):
                    self.procedure.get_max_lift_updates()
                print("Please enter a valid option.")
            elif input_text == 'q':
                break
            else:
                print("Please enter a valid option.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
