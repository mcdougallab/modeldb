import requests
import re

import json
import requests
from pymongo import MongoClient

SETTINGS_PATH = '/home/bitnami/modeldb-settings.json'

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security['db_name']]
sdb.authenticate(security['mongodb_user'], security['mongodb_pw'])

icg_by_modeldbid = {}
for kind in range(1, 6):
    data = requests.get(f'https://icg.neurotheory.ox.ac.uk/channels/{kind}').text

    for line in data.split('\n'):
        matches = re.findall(f'/channels/([0-9]+)/([0-9]+)">(.+)-(.+)</a>', line)
        if matches:
            assert(len(matches) == 1)
            my_kind, icg_id, modeldb_id, modeldb_mech = matches[0]
            modeldb_id = int(modeldb_id)
            icg_id = int(icg_id)
            my_kind = int(my_kind)
            icg_by_modeldbid.setdefault(modeldb_id, {})
            icg_by_modeldbid[modeldb_id][modeldb_mech] = {'icg_id': icg_id, 'kind': my_kind}

sdb.drop_collection('icg')
sdb.icg.insert_many([{'id': key, 'data': value} for key, value in icg_by_modeldbid.items()])
print(icg_by_modeldbid)