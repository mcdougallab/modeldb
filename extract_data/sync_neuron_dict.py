from pymongo import MongoClient, ReturnDocument
import json
import requests
from pymongo import MongoClient
from datetime import datetime

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"
PIPELINE_SETTINGS_PATH = "/home/bitnami/app-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

with open(PIPELINE_SETTINGS_PATH) as f:
    pipeline_settings = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

def have_cell_id(my_id):
    return sdb.celltypes.find_one({"id": my_id}) is not None

def sync_neuron_dict():

    for model in sdb.models.find():
        if 'neurons' in model:
            for neuron in model['neurons']['value']:
                if not have_cell_id(neuron['object_id']):
                    sdb.celltypes.insert_one(
                         {'id': neuron['object_id'], 'name': neuron['object_name'], 'created': datetime.now().isoformat(), 'class_id': 18}
                    )

if __name__ == "__main__":
    sync_neuron_dict()
