import requests
import re
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

# TODO: pull from some API
data = [
    {"ModelDB_ID": 151681, "OSB_ID": "miglioreetal14_olfactorybulb3d"},
    {"ModelDB_ID": 143751, "OSB_ID": "vogelsetal2011"},
    {"ModelDB_ID": 187604, "OSB_ID": "nc_ca1"},
    {
        "ModelDB_ID": 102288,
        "OSB_ID": "ca1-oriens-lacunosum-moleculare-lawrence-et-al-2006",
    },
    {
        "ModelDB_ID": 28316,
        "OSB_ID": "ca1-oriens-lacunosum-moleculare-saraga-et-al-2003",
    },
    {"ModelDB_ID": 182843, "OSB_ID": "ca1-pv-fast-firing-cell-ferguson-et-al-2013"},
    {"ModelDB_ID": 182515, "OSB_ID": "ca1-pyr-cell-ferguson-et-al-2014"},
    {"ModelDB_ID": 153280, "OSB_ID": "nc_superdeep"},
    {"ModelDB_ID": 101629, "OSB_ID": "ca3-pyramidal-cell"},
    {"ModelDB_ID": 51781, "OSB_ID": "dentategyrus2005"},
    {"ModelDB_ID": 124291, "OSB_ID": "dentate-gyrus-granule-cell"},
    {"ModelDB_ID": 124513, "OSB_ID": "dentate"},
    {"ModelDB_ID": 140789, "OSB_ID": "norenbergetal2010_dgbasketcell"},
    {"ModelDB_ID": 140249, "OSB_ID": "dlgninterneuronhalnesetal2011"},
    {"ModelDB_ID": 152028, "OSB_ID": "drosophila-acc-l3-motoneuron-gunay-et-al-2014"},
    {"ModelDB_ID": 151825, "OSB_ID": "almog-korngreen-pyramidal-neuron"},
    {"ModelDB_ID": 114655, "OSB_ID": "weileretal08-laminarcortex"},
    {
        "ModelDB_ID": 156072,
        "OSB_ID": "large-scale-model-of-neocortical-slice-in-vitro-exhibiting-persistent-gamma",
    },
    {"ModelDB_ID": 116835, "OSB_ID": "multicompgrc"},
    {
        "ModelDB_ID": 150284,
        "OSB_ID": "multiscale-medium-spiny-neuron-mattioni-and-le-novere",
    },
    {
        "ModelDB_ID": 146030,
        "OSB_ID": "olfactory-bulb-network-model-o-connor-angelo-and-jacob-2012",
    },
    {"ModelDB_ID": 225301, "OSB_ID": "specnet-sade-et-al-2015"},
    {"ModelDB_ID": 124043, "OSB_ID": "larkumetal2009"},
    {"ModelDB_ID": 118662, "OSB_ID": "drosophila_projection_neuron"},
    {"ModelDB_ID": 139653, "OSB_ID": "l5bpyrcellhayetal2011"},
    {"ModelDB_ID": 123623, "OSB_ID": "pospischiletal2008"},
    {"ModelDB_ID": 55035, "OSB_ID": "ca1pyramidalcell"},
    {"ModelDB_ID": 136175, "OSB_ID": "cerebellarnucleusneuron"},
    {"ModelDB_ID": 35358, "OSB_ID": "pinskyrinzelmodel"},
    {"ModelDB_ID": 126466, "OSB_ID": "destexhe_jcns_2009"},
    {"ModelDB_ID": 39948, "OSB_ID": "izhikevichmodel"},
    {"ModelDB_ID": 8210, "OSB_ID": "mainenetalpyramidalcell"},
    {"ModelDB_ID": 7176, "OSB_ID": "purkinjecell"},
    {"ModelDB_ID": 114394, "OSB_ID": "rothmanetalkoleetalpyrcell"},
    {"ModelDB_ID": 144416, "OSB_ID": "cerebellargainandtiming"},
    {
        "ModelDB_ID": 112685,
        "OSB_ID": "cerebellum--cerebellar-golgi-cell--solinasetal-golgicell",
    },
    {"ModelDB_ID": 42020, "OSB_ID": "brunel2000"},
    {"ModelDB_ID": 45539, "OSB_ID": "thalamocortical"},
    {"ModelDB_ID": 127996, "OSB_ID": "vervaekeetalgolgicellnetwork"},
    {"ModelDB_ID": 141273, "OSB_ID": "vierlingclaassenetal2010"},
    {"ModelDB_ID": 26997, "OSB_ID": "wangbuzsaki1996"},
]

for item in data:
    sdb.models.update_one(
        {"id": item["ModelDB_ID"]},
        {"$set": {"opensourcebrain": {"value": item["OSB_ID"]}}},
    )
