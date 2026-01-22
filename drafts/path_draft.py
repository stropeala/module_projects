import pathlib

filepath = "drafts/data/clients_draft.json"


db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/db_draft.json"


print(db_filepath)
