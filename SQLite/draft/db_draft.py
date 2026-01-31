import os
import sqlite3

"""
CREATE TABLE "" (
	"ID"	INTEGER UNIQUE,
	"First Name"	TEXT,
	"Last Name"	TEXT,
	"Phone Nr."	NUMERIC UNIQUE,
	"City of residence"	TEXT,
	"Date & Time of entrance"	NUMERIC,
	"Date & Time of exit"	NUMERIC,
	"Pariah"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
"""

PARKING_DB_PATH_DRAFT = "SQLite/draft/data/park_draft.db"
CLIENTS_TABLE = "Clients"


# def create_table(db_path: str) -> None:
#     # Connect to the SQLite database or create it if it doesnt exist
#     conn = sqlite3.connect(db_path)

#     # Create a cursor object to interact with the database
#     cursor = conn.cursor()
#     try:
#         # Drop the PARK_DRAFT table if it already exists for a clean setup
#         cursor.execute("DROP TABLE IF EXISTS PARK_DRAFT")

#         # SQL query to create the table
#         sql = """
#             CREATE TABLE "Clients" (
#            	"ID"	INTEGER UNIQUE,
#            	"First Name"	TEXT,
#            	"Last Name"	TEXT,
#            	"Phone Nr."	NUMERIC UNIQUE,
#            	"City of residence"	TEXT,
#            	"Date & Time of entrance"	NUMERIC,
#            	"Date & Time of exit"	NUMERIC,
#            	"Pariah"	TEXT,
#            	PRIMARY KEY("ID" AUTOINCREMENT)
#             );
#         """

#         # Execute the table creation query
#         cursor.execute(sql)

#         # Close the connections to the database
#         cursor.close()
#         conn.close()
#         print("Success: Table created!")

#     except sqlite3.OperationalError:
#         print("Error: Table already exists!")


def create_table(db_path: str) -> None:
    if os.path.isfile(db_path) is False:
        # Connect to the SQLite database or create it if it doesnt exist
        conn = sqlite3.connect(db_path)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # SQL query to create the table
        sql = """
            CREATE TABLE "Clients" (
           	"ID"	INTEGER UNIQUE,
           	"First Name"	TEXT,
           	"Last Name"	TEXT,
           	"Phone Nr."	NUMERIC UNIQUE,
           	"City of residence"	TEXT,
           	"Date & Time of entrance"	NUMERIC,
           	"Date & Time of exit"	NUMERIC,
           	"Pariah"	TEXT,
           	PRIMARY KEY("ID" AUTOINCREMENT)
            );
        """

        # Execute the table creation query
        cursor.execute(sql)

        # Close the connections to the database
        cursor.close()
        conn.close()

        print("Success: Table created!")

    else:
        print("Error: Table already exists!")


(
    f"INSERT INTO Clients ("
    f"'First_Name', 'Last_Name', "
    f"'Phone_Nr', 'City_of_residence', "
    f"'DateTime_entrance', 'DateTime_exit', "
    f"'Hours_Parked', 'Pariah'"
    f") VALUES ("
    f"'{firstname}', '{lastname}', "
    f"'{phone}', '{city}', "
    f"'{entry}', 'None', "
    f"'None', 'False'"
    f")"
)


if __name__ == "__main__":
    create_table(PARKING_DB_PATH_DRAFT)
