# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

import sqlite3
import csv
import datetime
from functools import wraps
from . import constants


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
    with sqlite3.connect(db_path) as con:
        try:
            con.execute("CREATE TABLE " + table + " (" + query + ");")
        except sqlite3.OperationalError as e:
            if str(e) != ('table ' + table + " already exists"):
                raise


@sql_wrapper
def add_new_row(db_path, table):
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO " + table + " DEFAULT VALUES")
        unique_id = cursor.lastrowid
    update_item(db_path, table, (str(datetime.datetime.now()), unique_id), ["date"])
    return unique_id


@sql_wrapper
def update_item(db_path, table, value_tuple, name_list):
    """

    :param db_path: Path to the db file.
    :param table: Name of the table to access within the db file.
    :param value_tuple:
    :param name_list:
    """
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        query = 'Update ' + table + ' SET '
        for name in name_list:
            query = query + name + ' = ? ,'
        query = query[:(len(query) - 1)]
        query = query + ' WHERE ID = ?'
        # print(query)
        cur.execute(query, value_tuple)


@sql_wrapper
def get_table_rows(db_path, table):
    with sqlite3.connect(db_path) as con:
        for row in con.execute("SELECT * FROM " + table + ";"):
            print(row)


@sql_wrapper
def table_to_csv(db_path, table):
    """
    Outputs the specified table to a csv file.

    :param db_path: Path to the DB file.
    :param table: Name of table within the DB file.
    """
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM " + table + ";")
            with open('{0}.csv'.format(table), "w", newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur)
        except sqlite3.OperationalError as msg:
            if 'no such table' in str(msg):
                print("Error!\nTable: " + table + " does not exist")
            else:
                raise

# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
