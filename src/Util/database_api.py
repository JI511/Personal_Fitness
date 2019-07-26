# ----------------------------------------------------------------------------------------------------------------------
#    Utility functions
# ----------------------------------------------------------------------------------------------------------------------

import sqlite3
from functools import wraps
from . import Constants


def create_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Exception as e:
        print(e)
    return None


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
        con.execute("INSERT INTO " + table + " DEFAULT VALUES")


@sql_wrapper
def get_table_rows(db_path, table):
    with sqlite3.connect(db_path) as con:
        for row in con.execute("SELECT * FROM " + table + ";"):
            print(row)


# ----------------------------------------------------------------------------------------------------------------------
#    End
# ----------------------------------------------------------------------------------------------------------------------
