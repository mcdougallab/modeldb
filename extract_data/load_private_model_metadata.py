import json
from pymongo import MongoClient
import bcrypt


SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"
PIPELINE_SETTINGS_PATH = "/home/bitnami/app-settings.json"
METADATA_PATH = "/home/bitnami/private_model_metadata.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

with open(PIPELINE_SETTINGS_PATH) as f:
    pipeline_settings = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


def get_salted_code(code):
    return bcrypt.hashpw(code.encode("utf8"), bcrypt.gensalt()).decode("utf8")


with open(METADATA_PATH) as f:
    all_metadata = json.load(f)

# loop through everything, hash and relocate any access codes
for model_id, model_metadata in all_metadata.items():
    model_id = int(model_id)
    if sdb.private_models.find_one({"id": model_id}) is None:
        # we're skipping anything that already exists for now
        data_to_curate = model_metadata.get("data_to_curate", {})
        if "rac" in model_metadata:
            rac = get_salted_code(model_metadata["rac"])
            del model_metadata["rac"]
            data_to_curate["rac"] = rac
        if "rwac" in model_metadata:
            rwac = get_salted_code(model_metadata["rwac"])
            del model_metadata["rwac"]
            data_to_curate["rwac"] = rwac
        if data_to_curate:
            model_metadata["data_to_curate"] = data_to_curate
        model_metadata["id"] = model_id
        sdb.private_models.insert_one(model_metadata)
