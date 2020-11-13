# NOTE: this will wipe out meta information thereby corrputing e.g. next accession number
import json
import requests
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

pipeline = mongodb[pipeline_settings["db_name"]]
pipeline.authenticate(pipeline_settings["mongodb_user"], pipeline_settings["mongodb_pw"])

