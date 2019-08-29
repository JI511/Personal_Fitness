# ----------------------------------------------------------------------------------------------------------------------
#    Config file util
# ----------------------------------------------------------------------------------------------------------------------

# imports
import configparser
import pathlib
import logging
import os
from src.Util import constants

config_path = 'config.ini'


def __init_cfg():
    """
    Creates a config file with default values.

    """
    config = configparser.ConfigParser()
    config["OPTIONS"] = constants.config_defaults["OPTIONS"]
    with open(config_path, "w") as configfile:
        config.write(configfile)
    configfile.close()
    logging.getLogger(__name__).info('Config file created.')


def read_cfg():
    """

    """
    if not os.path.exists(constants.output_path):
        os.mkdir(constants.output_path)
    if not pathlib.Path(config_path).exists():
        __init_cfg()
    logging.getLogger(__name__).info("Reading config...")
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        constants.water_option = config["OPTIONS"]["Water"]
    except KeyError:
        logging.getLogger(__name__).error("Error, trying to access a field not available in current config file.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
