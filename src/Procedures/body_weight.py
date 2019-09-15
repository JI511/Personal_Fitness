# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util.constants import Constants
from src.Util import utilities as util
from src.Procedures.procedure import Procedure


class BodyWeightProcedure(Procedure):
    """
    Class for handling body weight procedures and functions.
    """
    def __init__(self, output_dir=None):
        """
        Setup for body weight procedure.

        :param output_dir: Optional output directory if not the default.
        """
        super(BodyWeightProcedure, self).__init__(table='body_weight',
                                                  output_dir=output_dir,
                                                  query=Constants.body_weight_query,
                                                  logger=logging.getLogger(__name__),
                                                  names=['body_weight'])
        self.logger.info("Body weight tracking and calculations")

    def get_new_data(self, connection):
        """
        Get the input value from the user for body weight procedure.
        """
        new_data = []
        while True:
            self.logger.info('Getting input for new body weight entry.')
            weight_text = input("What did you weigh today?\n")
            if weight_text != 'q':
                try:
                    new_data.append(int(weight_text))
                    self.append_new_entry(connection=connection,
                                          values=new_data,
                                          column_names=self.names)
                    break
                except ValueError:
                    print('Invalid option, please enter a valid number.')
            else:
                self.logger.info("User backed out before new entry added.")
                break
        return new_data, self.names

    def get_new_data_from_file(self, connection):
        """
        Appends multiple entries to the database with values read from a file

        :param connection: Connection to the database.
        :return: All values added to the database
        """
        self.logger.info('Getting multiple values from file')
        weight_text = input("What file would you like to use?\n")
        values = util.read_file_values(file_path=weight_text,
                                       logger=self.logger)
        if values is not None:
            for value in values:
                self.append_new_entry(connection=connection,
                                      values=[value],
                                      column_names=self.names)
        else:
            self.logger.error("Bad path provided, aborting updates")
        return values


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
