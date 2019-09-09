# ----------------------------------------------------------------------------------------------------------------------
#    Morning Lifts
# ----------------------------------------------------------------------------------------------------------------------

# imports
import logging
from src.Procedures.procedure import Procedure
from src.Util.constants import Constants


class MorningLiftsProcedure(Procedure):
    """
    Class to handle morning lifts procedures and functions.
    """
    def __init__(self, output_dir=None):
        """
        Setup for morning lifts procedure.
        """
        super(MorningLiftsProcedure, self).__init__(table='morning_lifts',
                                                    output_dir=output_dir,
                                                    query=Constants.morning_lifts_query,
                                                    logger=logging.getLogger(__name__),
                                                    names=None)
        self.logger.info("Morning lifts tracking and procedures.")

    def get_new_data(self, connection):
        pass


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
