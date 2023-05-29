from pymongo import MongoClient, ReturnDocument
import json
import requests
from pymongo import MongoClient
import tqdm

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"
PIPELINE_SETTINGS_PATH = "/home/bitnami/app-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

with open(PIPELINE_SETTINGS_PATH) as f:
    pipeline_settings = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

all_metadata_list = []

for model in tqdm.tqdm(sdb.models.find()):
    # not doing: 'model_type'
    for kind in ['modeling_application', 'currents', 'species', 'neurotransmitters', 'neurons', 'gene', 'region', 'model_concept', 'receptors']:
        if kind in model:
            try:
                all_metadata_list.extend(item["object_name"] for item in model[kind]["value"])
            except:
                breakpoint()

with open("all_metadata_list.txt", "w") as f:
    f.write("\n".join(all_metadata_list))
