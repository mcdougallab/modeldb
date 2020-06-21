import json
import zipfile
import os
import fnmatch
from pymongo import MongoClient
from django.db import models
from . import settings

mongodb = MongoClient()
sdb = mongodb[settings.security['db_name']]
sdb.authenticate(settings.security['mongodb_user'], settings.security['mongodb_pw'])

def load_collection(name):
    new_collection = {str(item['id']): item for item in getattr(sdb, name).find()}
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
    
    def has_model(self, id_):
        return id_ in modeldb
    
    def model(self, id_):
        return Model(id_)

    @property
    def num_models(self):
        return len(modeldb)
    
    def models_by_name(self):
        return sorted([{'id': key, 'name': model['name']} for key, model in modeldb.items()], key=lambda item: item['name'])



def hasany(present, wanted, add_star=False):
    # if we don't want anything, then we're always happy
    if not wanted:
        return True
    if present is None:
        return False
    for check in wanted:
        if add_star:
            check = '*' + check + '*'
        check = check.lower().strip()
        if check:
            for item in present['value']:
                if fnmatch.fnmatch(item['object_name'].lower(), check):
                    return True
    return False

def hasanytitle(present, wanted, add_star=False):
    # if we don't want anything, then we're always happy
    if not wanted:
        return True
    if present is None:
        return False
    for check in wanted:
        if add_star:
            check = '*' + check + '*'
        check = check.lower().strip()
        if check:
            for item in present:
                if fnmatch.fnmatch(item.lower(), check):
                    return True
    return False

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

class Model:
    def __init__(self, model_id):
        self._model = modeldb[model_id]
        self._zip = None
        self._readme_file = None
        self._setup_filetree()
    
    @property
    def papers(self):
        return [ModelDB.object_by_id(item['object_id']) for item in self._model['model_paper']['value']]

    def __getattr__(self, key):
        if key in self._model:
            return self._model[key]
        else:
            return None

    def zip(self):
        if self._zip is None:
            self._zip = zipfile.ZipFile(os.path.join(settings.security["modeldb_zip_dir"], str(self._model['id']) + '.zip'))
        return self._zip
    
    @property
    def readme_file(self):
        return self._readme_file

    @property
    def file_hierarchy(self):
        return self._file_hierarchy
    
    def has_path(self, path):
        return path in self.zip().namelist() or self.has_folder(path)
    
    def file(self, path):
        return self.zip().read(path)
    
    def has_folder(self, path):
        name_list = self.zip().namelist()
        path = path.strip('/') + '/'
        return any(item.startswith(path) for item in name_list)
 
    def zip_file(self):
        filename = str(self._model['id']) + '.zip'
        with open(os.path.join(settings.security["modeldb_zip_dir"], filename), 'rb') as f:
            return f.read()

    def folder_contents(self, path, _hierarchy=None):
        def _filter(items):
            return sorted([{'name': item['name'], 'type': item['type'].lower()} for item in items], key=lambda item: item['name'].lower())
        if _hierarchy is None:
            _hierarchy = self.file_hierarchy
        if '/' in path:
            first, rest = path.split('/', 1)
        else:
            first, rest = path, None
        for item in _hierarchy:
            if item['name'] == first:
                if rest:
                    return self.folder_contents(rest, _hierarchy=item['contents'])
                return _filter(item['contents'])
        assert(False)
        
    def _setup_filetree(self):
        if self._readme_file is None:
            file_hierarchy = []
            readme_file = None
            first_file = ''
            for subfilename in self.zip().namelist():
                if not first_file and os.path.split(subfilename)[1]:
                    first_file = subfilename
                if ('readme' in subfilename.lower() or subfilename.lower() in ('index.html', 'index.htm')) and readme_file is None:
                    readme_file = subfilename
                path = subfilename.split('/')
                my_file_hierarchy = file_hierarchy
                for i, item in enumerate(path):
                    for mfh in my_file_hierarchy:
                        if mfh['name'] == item:
                            my_file_hierarchy = mfh['contents']
                            break
                    else:
                        my_file_hierarchy.append({'name': item})
                        if i != len(path) - 1:
                            my_file_hierarchy[-1]['type'] = 'folder'
                            my_file_hierarchy[-1]['contents'] = []
                            my_file_hierarchy = my_file_hierarchy[-1]['contents']
                        else:
                            if '.' not in item:
                                my_file_hierarchy[-1]['type'] = 'file'
                            else:
                                my_file_hierarchy[-1]['type'] = item.split('.')[-1]
            self._readme_file = readme_file if readme_file else first_file
            self._file_hierarchy = file_hierarchy
        return self._readme_file, self._file_hierarchy






refresh()
