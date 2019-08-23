# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

import sqlite3
import csv
import datetime
import sys
import os
from functools import wraps


class SqlError(Exception):
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
def create_table(db_path, table, query):
    if 'date' in query and 'ID integer' in query:
        if not os.path.isdir(db_path) and db_path[-3:] == '.db':
            with sqlite3.connect(db_path) as con:
                try:
                    con.execute("CREATE TABLE " + table + " (" + query + ");")
                except sqlite3.OperationalError as e:
                    if str(e) != ('table ' + table + " already exists"):
                        raise
        else:
            # print('invalid file path')
            pass
    else:
        pass
        # print('required column names not in query')


@sql_wrapper
def add_new_row(db_path, table):
    """
    Creates a default row with a unique id and appends the current time to the table entry.

    :param db_path: Path to the DB file.
    :param table: Name of the table to access within the db file.
    :return: The unique id as an integer.
    """
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO " + table + " DEFAULT VALUES")
        unique_id = cursor.lastrowid
    update_item(db_path, table, (str(datetime.datetime.now()), unique_id), ["date"])
    return unique_id


@sql_wrapper
def update_item(db_path, table, value_tuple, column_list):
    """

    Note - unique_id needs to be the last value of the value tuple.

    :param db_path: Path to the db file.
    :param table: Name of the table to access within the db file.
    :param value_tuple:
    :param column_list:
    """
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        query = 'Update ' + table + ' SET '
        for name in column_list:
            query = query + name + ' = ? ,'
        query = query[:(len(query) - 1)]
        query = query + ' WHERE ID = ?'
        # print(query)
        cur.execute(query, value_tuple)


@sql_wrapper
def get_all_table_items(db_path, table):
    """
    Gets all rows within specified table.

    Note - Do not call this with a lot of items present within table.

    :param db_path: Path to the DB file.
    :param table: Name of the table to access within the db file.
    """
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM " + table + ";")
        return cursor.fetchall()


@sql_wrapper
def get_table_columns(db_path, table, column_names):
    """
    Gets all column items from the specified table column, or a set amount if count is used.

    :param db_path: Path to the DB file.
    :param String table: Name of table within the DB file.
    :param List column_names: Column names within the database.
    :param int count: Amount of values to gather in descending order of most recent.
    :return: Dictionary of key=column_name and value=gathered values
    """
    value_dict = dict()
    with sqlite3.connect(db_path) as con:
        for column in column_names:
            item_list = list()
            cursor = con.cursor()
            for item in cursor.execute("SELECT " + column + " FROM " + table + ";"):
                item_list.append(item[0])
            value_dict[column] = item_list
        return value_dict


@sql_wrapper
def table_to_csv(db_path, table, output_dir=None):
    """
    Outputs the specified table to a csv file.

    :param db_path: Path to the DB file.
    :param table: Name of table within the DB file.
    :param output_dir: Optional output directory (if different than project root).
    """
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM " + table + ";")
            csv_name = '%s.csv' % table
            if output_dir is not None and os.path.isdir(output_dir):
                csv_name = os.path.join(output_dir, csv_name)
            with open(csv_name.format(table), "w", newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur)
            return csv_name
        except sqlite3.OperationalError as msg:
            if 'no such table' in str(msg):
                print("Error!\nTable: " + table + " does not exist")
            else:
                raise

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
