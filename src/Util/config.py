# ----------------------------------------------------------------------------------------------------------------------
#    Config file util
# ----------------------------------------------------------------------------------------------------------------------

# imports
import configparser
import pathlib
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


def read_cfg():
    """

    """
    if not pathlib.Path(config_path).exists():
        print("Creating config...")
        __init_cfg()
    print("Reading config...")
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        constants.water_option = config["OPTIONS"]["Water"]
    except KeyError:
        print("Error, trying to access a field not available in current config file.")


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
