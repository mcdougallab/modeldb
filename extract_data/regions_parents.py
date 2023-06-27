# NOTE: assumes regions already pulled
# NOTE: if any of these have parents aleady set, the parents will be replaced
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

# NOTE: this assumes regions have been pulled already
parents = {
    "Vertebrate regions": [
        142628,
        143145,
        144485,
        115952,
        183076,
        115953,
        115947,
        115955,
        119191,
        115946,
        144513,
        151437,
        154751,
        115945,
        115950,
        115949,
        147188,
        115954,
        138633,
        116868,
        118308,
        115951,
        115948,
        228597,
        249414,
        241764,
        266986,
    ],
    "Species": [
        115956,
        116370,
        125736,
        115958,
        115957,
        266967,
        206363,
        234657,
        266968,
        227987,
        262707,
        228598,
        239013,
    ],
    "Invertebrate regions": [115959, 262706, 266649],
    "Miscellaneous": [127711, 115960, 118529, 115962],
}

for parent, children in parents.items():
    for child in children:
        sdb.regions.update_one(
            {"id": child}, {"$set": {"parent": {"object_name": parent}}}
        )

missing_parent = []
for r in sdb.regions.find():
    if "parent" not in r:
        missing_parent.append(r["id"])

if missing_parent:
    print("The following regions are missing parent values:")
    print(missing_parent)
