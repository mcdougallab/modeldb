import json
import os

try:
    from run_protocols import protocol
except:
    print("try again after you copy over the latest ModelView run_protocols.py")
    import sys

    sys.exit(-1)

from pymongo import MongoClient

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

modelviews = os.listdir("/home/bitnami/modelview-classic")

modelview_updates = {}
for modelview_id, data in protocol.items():
    model_id = int(modelview_id.split("_")[0])
    try:
        old_modelviews = sdb.models.find_one({"id": model_id}).get("modelviews")
    except AttributeError:
        print(f"No model {model_id}")
        continue
    if not old_modelviews:
        if f"{modelview_id}.json" in modelviews:
            print(modelview_id, data.get("variant", "ModelView"))
            modelview_updates.setdefault(model_id, []).append(
                {"name": data.get("variant", "ModelView"), "id": modelview_id}
            )

for model_id, model_modelviews in modelview_updates.items():
    sdb.models.update_one(
        {"id": model_id},
        {
            "$set": {
                "modelviews": {
                    "all": model_modelviews,
                    "default": model_modelviews[0]["id"],
                }
            }
        },
    )
