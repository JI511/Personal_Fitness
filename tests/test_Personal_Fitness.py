# ----------------------------------------------------------------------------------------------------------------------
#    Personal Fitness unit tests
# ----------------------------------------------------------------------------------------------------------------------


# imports
import unittest
import tempfile
import os
import shutil
import datetime
from src import Personal_Fitness


class TestBodyWeightProcedure(unittest.TestCase):
    """
    Class for testing the body weight procedure.
    """
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.logs_dir, 'backup_db'))
        self.database_name = 'test_database.db'
        self.application = Personal_Fitness.PersonalFitness(
            database_path=os.path.join(self.logs_dir, self.database_name),
            log_name='test_log.log',
            backup_path=self.logs_dir,
            config_path=self.logs_dir
        )
        self.input_values = []

        def mock_input(_):
            """
            Fake input function in order to test input calls in unit tests.
            """
            return self.input_values.pop(0)
        Personal_Fitness.input = mock_input

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.application.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    #    backup db tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_create_backup_db_nominal(self):
        """
        Creates a copy of database file and stores it in the backup_db folder.
        """
        self.input_values = ['5', 'q']
        self.application.run()
        date = datetime.datetime.now().strftime('%m_%d')
        backup_folder = os.path.join(self.logs_dir, 'backup_db')
        path = os.path.join(backup_folder, '%s_%s.db' % (self.database_name[:-3], date))
        self.assertTrue(os.path.exists(path))

    def test_no_backup_folder(self):
        """
        Creates the backup db folder in the cwd if it does not already exist.
        """
        shutil.rmtree(os.path.join(self.logs_dir, 'backup_db'))
        self.input_values = ['5', 'q']
        self.application.run()
        date = datetime.datetime.now().strftime('%m_%d')
        backup_folder = os.path.join(self.logs_dir, 'backup_db')
        path = os.path.join(backup_folder, '%s_%s.db' % (self.database_name[:-3], date))
        self.assertTrue(os.path.exists(path))

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
