# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util import utilities as util
from src.Util import constants
from src.Procedures.procedure import Procedure


class BodyWeightProcedure(Procedure):
    """

    """
    def __init__(self, output_dir=None):
        """
        Setup for body weight procedure.

        :param output_dir: Optional output directory if not the default.
        """
        super(BodyWeightProcedure, self).__init__(table='body_weight',
                                                  output_dir=output_dir,
                                                  query=constants.body_weight_query,
                                                  logger=logging.getLogger(__name__))
        self.logger.info("Body weight tracking and calculations")

    def get_new_data(self):
        """
        Get the input value from the user for body weight procedure.
        """
        while True:
            self.logger.info('Getting input for new body weight entry.')
            weight_text = input("What did you weigh today?\n")
            try:
                return [int(weight_text)], ['body_weight']
            except ValueError:
                print('Invalid option, please enter a valid number.')

    def get_new_data_from_file(self):
        """
        Reads multiple numeric values from a file to update the database.

        :return:
        """
        while True:
            self.logger.info('Getting multiple values from file')
            weight_text = input("What file would you like to use?\n")
            values = util.read_file_values(weight_text, self.logger)
            if values is not None:
                # todo, return all the values, only one column?
                pass

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
