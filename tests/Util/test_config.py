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
        value = self.config.read_cfg("Water")
        self.assertEqual(value, "oz")

# ------------------------------------------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------------------------------------------
