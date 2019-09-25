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

    def read_config_option(self, section, option):
        """
        Retrieves a specific variable from the config file.

        :param str section: Section to access within the config file.
        :param str option: The value to be taken.
        """
        self.logger.info("Reading config...")
        if option is not None and isinstance(option, str):
            try:
                self.__config.read(self.config_path)
                return self.__config[section][option]
            except KeyError:
                logging.getLogger(__name__).error(
                    "Error, trying to access a field not available in current config file.")
                raise KeyError(str(option))
        else:
            raise NotImplementedError

    def update_config_option(self, section, option, value):
        """
        Updates a config option at the specified section

        :param str section: The section of the config file to access.
        :param str option: The option to be updated.
        :param str value: The value to update option with.
        :return: True if successful, False otherwise.
        :rtype: bool
        """
        success = False
        try:
            if self.__config.has_option(section=section, option=option):
                self.__config.set(section=section,
                                  option=option,
                                  value=value)
                self.__config.write(open(self.config_path, 'w'))
                success = True
            else:
                self.logger.error('Option: %s does not exist in specified section' % option)
        except configparser.NoSectionError as e:
            self.logger.error('Section does not exist in config file, %s' % e)
        return success

    def check_config_file_values(self):
        """
        Checks if a given config contains all the config items in Constants.config_defaults. If a value is not within
        the config file the default Constants value will be added.
        """
        for key in Constants.config_defaults.keys():
            for dict_key in Constants.config_defaults[key]:
                if not self.__config.has_option(section=key, option=dict_key):
                    self.__config.set(section=key, option=dict_key, value=Constants.config_defaults[key][dict_key])
        self.__config.write(open(self.config_path, 'w'))

    def create_backup_database(self):
        """
        Will create a backup database file if there has not been one created since the amount of days ago indicated
        by the config value 'backup_rate'.
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
