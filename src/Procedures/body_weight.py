# ----------------------------------------------------------------------------------------------------------------------
#    Body Weight
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Util.constants import Constants
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
                                                  query=Constants.body_weight_query,
                                                  logger=logging.getLogger(__name__),
                                                  names=['body_weight'])
        self.logger.info("Body weight tracking and calculations")

    def get_new_data(self, connection):
        """
        Get the input value from the user for body weight procedure.
        """
        while True:
            self.logger.info('Getting input for new body weight entry.')
            weight_text = input("What did you weigh today?\n")
            try:
                self.append_new_entry(connection=connection,
                                      values=[int(weight_text)],
                                      column_names=self.names)
                return [int(weight_text)], self.names
            except ValueError:
                print('Invalid option, please enter a valid number.')

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
