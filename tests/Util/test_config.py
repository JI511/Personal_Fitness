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
    # read_cfg tests
    # ------------------------------------------------------------------------------------------------------------------
    def test_read_cfg(self):
        """
        Checks that the default config file is created properly.
        """
        value = self.config.read_cfg(section="OPTIONS",
                                     option="Water")
        self.assertEqual(value, "oz")

    def test_read_cfg_bad_option(self):
        """
        Attempts to get a bad value in the config file.
        """
        with self.assertRaises(KeyError) as error:
            self.config.read_cfg(section="OPTIONS",
                                 option="bad")
            self.assertTrue('bad' in error.exception)

    def test_update_config_option_nominal(self):
        """
        Updates a config value to be used in the future.
        """
        value = 'mL'
        status = self.config.update_config_option(section=self.section,
                                                  option=self.option,
                                                  value=value)
        self.assertTrue(status)
        water_type = self.config.read_cfg(section=self.section,
                                          option=self.option)
        self.assertEqual(value, water_type)

    def test_update_config_retain_unique(self):
        """
        Updating an option should keep unaffected values the same when rewriting.
        """
        pass

    def test_change_config_option_bad_section(self):
        """
        Attempts to change a config option with a section that does not exist.
        """
        pass

    def test_change_config_option_bad_option(self):
        """
        Attempts to change a config option that does not exist.
        """

    def test_add_missing_config_option_value(self):
        """
        A new default has been added to a section. Add the default value to an already existing config file. The old
        config values will remain.
        """
        pass

# ------------------------------------------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------------------------------------------
