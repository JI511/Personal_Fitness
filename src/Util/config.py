# ----------------------------------------------------------------------------------------------------------------------
#    Config file util
# ----------------------------------------------------------------------------------------------------------------------

# imports
import configparser
import pathlib
from Util import constants

config_path = 'config.ini'


def __init_cfg():
    """
    Creates a config file with default values.

    """
    config = configparser.ConfigParser()
    config["OPTIONS"] = constants.config_defaults["OPTIONS"]
    with open(config_path, "w") as configfile:
        config.write(configfile)


def read_cfg():
    """

    """
    if not pathlib.Path(config_path).exists():
        __init_cfg()
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        constants.water_option = config["OPTIONS"]["Water"]
        a = config["OPTIONS"]["test"]
    except KeyError:
        print("Error, trying to access a field not available in current config file.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
