"""
Get model zip files and metadata from ModelDB.

Robert A. McDougal 2020-05-11 - 2020-07-15

Note: while most models have associated zip files, probably a couple hundred do not.
Those are the "web link to models" (additional information for these models is stored
in the notes -- attribute 24.)

Note: This will only gather zip files on new models.
      To restart, you must delete the contents of zip_dir.
"""

import requests
import json
import base64
import os
from pymongo import MongoClient

try:
    from tqdm import tqdm as progress_bar
except:
    # do nothing "progress bar" if no tqdm
    progress_bar = lambda collection: collection



SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

# filenames
zip_dir = security["modeldb_zip_dir"]

try:
    os.makedirs(zip_dir)
except FileExistsError:
    pass

prev_model_ids = [int(item.split(".")[0]) for item in os.listdir(zip_dir)]

model_ids = [
    item["id"]
    for item in requests.get(
        "https://senselab.med.yale.edu/_site/webapi/object.json/?cl=19"
    ).json()["objects"]
]


models_added = []
for model_id in progress_bar(model_ids):
    # don't reload anything that you already have
    if model_id in prev_model_ids:
        continue

    models_added.append(model_id)
    unprocessed_metadata = requests.get(
        f"https://senselab.med.yale.edu/_site/webapi/object.json/{model_id}"
    ).json()
    metadata = {"title": unprocessed_metadata["object_name"], "id": model_id}
    for item in unprocessed_metadata["object_attribute_values"]:
        if item["attribute_id"] == 23:
            # the zip file
            with open(os.path.join(zip_dir, f"{model_id}.zip"), "wb") as f:
                f.write(base64.standard_b64decode(item["value"]["file_content"]))


mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

# TODO: this pulls the metadata twice. Don't do that

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
    return result


def get_model_metadata(object_id):
    result = get_metadata(object_id)
    if "hg" in result:
        result["gitrepo"] = True
        del result["hg"]
    else:
        result["gitrepo"] = False
    if "more_cells" in result:
        if "neurons" not in result:
            result["neurons"] = result["more_cells"]
        else:
            result["neurons"]["value"] += result["more_cells"]["value"]
        del result["more_cells"]
    return result

for _id in models_added:
    if not list(sdb.models.find({"id": _id})):
        sdb.models.insert_one(get_model_metadata(_id))
        print(f"added model {_id}")
    else:
        print(f"downloaded but already had metadata for {_id}")