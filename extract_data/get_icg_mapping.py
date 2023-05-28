import requests
import re

import json
import requests
from pymongo import MongoClient

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

data = requests.get("https://icg.neurotheory.ox.ac.uk/api/app/families/").json()
families = [item["id"] for item in data]

icg = {}
for family in families:
    print(f"Processing family {family}")
    chans = requests.get(
        f"https://icg.neurotheory.ox.ac.uk/api/app/families/{family}/"
    ).json()["chans"]
    for channel in chans:
        modeldb_id = channel["id_moddb"]
        icg.setdefault(modeldb_id, {})[channel["name"]] = {
            "icg_id": channel["id"],
            "kind": family,
        }

sdb.drop_collection("icg")
sdb.icg.insert_many([{"id": key, "data": value} for key, value in icg.items()])
