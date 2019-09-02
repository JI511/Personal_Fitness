# ----------------------------------------------------------------------------------------------------------------------
#    Procedures Abstract Class
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import utilities as util
from src.Util import database_api as db_api
from src.Util import constants


class Procedure(object):
    """
    Abstract implementation for procedures classes
    """
    def __init__(self, table, output_dir, query, logger):
        """
        Setup the abstract procedure variables.

        :param str table: The name of the table within the database.
        :param str output_dir: The path to store any output files created.
        :param str query: The query to use within the specified table.
        """
        output_path = output_dir if output_dir is not None else constants.output_path
        self.table = table
        self.query = query
        self.output_path = output_path
        self.logger = logger

    @staticmethod
    def get_new_data():
        """
        Abstract body for getting user input for a procedure.
        """
        raise NotImplementedError

    def get_new_data_from_file(self):
        """
        Abstract body for getting multiple input values for a procedure via file.
        """
        raise NotImplementedError

    def view_data(self, connection, column_names=None):
        """
        Creates plots for every column in the procedure table. Outputs will be stored in the output_path param.

        :param connection: Connection to the database file.
        :param column_names: Optional param to specify columns desired for plotting.
        """
        columns = db_api.get_columns_in_table(connection, self.table) if column_names is None else column_names
        util.plot_data(connection, self.table, columns, self.output_path)

    def append_new_entry(self, connection):
        """
        Gets the required input from the user and appends the new values into the database.
        """
        values, column_names = self.get_new_data()
        self.logger.info('New data gathered:\n\t names: %s\n\t values: %s' % (column_names, values))
        unique_id = db_api.add_new_row(connection, self.table)
        values.append(unique_id)
        db_api.update_item(connection, self.table, tuple(values), column_names)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
