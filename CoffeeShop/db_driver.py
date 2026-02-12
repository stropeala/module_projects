import os
import sqlite3

from sql_query_manager import (
    EMPLOYEE_STARTDATE_ROLE,
    EMPLOYEE_TABLE,
    EMPLOYEE_TABLE_COLUMNS,
    MENU_NAME_PRICE,
    MENU_TABLE,
    MENU_TABLE_COLUMNS,
    ORDERS_NAME_QTY_CLIENTID_TIMESTAMP_CASHIERID,
    ORDERS_TABLE,
    ORDERS_TABLE_COLUMNS,
    TEST_DB_PATH,
)


def con_to_db(db_filepath: str) -> sqlite3.Connection:
    try:
        if os.path.isfile(db_filepath):
            con = sqlite3.connect(db_filepath)
            return con
        else:
            print("Path is incorrect!")
            return None  # pyright: ignore
    except sqlite3.OperationalError:
        print("Couldn't connect to database!")
        return None  # pyright: ignore


def read_from_table(db_filepath: str, sql_query: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()


def add_to_table(table_name: str, table_columns: str, table_values: str, input: tuple):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} {table_columns} VALUES {table_values}", input
        )
        return con.commit()


if __name__ == "__main__":
    db_filepath = TEST_DB_PATH

    add_to_table(
        EMPLOYEE_TABLE,
        EMPLOYEE_TABLE_COLUMNS,
        EMPLOYEE_STARTDATE_ROLE,
        ("2025-06-07", "TEST_1"),
    )

    add_to_table(
        MENU_TABLE,
        MENU_TABLE_COLUMNS,
        MENU_NAME_PRICE,
        ("FRIPTURA", "TEST_2"),
    )

    add_to_table(
        ORDERS_TABLE,
        ORDERS_TABLE_COLUMNS,
        ORDERS_NAME_QTY_CLIENTID_TIMESTAMP_CASHIERID,
        ("FRIPTURA", "3", "MARIUSICA BOSSULICA", "2025-06-07 20:45", "TEST_3"),
    )
