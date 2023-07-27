# NOTE: this will wipe out meta information thereby corrputing e.g. next accession number
import json
import requests
from pymongo import MongoClient
import bcrypt

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"
PIPELINE_SETTINGS_PATH = "/home/bitnami/app-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

with open(PIPELINE_SETTINGS_PATH) as f:
    pipeline_settings = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


def get_salted_code(code):
    return bcrypt.hashpw(code.encode("utf8"), bcrypt.gensalt()).decode("utf8")


def set_private_model_rac(model_id, rac):
    model = sdb.private_models.find_one({"id": model_id})
    if model is None:
        raise Exception(f"No such private model: {model_id}")
    sdb.private_models.update_one(
        {"id": model_id}, {"$set": {"data_to_curate.rac": get_salted_code(rac)}}
    )


def set_private_model_rwac(model_id, rwac):
    model = sdb.private_models.find_one({"id": model_id})
    if model is None:
        raise Exception(f"No such private model: {model_id}")
    sdb.private_models.update_one(
        {"id": model_id}, {"$set": {"data_to_curate.rwac": get_salted_code(rwac)}}
    )


# pipeline = mongodb[pipeline_settings["db_name"]]
# pipeline.authenticate(pipeline_settings["mongodb_user"], pipeline_settings["mongodb_pw"])
