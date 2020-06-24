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

# TODO: force object_id to be string here so we don't have to do it later
def load_collection(name):
    new_collection = {str(item['id']): item for item in getattr(sdb, name).find()}
    # expand parent data (if any) into reciprocal parent-child data
    for item in new_collection.values():
        if 'parent' in item:
            item['parent'] = str(item['parent'])
            new_collection[item['parent']].setdefault('children', [])
            new_collection[item['parent']]['children'].append(str(item['id']))
    return new_collection


def refresh():
    global modeldb, currents, genes, regions, receptors
    global transmitters, simenvironments, modelconcepts
    global modeltypes, celltypes, papers, cites_paper_unsorted

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

    # Prepare dictionary used to provide the "references that cite a paper" on citation display pages

    cites_paper_unsorted={}  # will contain value key pairs like 
    # cites_paper_unsorted[paper_obj_id]=[list of obj ids of refs that cite paper_obj_id]

    # Loop over all the papers.  Actually the citing_paper_obj_id is not necessarily "citing" until it is found to have refs a line below
    for citing_paper_obj_id in papers:
        citing_paper_obj_id = str(citing_paper_obj_id)
        if 'references' in papers[citing_paper_obj_id]:
            # loop over the list of references in the paper:
            for ref in papers[citing_paper_obj_id]['references']['value']:
                cited_paper_obj_id = str(ref['object_id'])
                cites_paper_unsorted.setdefault(cited_paper_obj_id, [])
                cites_paper_unsorted[cited_paper_obj_id].append(citing_paper_obj_id)

    print('cites_paper_unsorted', cites_paper_unsorted['126976'])

class ModelDB(models.Model):
    class Meta:
        app_label = 'modeldb2020',
        permissions = [
            ('can_admin', 'Can do admin'),
            ('can_pipeline', 'Can use pipeline')
        ]

    def find_models(self, channels=[], transmitters=[], receptors=[], genes=[], simenvironment=[], modelconcepts=[], celltypes=[], modeltype=[],
                    brainregions=[], title=[], authors=[]):
        result = []
        for model in modeldb.values():
            
            if (hasany(model.get('transmitters'), transmitters) and hasany(model.get('receptors'), receptors) and hasany(model.get('genes'), genes)
                and hasany(model.get('modeling_application'), simenvironment) and hasany(model.get('model_concept'), modelconcepts)
                and hasany(model.get('neurons'), celltypes) and hasany(model.get('model_type'), modeltype)
                and hasany(model.get('currents'), channels)
                #and hasany(model.get('authors'), authors)
                and hasanytitle([model.get('name')], title, add_star=True)
                and hasany(model.get('brainregions'), brainregions)):
                result.append(self.model(model['id']))
        
        return result


    def get_models(self):
        return modeldb

    def __getitem__(self, name):
        return getattr(self, name)
    
    def has_model(self, id_):
        return id_ in modeldb

    def object_by_id(self, object_id):
        return _object_by_id(object_id)
    
    def model(self, id_):
        return Model(id_)

    @property
    def num_models(self):
        return len(modeldb)
    
    def models_by_name(self):
        return sorted([{'id': key, 'name': model['name']} for key, model in modeldb.items()], key=lambda item: item['name'])

def _object_by_id(object_id):
    object_id = str(object_id)
    test_list = [modeldb, currents, genes, regions, receptors, transmitters, simenvironments, modelconcepts, modeltypes, celltypes, papers]
    classes = [Model, Current, Gene, Region, Receptor, Transmitter, SimEnvironment, ModelConcept, ModelType, CellType, Paper]
    for test, kind in zip(test_list, classes):
        if object_id in test:
            return kind(object_id)
    return None

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
        self._id = str(_id)
    
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
                    # TODO: see the TODO on load_collection that will allow removing this str()
                    if str(obj['object_id']) == self._id:
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
        print('model_id', model_id)
        print(modeldb.keys())
        self._model = modeldb[str(model_id)]
        self._zip = None
        self._readme_file = None
        self._setup_filetree()
    
    @property
    def papers(self):
        return [_object_by_id(item['object_id']) for item in self._model['model_paper']['value']]

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


class Paper:
    def __init__(self, paper_id):
        self._id = str(paper_id)
    
    @property
    def _raw(self):
        return papers[str(self._id)]

    @property
    def authors(self):
        try:
            return [item['object_name'] for item in self._raw['authors']['value']]
        except:
            return ''
    
    @property
    def year(self):
        try:
            return self._raw['year']['value']
        except:
            return ''

    @property
    def model_link(self):
        try:
            return self._raw['model_link']
        except:
            return ''
    
    @property
    def title(self):
        try:
            return self._raw['title']['value']
        except:
            return ''

    @property
    def journal(self):
        try:
            return self._raw['journal']['value']    
        except:
            return ''

    @property
    def volume(self):
        try:
            return self._raw.get('volume', {'value': ''})['value']    
        except:
            return ''

    @property
    def url(self):
        try:
            return self._raw['url']['value']
        except:
            return ''

    @property
    def doi(self):
        try:
            return self._raw['doi']['value']
        except:
            return ''

    @property
    def pubmed(self):
        try:
            return self._raw['pubmed_id']['value']
        except:
            return ''

    @property
    def html(self):
        url = self.doi
        if not url:
            url = self.url
        else:
            url = 'https://doi.org/' + url
        
        if url:
            link_prefix = '<a href="{}">'.format(url)
            link_suffix = '</a>'
        else:
            link_prefix = link_suffix = ''

        pubmed = self.pubmed
        if pubmed:
            pubmed = ' [<a href="https://www.ncbi.nlm.nih.gov/pubmed?holding=modeldb&term={}">PubMed</a>]'.format(pubmed)

        base_info = ', '.join(self.authors) + f'. ({self.year}).'
        base_info = f'<a href="/mdbcitations?id={self._id}">{base_info}</a>'
        return base_info + f' {self.title} <i>' + link_prefix + self.journal + link_suffix + '</i> ' + self.volume + pubmed
    
    def __getitem__(self, item):
        return getattr(self, item)
    
    @property
    def references(self):
        if 'references' in self._raw:
            return [Paper(item['object_id']) for item in self._raw['references']['value']]
        else:
            return []
    
    @property
    def citations(self):
        if self._id in cites_paper_unsorted:
            return [Paper(item) for item in cites_paper_unsorted[self._id]]
        else:
            return []
    
    @property
    def name(self):
        return self._raw['name']


refresh()
