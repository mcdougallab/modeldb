import json
import requests

from pymongo import MongoClient

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


"""
Neuromorpho.Org links of the form:
    http://neuromorpho.org/MetaDataResult.jsp?count=3379&summary={%22neuron%22:{%22brain_region_1%22:[%22hippocampus%22],%22brain_region_2%22:[%22CA1%22],%22cell_type_1%22:[%22principal%20cell%22],%22cell_type_2%22:[%22pyramidal%22]},%22ageWeightOperators%22:{},%22ageWeightOperations%22:{}}

NIFSTD links of the form: (note: lowercase curie and remove the colon)
    http://uri.neuinfo.org/nif/nifstd/sao830368389

Neuroelectro links of the form:
    https://neuroelectro.org/neuron/89/

"""


# get links to neuroelectro by querying their API (some also link to neurolex that we can use)
data = requests.get("https://neuroelectro.org/api/1/n/").json()

celltypes = sdb.celltypes


def declare_link(cell_id, resource, resource_identifier):
    celltypes.update_one(
        {"id": cell_id}, {"$set": {f"links.{resource}": resource_identifier}}
    )
    print(celltypes.find_one({"id": cell_id}))


neuroelectro_cells = [obj for obj in data["objects"] if obj["neuron_db_id"] is not None]

for cell in neuroelectro_cells:
    neuroelectro_id = cell["id"]
    modeldb_id = cell["neuron_db_id"]
    nlex_id = cell["nlex_id"]
    declare_link(modeldb_id, "neuroelectro", neuroelectro_id)
    if nlex_id.startswith("sao"):
        declare_link(modeldb_id, "neurolex", nlex_id)


def declare_links(modeldb_id, items):
    for resource, resource_id in items.items():
        declare_link(modeldb_id, resource, resource_id)


# CA1 pyramidal cell
declare_links(
    258,
    {
        "neuromorpho": '{"neuron":{"brain_region_1":["hippocampus"],"brain_region_2":["CA1"],"cell_type_1":["principal cell"],"cell_type_2":["pyramidal"]},"ageWeightOperators":{},"ageWeightOperations":{}}',
    },
)

# CA3 pyramidal cell
declare_links(
    259,
    {
        "neuromorpho": '{"neuron":{"brain_region_1":["hippocampus"],"brain_region_2":["CA3"],"cell_type_1":["principal cell"],"cell_type_2":["pyramidal"]},"ageWeightOperators":{},"ageWeightOperations":{}}',
        "neurolex": "sao383526650",
    },
)
