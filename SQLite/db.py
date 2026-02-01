from datetime import datetime
from os import path
from random import randint

from helpers import (
    create_db,
    timer,
    update_hours_parked,
    update_pariah,
    write_client,
)


def db(db_path: str, firstname: str, lastname: str, phone: str, city: str) -> None:
    # Here we make the main func using all of the funcs we made before together
    # If the db doesnt exist we create one using the create_db() func
    if path.isfile(db_path) is False:
        create_db(db_path)
    else:
        print("Clients table already exists\nAdding client...")

    # Client enters the parking lot
    entry = str(datetime.now())
    # We write the clients data: name, phone, city, entry date
    write_client(db_path, firstname, lastname, phone, city, entry)
    # We simulate the time the client stays parked
    hours = randint(1, 10)
    # The client exits the parking lot
    exit = timer(hours)
    # We update the clients data with the exit date and time
    update_hours_parked(db_path, exit, hours)
    # We update the clients pariah if needed (stayed over 3 days)
    update_pariah(db_path)
