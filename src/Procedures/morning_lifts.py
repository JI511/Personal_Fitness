# ----------------------------------------------------------------------------------------------------------------------
#    Morning Lifts
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Procedures.procedure import Procedure
from src.Util import constants


class MorningLiftsProcedure(Procedure):
    """

    """
    def __init__(self):
        """

        """
        super(MorningLiftsProcedure, self).__init__('morning_lifts', constants.output_path,
                                                    constants.morning_lifts_query)

    def get_new_data(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
