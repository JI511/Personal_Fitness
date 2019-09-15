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
        """
        Gathers user input about which morning lifts were performed.

        :param connection: Connection to the database.
        :return:
        """
        return NotImplementedError

    def get_new_data_from_file(self, connection):
        """
        Appends multiple entries to the database with values read from a file

        :param connection: Connection to the database.
        :return: All values added to the database
        """
        return NotImplementedError

    def view_data(self, connection, column_names=None):
        return NotImplementedError


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
