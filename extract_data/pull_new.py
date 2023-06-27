import json
import requests
from pymongo import MongoClient
import os
import base64


try:
    from tqdm import tqdm as progress_bar
except:
    # do nothing "progress bar" if no tqdm
    progress_bar = lambda collection: collection

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

modeldb_models = requests.get(
    "https://senselab.med.yale.edu/_site/webapi/object.json/?cl=19"
).json()["objects"]
modeldb_ids = [item["id"] for item in modeldb_models]


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


alternate_model_ids = [
    item["id"]
    for item in requests.get(
        "https://senselab.med.yale.edu/_site/webapi/object.json/?cl=92"
    ).json()["objects"]
]

models_added = []
for model_id in progress_bar(model_ids + alternate_model_ids):
    # don't reload anything that you already have
    if model_id in prev_model_ids:
        continue

    models_added.append(model_id)
    unprocessed_metadata = requests.get(
        f"https://senselab.med.yale.edu/_site/webapi/object.json/{model_id}"
    ).json()
    metadata = {"title": unprocessed_metadata["object_name"], "id": model_id}
    for item in unprocessed_metadata["object_attribute_values"]:
        if item["attribute_id"] in (23, 311):
            # the zip file
            with open(os.path.join(zip_dir, f"{model_id}.zip"), "wb") as f:
                f.write(base64.standard_b64decode(item["value"]["file_content"]))


def get_metadata(object_id):
    data = requests.get(
        f"https://senselab.med.yale.edu/_site/webapi/object.json/{object_id}?woatts=23"
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


for _id in modeldb_ids:
    if sdb.models.find_one({"id": _id}) is None:
        sdb.models.insert_one(get_model_metadata(_id))
        print(f"added model {_id}")


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
        # skip alternate model source code
        if attr["attribute_id"] != 311:
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


for class_name, class_id in [
    ["alternate_models", 92],
    ["publication_facts", 195],
    ["currents", 17],
    ["papers", 42],
    ["genes", 126],
    ["regions", 144],
    ["receptors", 9],
    ["transmitters", 7],
    ["simenvironments", 36],
    ["modelconcepts", 39],
    ["edges", 125],
    ["modeltypes", 38],
    ["celltypes", 18],
]:
    objects = requests.get(
        "https://senselab.med.yale.edu/_site/webapi/object.json/?cl={}".format(class_id)
    ).json()["objects"]
    existing_ids = set(getattr(sdb, class_name).distinct("id"))
    object_ids = [item["id"] for item in objects if item["id"] not in existing_ids]
    all_objects = {}
    for _id in object_ids:
        while True:
            try:
                all_objects[_id] = get_metadata(_id)
                print(_id, class_name)
                break
            except requests.exceptions.ConnectionError:
                pass

    if all_objects:
        getattr(sdb, class_name).insert_many(all_objects.values())
    import pprint

    pprint.pprint(list(all_objects.values()))
