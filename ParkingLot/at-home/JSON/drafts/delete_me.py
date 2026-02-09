import json
import os
import random


def clients(filepath, nume, prenume, telefon, oras, pariah=False):
    id = random.randint(0, 1000000)

    # We check if the path exists
    if os.path.isfile(filepath) is True:
        with open(filepath, "a") as file:
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
            file.write("\n")

    # If False we write the file
    else:
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
            file.write("\n")


if __name__ == "__main__":
    clients(
        "drafts/data/delete_me.json",
        "Petre",
        "Razvan",
        "0770 420 69",
        "Dr.Tr.Severin",
        True,
    )
    clients(
        "drafts/data/delete_me.json",
        "Alexandra",
        "Sidonia",
        "0770 420 70",
        "Orsova",
        True,
    )
