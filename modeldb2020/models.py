import json
from pymongo import MongoClient
from django.db import models
from . import settings

mongodb = MongoClient()
sdb = mongodb[settings.security['db_name']]
sdb.authenticate(settings.security['mongodb_user'], settings.security['mongodb_pw'])

def load_collection(name):
    new_collection = {item['id']: item for item in getattr(sdb, name).find()}
    # expand parent data (if any) into reciprocal parent-child data
    for item in new_collection.values():
        if 'parent' in item:
            new_collection[item['parent']].setdefault('children', [])
            new_collection[item['parent']]['children'].append(item['id'])
    return new_collection


def refresh():
    global modeldb, currents, genes, regions, receptors
    global transmitters, simenvironments, modelconcepts
    global modeltypes, celltypes, papers

    modeldb = load_collection('models')
    currents = load_collection('currents')
    genes = load_collection('genes')
    regions = load_collection('regions')
    receptors = load_collection('receptors')
    transmitters = load_collection('transmitters')
    simenvironments = load_collection('simenvironments')
    modelconcepts = load_collection('modelconcepts')
    modeltypes = load_collection('modeltypes')
    celltypes = load_collection('celltypes')
    papers = load_collection('papers')

class ModelDB(models.Model):
    class Meta:
        app_label = 'modeldb2020',
        permissions = [
            ('can_admin', 'Can do admin'),
            ('can_pipeline', 'Can use pipeline')
        ]
    
    def get_models(self):
        return modeldb

    def __getitem__(self, name):
        return getattr(self, name)

    @property
    def num_models(self):
        return len(modeldb)
    
    def models_by_name(self):
        return sorted([{'id': key, 'name': model['name']} for key, model in modeldb.items()], key=lambda item: item['name'])




class SenseLabClass:
    def __init__(self, _id):
        self._id = _id
    
    @property
    def name(self):
        return self._data['name']

    @property
    def description(self):
        try:
            return self._data['Description']['value']
        except KeyError:
            return ''

    def __repr__(self):
        return repr(self._data)
    
    def __getitem__(self, name):
        return getattr(self, name)
    
    def models(self):
        # TODO: include children
        # TODO: respect access rights (include private if logged in)
        result = []
        for model_id, data in modeldb.items():
            if self.attr_name in data:
                for obj in data[self.attr_name]['value']:
                    if obj['object_id'] == self._id:
                        result.append({'id': model_id, 'name': data['name']})
                        break
        return sorted(result, key=lambda item: item['name'])


class Current(SenseLabClass):
    classname = 'Current'
    attr_name = 'currents'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = currents[_id]
    
    @property
    def function(self):
        try:
            return self._data['Function']['value']
        except KeyError:
            return ''

class Gene(SenseLabClass):
    classname = 'Gene'
    attr_name = 'genes'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = genes[_id]

class Region(SenseLabClass):
    classname = 'Brain Region/Organism'
    attr_name = 'regions'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = regions[_id]

class Receptor(SenseLabClass):
    classname = 'Receptor'
    attr_name = 'receptors'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = receptors[_id]

class Transmitter(SenseLabClass):
    classname = 'Transmitter'
    attr_name = 'transmitters'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = transmitters[_id]

class SimEnvironment(SenseLabClass):
    classname = 'Simulation Environment'
    attr_name = 'modeling_application'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = simenvironments[_id]

class ModelConcept(SenseLabClass):
    classname = 'Model Concept'
    attr_name = 'model_concept'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = modelconcepts[_id]

class ModelType(SenseLabClass):
    classname = 'Model Type'
    attr_name = 'model_type'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = modeltypes[_id]

class CellType(SenseLabClass):
    classname = 'Cell Type'
    attr_name = 'neurons'
    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = celltypes[_id]


refresh()