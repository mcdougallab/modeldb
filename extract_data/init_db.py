# NOTE: this will wipe out meta information thereby corrputing e.g. next accession number
import json
import requests
from pymongo import MongoClient

SETTINGS_PATH = '/home/bitnami/modeldb-settings.json'

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security['db_name']]
sdb.authenticate(security['mongodb_user'], security['mongodb_pw'])

sdb.drop_collection('meta')
sdb.meta.insert_one({
    'id_count': 2000000
})