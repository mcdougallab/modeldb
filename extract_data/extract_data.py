import json
import requests
from pymongo import MongoClient

SETTINGS_PATH = '/home/bitnami/modeldb-settings.json'

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security['db_name']]
sdb.authenticate(security['mongodb_user'], security['mongodb_pw'])

modeldb_models = requests.get('https://senselab.med.yale.edu/_site/webapi/object.json/?cl=19').json()['objects']
modeldb_ids = [item['id'] for item in modeldb_models]


def get_metadata(object_id):
    data = requests.get('https://senselab.med.yale.edu/_site/webapi/object.json/{}?woatts=23'.format(object_id)).json()
    assert(data['object_id'] == object_id)
    result = {
        'id': object_id,
        'name': data['object_name'],
        'created': data['object_created'],
        'ver_number': data['object_ver_number'],
        'ver_date': data['object_ver_date'],
        'class_id': data['object_class']['class_id']
    }
    for attr in data['object_attribute_values']:
        if 'value' not in attr:
            attr['value'] = attr['values']
        elif isinstance(attr['value'], dict):
            attr['value'] = [attr['value']]
        result[attr['attribute_name']] = {'value': attr['value'], 'attr_id': attr['attribute_id']}
    return result


def get_model_metadata(object_id):
    result = get_metadata(object_id)
    if 'hg' in result:
        result['gitrepo'] = True
        del result['hg']
    else:
        result['gitrepo'] = False
    if 'more_cells' in result:
        if 'neurons' not in result:
            result['neurons'] = result['more_cells']
        else:
            result['neurons']['value'] += result['more_cells']['value']
        del result['more_cells']
    return result

'''
sdb.drop_collection('models')
for _id in modeldb_ids:
    sdb.models.insert_one(get_model_metadata(_id))
    print(f'added model {_id}')
'''







def get_metadata(object_id):
    data = requests.get('https://senselab.med.yale.edu/_site/webapi/object.json/{}?woatts=23'.format(object_id)).json()
    assert(data['object_id'] == object_id)
    result = {
        'id': object_id,
        'name': data['object_name'],
        'created': data['object_created'],
        'ver_number': data['object_ver_number'],
        'ver_date': data['object_ver_date'],
        'class_id': data['object_class']['class_id']
    }
    for attr in data['object_attribute_values']:
        if 'value' not in attr:
            attr['value'] = attr['values']
        elif isinstance(attr['value'], dict):
            attr['value'] = [attr['value']]
        result[attr['attribute_name']] = {'value': attr['value'], 'attr_id': attr['attribute_id']}
    return result

for class_name, class_id in [
        #['publication_facts', 195],
        #['currents', 17],
        ['papers', 42],
        ['genes', 126],
        ['regions', 144],
        ['receptors', 9],
        ['transmitters', 7],
        ['simenvironments', 36],
        ['modelconcepts', 39],
        ['modeltypes', 38],
        ['celltypes', 18]
    ]:

    objects = requests.get('https://senselab.med.yale.edu/_site/webapi/object.json/?cl={}'.format(class_id)).json()['objects']
    object_ids = [item['id'] for item in objects]
    all_objects = {}
    for _id in object_ids:
        while True:
            try:
                all_objects[_id] = get_metadata(_id)
                print(_id, class_name)
                break
            except requests.exceptions.ConnectionError:
                pass

    sdb.drop_collection(class_name)
    getattr(sdb, class_name).insert_many(all_objects.values())
    import pprint
    pprint.pprint(list(all_objects.values()))

