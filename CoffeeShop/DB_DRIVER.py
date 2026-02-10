import os
import sqlite3

from SQL_QUERY_MANAGER import UPDATE_SOMETHING


def con_to_db(db_filepath: str) -> sqlite3.Connection:
    try:
        if os.path.isfile(db_filepath):
            con = sqlite3.connect(db_filepath)
            return con
        else:
            print("Couldn't connect to database!")
            return None  # pyright: ignore
    except sqlite3.OperationalError:
        print("Couldn't connect to database!")
        return None  # pyright: ignore


def update_table(db_filepath: str, sql_query: str, sql_param: str) -> None:
    con = con_to_db(db_filepath)
    cursor = con.cursor()

    sql = sql_query
    cursor.execute(sql, (sql_param))

    con.commit()
    cursor.close()
    con.close()


update_table("test", UPDATE_SOMETHING, "40")
