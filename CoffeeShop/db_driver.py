import os
import sqlite3

from sql_query_manager import (
    MENU_ESPRESSO_NEW_PRICE,
    MENU_ESPRESSO_PRICE,
    MENU_TABLE,
    ORDERS_GET_QTY_SUM_GROUP,
    ORDERS_GET_QTY_SUM_SELECT,
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


# Crud
def add_to_table(table_name: str, table_columns: str, table_values: str, input: tuple):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} {table_columns} VALUES {table_values};", input
        )
        return con.commit()


# cRud
def read_from_table(table_select: str, table_name: str, table_read_query: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT {table_select} FROM {table_name} {table_read_query};")
        return cursor.fetchall()


# crUd
def update_table(table_name: str, update: str, where_to_update: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE {table_name} SET {update} WHERE {where_to_update};")
        return con.commit()


# cruD
def delete_from_table() -> None:
    pass


if __name__ == "__main__":
    db_filepath = TEST_DB_PATH

    print(
        read_from_table(
            ORDERS_GET_QTY_SUM_SELECT,
            ORDERS_TABLE,
            ORDERS_GET_QTY_SUM_GROUP,
        )
    )

    add_to_table(
        ORDERS_TABLE,
        ORDERS_TABLE_COLUMNS,
        ORDERS_NAME_QTY_CLIENTID_TIMESTAMP_CASHIERID,
        ("FRIPTURA", "3", "MARIUSICA BOSSULICA", "2025-06-07 20:45", "TEST"),
    )

    update_table(
        MENU_TABLE,
        MENU_ESPRESSO_NEW_PRICE,
        MENU_ESPRESSO_PRICE,
    )
