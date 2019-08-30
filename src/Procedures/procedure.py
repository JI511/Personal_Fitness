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
    def __init__(self, connection, table, output_path, query=None):
        """
        Setup the abstract procedure variables.

        :param `sqlite3` connection: The connection object to an sqlite3 database.
        :param `str` table: The name of the table within the database.
        :param `str` output_path: The path to store any output files created.
        :param `str` query: The query to use within the specified table.
        """
        self.connection = connection
        self.table = table
        self.query = query
        self.output_path = output_path

    @staticmethod
    def get_new_data():
        raise NotImplementedError

    def view_data(self):
        """

        :return:
        """
        columns = db_api.get_columns_in_table(self.connection, self.table)
        util.plot_data(self.connection, self.table, columns, self.output_path)
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
