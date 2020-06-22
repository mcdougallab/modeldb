import json
from pymongo import MongoClient

SETTINGS_PATH = '/home/bitnami/modeldb-settings.json'

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security['db_name']]
sdb.authenticate(security['mongodb_user'], security['mongodb_pw'])


# TODO: parent probably isn't the right term since this implies a
#       hierarchy when we want a web... especially important for cell types
def declare_children(collection_name, relationships):
    collection = getattr(sdb, collection_name)
    for parent, children in relationships.items():
        for child in children:
            collection.update_one({'id': str(child)}, {'$set': {'parent': str(parent)}})

declare_children('currents',
    {
        2396: [243505, 140826, 243, 244, 245, 246, 112843, 112844], # I Calcium
        240: [139267, 252], # I Chloride
        2397: [255, 254, 251, 253], # I Mixed
        2405: [247, 3277, 248, 249, 112841, 250, 127083, 116966, 143445, 88117, 88118, 88215, 243504, 243506, 88212, 167500, 185501], # I Potassium
        2395: [139268, 222730, 241, 242, 88210, 88208] # I Sodium
    }
)


declare_children('transmitters',
    {
        231: [232, 233, 214], # Amino Acids
        237: [227, 226], # gases
        236: [225], # ions
        234: [224, 229, 238, 230, 239], # monoamines
        235: [184582, 228] # peptides
    }
)

declare_children('receptors',
    {
        219: [213, 212, 1361], # amino acid receptors
        213: [202, 203], # Gaba
        212: [205, 210, 207, 206], # Glutamate
        207: [184, 185, 186, 187, 188, 189, 190, 191], # mGluR
        218: [204, 178], # cholinergic receptors
        204: [179, 180, 181, 182, 183], # muscarinic
        2372: [2393, 2375], # gaseous
        2391: [2392], # ion receptors
        211: [215, 223, 217, 216], # monoamine receptors
        215: [192, 195], # adrenergic
        192: [193, 194], # alpha
        223: [196, 197, 225820], # dopamenergic receptors
        217: [2390, 201], # histamine
        216: [198, 199, 200, 208], # serotonin
        2388: [2389], # peptide receptors
        220: [221, 222, 42670] # sensory receptors
    }
)

declare_children('modelconcepts',
    {
        3649: [3541, 3645, 3629], # action potentials
        3639: [169987], # active dendrites
        3543: [3630, 97752, 3634, 185343, 3636, 97751, 3635, 3633, 152968], # activity patterns
        3634: [145886], # oscillations
        3635: [127084], # synchronization
        139148: [185022, 156115], # brain rhythms
        114660: [242018], # connectivity matrix
        84598: [139996], # extracellular fields
        188516: [83535], # memory
        83535: [180821, 83536, 151331, 83538], # learning
        52404: [112854, 112047, 242863, 139270, 239754, 225427, 196196, 243213, 112855, 52405, 231425, 52407, 240955, 52406, 96767, 65417, 112853, 13855], # pathophysiology
        52407: [88213, 88214, 104624], # heart disease
        96767: [138271], # nociception
        65417: [116944], # parkinson's
        140966: [245692, 245690, 245798, 245693, 245691, 245799], # sensory processing
        245691: [245934], # vision
        55277: [144991, 144990], # signaling pathways
        64174: [241168], # synaptic integration
        3643: [3644, 3647], # synaptic plasticity
        3644: [22010, 22011, 22012], # short term synaptic plasticity
        3647: [87578, 118207] # long term synaptic plasticity
    }
)