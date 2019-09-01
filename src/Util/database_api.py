# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

import sqlite3
import csv
import datetime
import sys
import os
import logging
from functools import wraps


class SqlError(BaseException):
    pass


def sql_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            raise SqlError(e)
    return wrapper


@sql_wrapper
def create_connection(db_path):
    """
    Creates a connection to a specified database path.

    :param db_path: The path to the DB file.
    :return: Connection object.
    """
    if not os.path.isdir(db_path) and db_path[-3:] == '.db':
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            return cursor
    else:
        return None


@sql_wrapper
def create_table(con, table, query):
    if 'date' in query and 'ID integer' in query and isinstance(con, sqlite3.Cursor):
        try:
            con.execute("CREATE TABLE " + table + " (" + query + ");")
        except sqlite3.OperationalError as e:
            if str(e) != ('table ' + table + " already exists"):
                raise
    else:
        pass
        logging.getLogger(__name__).error('required column names not in query')


@sql_wrapper
def add_new_row(connection, table):
    """
    Creates a default row with a unique id and appends the current time to the table entry.

    :param connection: Connection to the DB file.
    :param table: Name of the table to access within the db file.
    :return: The unique id as an integer.
    """

    connection.execute("INSERT INTO " + table + " DEFAULT VALUES")
    unique_id = connection.lastrowid
    update_item(connection, table, (str(datetime.datetime.now()), unique_id), ["date"])
    return unique_id


@sql_wrapper
def update_item(connection, table, value_tuple, column_list):
    """

    Note - unique_id needs to be the last value of the value tuple.

    :param connection: Connection to the db file.
    :param table: Name of the table to access within the db file.
    :param value_tuple:
    :param column_list:
    """
    query = 'Update ' + table + ' SET '
    for name in column_list:
        query = query + name + ' = ? ,'
    query = query[:(len(query) - 1)]
    query = query + ' WHERE ID = ?'
    connection.execute(query, value_tuple)


@sql_wrapper
def get_all_table_entries(connection, table):
    """
    Gets all rows within specified table.

    Note - Do not call this with a lot of items present within table.

    :param connection: Connection to the DB file.
    :param table: Name of the table to access within the db file.
    """
    connection.execute("SELECT * FROM " + table + ";")
    return connection.fetchall()


@sql_wrapper
def get_table_columns_dict(connection, table, column_names):
    """
    Gets all column items from the specified table column, or a set amount if count is used.

    :param connection: Connection to the DB file.
    :param String table: Name of table within the DB file.
    :param List column_names: Column names within the database.
    :return: Dictionary of key=column_name and value=gathered values
    """
    value_dict = dict()
    for column in column_names:
        item_list = list()
        for item in connection.execute("SELECT " + column + " FROM " + table + ";"):
            item_list.append(item[0])
        value_dict[column] = item_list
    return value_dict


@sql_wrapper
def get_columns_in_table(connection, table):
    """
    Gets a list of all column names within the specified table.

    :param connection: Connection to the DB file.
    :param table: Table name to get columns from.
    :return: List of column names.
    """
    connection.execute("select * from %s;" % table)
    result = []
    for item in connection.description:
        result.append(item[0])
    result = result[2:]
    return result


def get_table_names(connection):
    """
    Gets all table names in the specified database file.

    :param connection: Connection to the DB file.
    :return: List of table names
    """
    connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = []
    for table in connection.fetchall():
        tables.append(table[0])
    return tables


@sql_wrapper
def table_to_csv(connection, table, output_dir=None):
    """
    Outputs the specified table to a csv file.

    :param connection: Connection to the DB file.
    :param table: Name of table within the DB file.
    :param output_dir: Optional output directory (if different than project root).
    """
    connection.execute("SELECT * FROM " + table + ";")
    csv_name = '%s.csv' % table
    if output_dir is not None and os.path.isdir(output_dir):
        csv_name = os.path.join(output_dir, csv_name)
    with open(csv_name.format(table), "w", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([i[0] for i in connection.description])
        csv_writer.writerows(connection)
    return csv_name

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
