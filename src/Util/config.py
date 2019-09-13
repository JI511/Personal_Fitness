# ----------------------------------------------------------------------------------------------------------------------
#    Config file util
# ----------------------------------------------------------------------------------------------------------------------

# imports
import configparser
import logging
import os
from src.Util.constants import Constants


class Config(object):
    """
    Functions for creating and reading a config file.

    Notes
    * Config file must be '.ini'
    """
    def __init__(self, logger, output_path):
        """
        Creates a default config file if it does not already exist.
        :param output_path: The path
        """
        self.config_path = 'config.ini'
        self.logger = logger
        self.__config = configparser.ConfigParser()
        if not os.path.exists(output_path):
            # todo, try catch here
            os.mkdir(output_path)
        if not os.path.exists(os.path.join(output_path, self.config_path)):
            self.__config["OPTIONS"] = Constants.config_defaults["OPTIONS"]
            with open(self.config_path, "w") as configfile:
                self.__config.write(configfile)
            configfile.close()
            self.logger.info('Config file created.')

    def read_cfg(self, read_value):
        """
        Retrieves a specific variable from the config file.

        :param str read_value: The value to be taken.
        """
        self.logger.info("Reading config...")
        if read_value is not None and isinstance(read_value, str):
            try:
                self.__config.read(self.config_path)
                return self.__config["OPTIONS"][read_value]
            except KeyError:
                logging.getLogger(__name__).error(
                    "Error, trying to access a field not available in current config file.")
                raise KeyError(str(read_value))
        else:
            raise NotImplementedError


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
