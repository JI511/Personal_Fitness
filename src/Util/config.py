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

        :param logger: An instance of logging.
        :param output_path: The directory to store a config file.
        """
        self.config_name = 'config.ini'
        self.config_path = os.path.join(output_path, self.config_name)
        self.logger = logger
        self.__config = configparser.ConfigParser()
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        if not os.path.exists(os.path.join(output_path, self.config_name)):
            for key in Constants.config_defaults.keys():
                self.__config[key] = Constants.config_defaults[key]
            with open(self.config_path, "w") as configfile:
                self.__config.write(configfile)
            configfile.close()
            self.logger.info('Config file created.')

    def read_cfg(self, section, option):
        """
        Retrieves a specific variable from the config file.

        :param str section: Section to access within the config file.
        :param str option: The value to be taken.
        """
        self.logger.info("Reading config...")
        if option is not None and isinstance(option, str):
            try:
                self.__config.read(self.config_name)
                return self.__config[section][option]
            except KeyError:
                logging.getLogger(__name__).error(
                    "Error, trying to access a field not available in current config file.")
                raise KeyError(str(option))
        else:
            raise NotImplementedError

    def check_config_file_values(self):
        """
        Checks if a given config contains all the config items in Constants.config_defaults. If a value is not within
        the config file the default Constants value will be added.
        """
        for key in Constants.config_defaults.keys():
            for dict_key in Constants.config_defaults[key]:
                if self.__config.has_option(section=key, option=dict_key):
                    Constants.config_defaults[key][dict_key] = self.read_cfg(section=key, option=dict_key)
            self.__config.remove_section(key)
            self.__config.write(Constants.config_defaults[key])


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
