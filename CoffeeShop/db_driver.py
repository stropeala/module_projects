import os
import sqlite3

from sql_query_manager import (
    DRAFT_DB_PATH,
    EMPLOYEE_TABLE,
    EMPLOYEE_TABLE_COLUMNS,
    MENU_TABLE,
    MENU_TABLE_COLUMNS,
    ORDERS_TABLE,
    ORDERS_TABLE_COLUMNS,
)

db_filepath = DRAFT_DB_PATH


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


def read_from_table(db_filepath: str, sql_query: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()


def add_to_employee(db_filepath: str, sql_query: str, start_date: str, role: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(sql_query, (start_date, role))
        return con.commit()


def add_to_table(table_name: str, columns: str, values: str):
    with con_to_db(db_filepath) as con:
        cursor = con.cursor()
        cursor.execute(f"""
                INSERT INTO {table_name}
                {columns}
                VALUES
                {values}
        """)
        return con.commit()


if __name__ == "__main__":
    add_to_table(
        EMPLOYEE_TABLE,
        EMPLOYEE_TABLE_COLUMNS,
        "('2025-06-07', 'test_1')",
    )

    add_to_table(
        MENU_TABLE,
        MENU_TABLE_COLUMNS,
        "('FRIPTURA', 'test_2')",
    )

    add_to_table(
        ORDERS_TABLE,
        ORDERS_TABLE_COLUMNS,
        "('FRIPTURA', '67', 'MARIUSICA BOSSULICA', '2025-06-07', 'test_3')",
    )
