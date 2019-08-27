# ----------------------------------------------------------------------------------------------------------------------
#    Procedures Abstract Class
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import utilities as util
from src.Util import database_api as db_api


class Procedures(object):
    """
    Abstract implementation for procedures classes
    """
    def __init__(self, connection, table, query, output_path):
        """


        :param `sqlite3` connection:
        :param table:
        :param query:
        :param output_path:
        """
        self.connection = connection
        self.table = table
        self.query = query
        self.output_path = output_path

    def get_new_data(self):
        raise NotImplementedError

    def view_data(self, column_names=None):
        """

        :param column_names:
        :return:
        """
        # util.plot_data()
        pass

    def append_new_entry(self):
        """
        Gets the required input from the user and appends the new values into the database.
        """
        values, column_names = self.get_new_data()
        unique_id = db_api.add_new_row(self.connection, self.table)
        values.append(unique_id)
        db_api.update_item(self.connection, self.table, tuple(values), column_names)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
