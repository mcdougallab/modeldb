"""
Usage:

python3 load_obj.py papers 266729 266771

This file need not be used when setting up a system from scratch but it is
convenient for updating specific data items
"""

import sys
import json
import requests
from pymongo import MongoClient

# TODO: replace this with a dictionary lookup
for class_name, class_id in [
    ["publication_facts", 195],
    ["currents", 17],
    ["papers", 42],
    ["genes", 126],
    ["regions", 144],
    ["receptors", 9],
    ["transmitters", 7],
    ["simenvironments", 36],
    ["modelconcepts", 39],
    ["modeltypes", 38],
    ["celltypes", 18],
]:
    if sys.argv[1] == class_name:
        break
else:
    print("unable to find class_id; exiting")
    sys.exit()


object_ids = [int(id_) for id_ in sys.argv[2:]]

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


def get_metadata(object_id):
    data = requests.get(
        "https://senselab.med.yale.edu/_site/webapi/object.json/{}?woatts=23".format(
            object_id
        )
    ).json()
    assert data["object_id"] == object_id
    result = {
        "id": object_id,
        "name": data["object_name"],
        "created": data["object_created"],
        "ver_number": data["object_ver_number"],
        "ver_date": data["object_ver_date"],
        "class_id": data["object_class"]["class_id"],
    }
    for attr in data["object_attribute_values"]:
        if "value" not in attr:
            attr["value"] = attr["values"]
        elif isinstance(attr["value"], dict):
            attr["value"] = [attr["value"]]
        result[attr["attribute_name"]] = {
            "value": attr["value"],
            "attr_id": attr["attribute_id"],
        }
    if result["class_id"] == 18:
        result["links"] = {}
    return result


all_objects = {}
for _id in object_ids:
    while True:
        try:
            all_objects[_id] = get_metadata(_id)
            print(_id, class_name)
            break
        except requests.exceptions.ConnectionError:
            pass

getattr(sdb, class_name).insert_many(all_objects.values())
import pprint

pprint.pprint(list(all_objects.values()))
