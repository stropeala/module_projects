import sqlite3
from datetime import datetime
from os import path
from re import findall
from time import sleep


def create_db(db_path: str) -> None:
    # Connect to the SQLite database or create it if it doesnt exist
    conn = sqlite3.connect(db_path)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # SQL query to create the table
    sql = """
        CREATE TABLE "Clients" (
       	"ID"	INTEGER UNIQUE,
       	"First_Name"	TEXT,
       	"Last_Name"	TEXT,
       	"Phone_Nr"	NUMERIC UNIQUE,
       	"City_of_Residence"	TEXT,
       	"DateTime_entrance"	NUMERIC,
       	"DateTime_exit"	NUMERIC,
        "Hours_Parked" NUMERIC,
       	"Pariah"	TEXT,
       	PRIMARY KEY("ID" AUTOINCREMENT)
        );
    """

    # Execute the table creation query
    cursor.execute(sql)

    # Close the connections to the database after commiting the change
    conn.commit()
    cursor.close()
    conn.close()
    print("Clients table created\nAdding client...")


def get_conn(db_path: str) -> sqlite3.Connection:
    # We get connection to db only if db_path is valid
    # Then we return the connection so we can use it in other funcs
    if path.isfile(db_path):
        conn = sqlite3.connect(db_path)
        return conn
    else:
        print("Couldn't connect to database!")
        return None  # pyright: ignore


def write_client(
    db_path: str,
    firstname: str,
    lastname: str,
    phone: str,
    city: str,
    entry: str,
) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        # We make a query for writing a client into the table
        sql = f"""
            INSERT INTO Clients
            ('First_Name', 'Last_Name', 'Phone_Nr','City_of_residence',
            'DateTime_entrance', 'DateTime_exit','Hours_Parked', 'Pariah')
            VALUES
            ('{firstname}', '{lastname}', '{phone}', '{city}',
            '{entry}', 'None', 'None', 'False')
        """

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def timer(hours: int) -> str:
    # Here we make a simple timer func
    # that counts every second until 0
    t = hours
    while t:
        sleep(1)
        t -= 1
    exit = str(datetime.now())
    return exit


def update_hours_parked(db_path: str, exit: str, hours: int) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        # Here we update the time with the exit from the previous timer() func
        sql1 = f"UPDATE Clients SET DateTime_exit='{exit}' WHERE DateTime_exit='None'"
        cursor.execute(sql1)

        # Here we update the hours with the var from the main db() func
        sql2 = f"UPDATE Clients SET Hours_Parked='{hours}' WHERE Hours_Parked='None'"
        cursor.execute(sql2)

        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def update_pariah(db_path: str) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        # Here we chage the Pariah from False to True for clients
        # who stayed more than 7 seconds (3 days)
        sql = "UPDATE Clients SET Pariah='True' WHERE Hours_Parked >= 7"
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def create_extra_table(db_path: str) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        # Here we create a new tables in the DB using the data from the Clients table
        # 1st with clients who stayed under 3 seconds (<2 hours)
        sql1 = """
            CREATE TABLE Under_2Hours AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked <= 3;
        """
        cursor.execute(sql1)

        # 2nd with clients who stayed between 3 and 7 seconds (>2 hours)
        sql2 = """
            CREATE TABLE Over_2Hours AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked > 3 AND Hours_Parked < 7;
        """
        cursor.execute(sql2)

        # 3rd with clients who stayed more than 7 seconds (>3 days)
        sql3 = """
            CREATE TABLE Over_3Days AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked >= 7;
        """
        cursor.execute(sql3)

        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def read_and_write_extra_tables(db_path: str) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        # Here we read the tables and make lists with the data we need using fetchall()
        # 1st list we select the clients who stayed under 3 seconds
        sql1 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) <= 3;
        """
        cursor.execute(sql1)
        id = findall(r"\d+", str(cursor.fetchall()))
        print(
            f"\nClient IDs parked under 2 hours: {id}\nExtra table created: Under_2Hours\n"
        )

        # 2nd list we select the clients who stayed between 3 and 7 seconds (>2 hours)
        sql2 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) > 3 AND max(Hours_Parked) < 7;
        """
        cursor.execute(sql2)
        id2 = findall(r"\d+", str(cursor.fetchall()))
        print(
            f"\nClient IDs parked over 2 hours: {id2}\nExtra table created: Over_2Hours\n"
        )

        # 3rd list we select the clients who stayed more than 7 seconds (>3 days)
        sql3 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) >= 7;
        """
        cursor.execute(sql3)
        id3 = findall(r"\d+", str(cursor.fetchall()))
        print(
            f"\nClient IDs parked for 3 days: {id3}\nExtra table created: Over_3Days\n"
        )

        conn.commit()
        cursor.close()
        conn.close()

        # Here we call the previous create_extra_table() so we can
        # with a single read_and_write_extra_tables() both read and write the new tables
        create_extra_table(db_path)
    else:
        print("Couldn't connect to database!")
