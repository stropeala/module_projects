import json
import random


def clients(filepath, nume, prenume, telefon, oras, pariah=False):
    id = random.randint(0, 1000000)
    with open(filepath, "w") as file:
        # If True we add a new client
        client = {
            "ID": id,
            "Nume": nume,
            "Prenume": prenume,
            "Nr.Telefon": telefon,
            "Oras": oras,
            "Pariah": pariah,
        }
        json.dump(client, file, indent=4)


if __name__ == "__main__":
    clients(
        "drafts/data/delete_me2.json",
        "salut",
        "sunt",
        "un",
        "test",
    )
    clients(
        "drafts/data/delete_me2.json",
        "salut",
        "sunt",
        "al doilea",
        "test",
    )
