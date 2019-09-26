# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight test cases
# ----------------------------------------------------------------------------------------------------------------------

# imports
import unittest
import tempfile
import os
import shutil
import logging

from src.Util.config import Config
from src.Util.constants import Constants


class TestConfig(unittest.TestCase):
    """
    Class for testing the body weight procedure.
    """
    def setUp(self):
        """
        Initializes unit test variables.
        """
        self.logs_dir = tempfile.mkdtemp()
        self.file_path = os.path.join(self.logs_dir, 'test_config.ini')
        self.logger = logging.getLogger(__name__)
        self.config = Config(logger=self.logger,
                             output_path=self.logs_dir)
        self.section = 'OPTIONS'
        self.option = 'water'

    def tearDown(self):
        """
        Performs any clean up needed.
        """
        self.connection = None
        if os.path.exists(self.logs_dir):
            shutil.rmtree(self.logs_dir)

    # ------------------------------------------------------------------------------------------------------------------
    # read_config_option tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_read_config_option_nominal(self):
        """
        Checks that the default config file is created properly.
        """
        value = self.config.read_config_option(section=self.section,
                                               option=self.option)
        self.assertEqual(value, "oz")

    def test_read_config_option_bad_option(self):
        """
        Attempts to get a bad value in the config file.
        """
        with self.assertRaises(KeyError) as error:
            self.config.read_config_option(section=self.section,
                                           option="bad")
            self.assertTrue('bad' in error.exception)

    # ------------------------------------------------------------------------------------------------------------------
    # update_config_option tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_update_config_option_nominal(self):
        """
        Updates a config value to be used in the future.
        """
        value = 'mL'
        status = self.config.update_config_option(section=self.section,
                                                  option=self.option,
                                                  value=value)
        self.assertTrue(status)
        water_type = self.config.read_config_option(section=self.section,
                                                    option=self.option)
        self.assertEqual(value, water_type)

    def test_update_config_retain_unique_values(self):
        """
        Updating an option should keep unaffected values the same when rewriting.
        """
        value = 'mL'
        status = self.config.update_config_option(section=self.section,
                                                  option=self.option,
                                                  value=value)
        self.assertTrue(status)
        value = '5'
        status = self.config.update_config_option(section=self.section,
                                                  option='backup_rate',
                                                  value=value)
        self.assertTrue(status)
        water_type = self.config.read_config_option(section=self.section,
                                                    option=self.option)
        backup_rate = self.config.read_config_option(section=self.section,
                                                     option='backup_rate')
        self.assertEqual(water_type, 'mL')
        self.assertEqual(backup_rate, '5')

    def test_update_config_option_bad_section(self):
        """
        Attempts to change a config option with a section that does not exist.
        """
        status = self.config.update_config_option(section='bad',
                                                  option=self.option,
                                                  value='mL')
        self.assertFalse(status)

    def test_update_config_option_bad_option(self):
        """
        Attempts to change a config option that does not exist.
        """
        status = self.config.update_config_option(section=self.section,
                                                  option='bad',
                                                  value='mL')
        self.assertFalse(status)

    # ------------------------------------------------------------------------------------------------------------------
    # check_config_file_values tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_check_config_file_values_nominal(self):
        """
        A new default has been added to a section. Add the default value to an already existing config file. The old
        config values will remain.
        """
        Constants.config_defaults[self.section]['test'] = 'new'
        value = 'mL'
        status = self.config.update_config_option(section=self.section,
                                                  option=self.option,
                                                  value=value)
        self.assertTrue(status)
        self.config.check_config_file_values()
        added_default = self.config.read_config_option(section=self.section,
                                                       option='test')
        self.assertEqual(added_default, 'new')
        old_value = self.config.read_config_option(section=self.section,
                                                   option=self.option)
        self.assertEqual(old_value, 'mL')

    # ------------------------------------------------------------------------------------------------------------------
    # create_backup_database tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_create_backup_database_nominal(self):
        """
        Creates a backup database when no other backups are present
        """
        pass

    def test_create_backup_database_already_exists(self):
        """
        Checks for a backup database file, and sees that one has been created within the backup rate.
        """
        pass

    def test_create_backup_database_needed(self):
        """
        Checks for a backup database file, one does exist, but a new one is needed.
        """
        pass

    def test_create_backup_database_no_backup_db_folder(self):
        """
        Creates the backup_db folder within the cwd if it does not already exist.
        """
        pass

# ------------------------------------------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------------------------------------------
