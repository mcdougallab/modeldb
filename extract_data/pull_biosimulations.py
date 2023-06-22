import requests
import re
import json
from pymongo import MongoClient

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"
PIPELINE_SETTINGS_PATH = "/home/bitnami/app-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

with open(PIPELINE_SETTINGS_PATH) as f:
    pipeline_settings = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

data = requests.get(
    "https://raw.githubusercontent.com/biosimulations/biosimulations-modeldb/dev/biosimulations_modeldb/final/status.yml"
).text
models = re.findall("modeldb-(\d+)", data)

for model in models:
    sdb.models.update_one(
        {"id": int(model)}, {"$set": {"biosimulations": {"value": f"modeldb-{model}"}}}
    )
