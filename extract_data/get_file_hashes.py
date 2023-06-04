import os
import json
import hashlib
import zipfile
import requests
from pymongo import MongoClient

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


class Model:
    def __init__(self, model_id):
        self._model_id = model_id
        self._zip = zipfile.ZipFile(
            os.path.join(
                security["modeldb_zip_dir"],
                f"{model_id}.zip",
            )
        )

    def __getitem__(self, path):
        return self._zip.read(path)

    def file_hash(self, path):
        return hashlib.sha256(self[path]).hexdigest()

    @property
    def filenames(self):
        return self._zip.namelist()

    def all_file_hashes(self):
        # silently drops any bad zip file entries
        result = {}
        for path in self.filenames:
            try:
                result[path] = self.file_hash(path)
            except zipfile.BadZipFile:
                pass
        return result

    def rows(self):
        return [
            {
                "model_id": self._model_id,
                "path": path,
                "basename": os.path.basename(path),
                "hash": hash,
            }
            for path, hash in self.all_file_hashes().items()
        ]


for i, model in enumerate(sdb.models.find()):
    print(f"Processing {i + 1}: {model['id']}")
    if model['id'] == 267116:
        print("  ... skipping for now because of known memory issues")
        continue
    new_data = Model(model["id"]).rows()
    sdb.model_files.delete_many({"model_id": model["id"]})
    sdb.model_files.insert_many(new_data)

sdb.model_files.drop_indexes()
for field_to_index in ["hash", "model_id", "basename"]:
    print(f"Indexing {field_to_index}...")
    sdb.model_files.create_index([(field_to_index, 1)])
