from Util import constants
import configparser

def init_cfg():
    config = configparser.ConfigParser()

    config["DATA"] = constants.config_defaults["DATA"]
    config["VALUES"] = constants.config_defaults["VALUES"]

    with open(r".\Util\config.cfg", "w") as file:
        config.write(file)

def read_cfg():
    config = configparser.ConfigParser()

    try:
        config.read(r".\Util\config.cfg")
        constants.database_path = config["DATA"]["DatabasePath"]
        constants.csv_path = config["DATA"]["CsvPath"]
        constants.logs_path = config["DATA"]["LogsPath"]
    except Exception as e:
        print("problem reading config with exception: {0}".format(e))
        return 0
    return 1
