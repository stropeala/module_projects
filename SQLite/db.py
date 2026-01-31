from datetime import datetime
from os import path
from random import randint

from helpers import (
    create_db,
    timer,
    update_hrs_parked,
    update_pariah,
    write_client,
)


def db(db_path: str, firstname: str, lastname: str, phone: str, city: str) -> None:
    if path.isfile(db_path):
        print("Table already exists, adding data to it!\nContinuing...")
        entry = str(datetime.now())
        write_client(db_path, firstname, lastname, phone, city, entry)
        hours = randint(1, 10)
        exit = timer(hours)
        update_hrs_parked(db_path, exit, hours)
        update_pariah(db_path)

    else:
        create_db(db_path)
        entry = str(datetime.now())
        write_client(db_path, firstname, lastname, phone, city, entry)
        hours = randint(1, 10)
        exit = timer(hours)
        update_hrs_parked(db_path, exit, hours)
        update_pariah(db_path)
