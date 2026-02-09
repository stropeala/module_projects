import json
import os
import pathlib
import re

from db_draft import db_draft


# We create a func that adds a new client to a json file without deleteing the old ones
def clients_draft(filepath, nume, prenume, telefon, oras, pariah=False):
    # We check if the json exists
    if os.path.isfile(filepath) is True:
        # If the json exists we open in read mode
        with open(filepath, "r") as file:
            all_clients = json.load(file)
    # If the json doesn't exist we start with an empty list
    else:
        all_clients = []

    # We create a client dict template
    id = len(all_clients) + 1
    client = {
        "ID": id,
        "Nume": nume,
        "Prenume": prenume,
        "Nr.Telefon": telefon,
        "Oras": oras,
        "Pariah": pariah,
    }

    # We add the new client dict to the all_clients list
    all_clients.append(client)

    # We open the json in write mode and convert the all_clients list to a json
    with open(filepath, "w") as file:
        # indent=4 for better format
        json.dump(all_clients, file, indent=4)

    db_draft(filepath, id)

    db_filepath2 = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_timers_draft.json"
    with open(db_filepath2, "r") as file:
        client_db2 = json.load(file)

    ids = list(range(len(all_clients)))
    for i in ids:
        timp_str = client_db2[i]["Date & Hour"]["Timp"]
        match = re.findall(r"\d", timp_str)
        timp_int = int(match[0])
        if 7 <= timp_int:
            all_clients[i].update({"Pariah": True})

    with open(filepath, "w") as file:
        # indent=4 for better format
        json.dump(all_clients, file, indent=4)
