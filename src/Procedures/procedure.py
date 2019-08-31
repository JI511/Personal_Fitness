# ----------------------------------------------------------------------------------------------------------------------
#    Procedures Abstract Class
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import utilities as util
from src.Util import database_api as db_api


class Procedure(object):
    """
    Abstract implementation for procedures classes
    """
    def __init__(self, table, output_path, query):
        """
        Setup the abstract procedure variables.

        :param `str` table: The name of the table within the database.
        :param `str` output_path: The path to store any output files created.
        :param `str` query: The query to use within the specified table.
        """
        self.table = table
        self.query = query
        self.output_path = output_path

    @staticmethod
    def get_new_data():
        raise NotImplementedError

    def view_data(self, connection):
        """
        Creates plots for every column in the procedure table. Outputs will be stored in the output_path param.

        :param connection: Connection to the database file.
        """
        columns = db_api.get_columns_in_table(connection, self.table)
        util.plot_data(connection, self.table, columns, self.output_path)

    def append_new_entry(self, connection):
        """
        Gets the required input from the user and appends the new values into the database.
        """
        values, column_names = self.get_new_data()
        unique_id = db_api.add_new_row(connection, self.table)
        values.append(unique_id)
        db_api.update_item(connection, self.table, tuple(values), column_names)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
