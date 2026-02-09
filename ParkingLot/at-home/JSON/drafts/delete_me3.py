import json
import os
import random


def clients(filepath, nume, prenume, telefon, oras, pariah=False):
    id = random.randint(0, 1000000)
    client = {
        "ID": id,
        "Nume": nume,
        "Prenume": prenume,
        "Nr.Telefon": telefon,
        "Oras": oras,
        "Pariah": pariah,
    }

    if os.path.isfile(filepath) is True:
        with open(filepath, "r") as file:
            all_clients = json.load(file)
    else:
        all_clients = []

    all_clients.append(client)

    with open(filepath, "w") as file:
        json.dump(all_clients, file, indent=4)


if __name__ == "__main__":
    clients(
        "drafts/data/delete_me3.json",
        "salut",
        "sunt",
        "un",
        "test",
    )
    clients(
        "drafts/data/delete_me3.json",
        "salut",
        "sunt",
        "al treilea",
        "test",
    )
