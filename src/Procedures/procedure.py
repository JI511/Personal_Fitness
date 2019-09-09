# ----------------------------------------------------------------------------------------------------------------------
#    Procedures Abstract Class
# ----------------------------------------------------------------------------------------------------------------------

# imports
from src.Util import utilities as util
from src.Util import database_api as db_api
from src.Util.constants import Constants


class Procedure(object):
    """
    Abstract implementation for procedures classes
    """
    def __init__(self, table, output_dir, query, logger, names):
        """
        Setup the abstract procedure variables.

        :param str table: The name of the table within the database.
        :param str output_dir: The path to store any output files created.
        :param str query: The query to use within the specified table.
        """
        output_path = output_dir if output_dir is not None else Constants.output_path
        self.table = table
        self.query = query
        self.output_path = output_path
        self.logger = logger
        self.names = names

    def get_new_data(self, connection):
        """
        Abstract body for getting user input for a procedure.

        :param connection: Connection to the database file.
        """
        raise NotImplementedError

    def get_new_data_from_file(self, connection):
        """
        Abstract body for getting multiple input values for a procedure via file.

        :param connection: Connection to the database file.
        """
        while True:
            self.logger.info('Getting multiple values from file')
            weight_text = input("What file would you like to use?\n")
            values = util.read_file_values(weight_text, self.logger)
            if values is not None:
                for value in values:
                    self.append_new_entry(connection, [value], self.names)

    def view_data(self, connection, column_names=None):
        """
        Creates plots for every column in the procedure table. Outputs will be stored in the output_path param.

        :param connection: Connection to the database file.
        :param column_names: Optional param to specify columns desired for plotting.
        """
        try:
            columns = db_api.get_columns_in_table(connection, self.table) if column_names is None else column_names
            column_dict = db_api.get_table_columns_dict(connection, self.table, columns)
            if column_dict is not dict():
                self.logger.info("Creating plots for %s" % self.table)
                util.plot_data(self.table, column_dict, self.output_path)
            else:
                self.logger.error("Error, no columns in the table")
        except db_api.SqlError as msg:
            self.logger.error("Error trying to modify the database,\n%s" % str(msg))

    def append_new_entry(self, connection, values, column_names):
        """
        Gets the required input from the user and appends the new values into the database.
        """
        self.logger.info('New data gathered:\n\t names: %s\n\t values: %s' % (values, column_names))
        unique_id = db_api.add_new_row(connection, self.table)
        values.append(unique_id)
        db_api.update_item(connection, self.table, tuple(values), column_names)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
