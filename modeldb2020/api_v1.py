import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_exempt
from . import models
from .models import currents, genes, regions, receptors, transmitters, simenvironments, modelconcepts, modeltypes, celltypes, papers


ModelDB = models.ModelDB()

def _output(request, data):
    # TODO: allow request for indentation
    if isinstance(data, dict):
        data2 = {key: value for key, value in data.items() if key != '_id'}
    else:
        data2 = data
    return HttpResponse(json.dumps(data2))

def index(request):
    return _output(request, sorted([
        'models', 'celltypes', 'currents', 'genes', 'regions', 'receptors', 'transmitters',
        'simenvironments', 'modelconcepts', 'modeltypes', 'papers'
        ]))

def models_view(request, model_id=None, field=None):
    if model_id is not None:
        model_id = str(model_id)
        if ModelDB.has_model(model_id):
            return _output(request, ModelDB.model(model_id)._model)
        else:
            return HttpResponse("404 Not Found", status=404)
    elif field is not None:
        return _output(request, [item.get(field) for item in models.modeldb.values()])
    else:
        return _output(request, list(models.modeldb.keys()))

def papers_view(request, _id=None, field=None):
    return _generic_view(request, papers, _id, field)

def modeltypes_view(request, _id=None, field=None):
    return _generic_view(request, modeltypes, _id, field)

def modelconcepts_view(request, _id=None, field=None):
    return _generic_view(request, modelconcepts, _id, field)

def celltypes_view(request, _id=None, field=None):
    return _generic_view(request, celltypes, _id, field)

def currents_view(request, _id=None, field=None):
    return _generic_view(request, currents, _id, field)

def genes_view(request, _id=None, field=None):
    return _generic_view(request, genes, _id, field)

def regions_view(request, _id=None, field=None):
    return _generic_view(request, regions, _id, field)

def receptors_view(request, _id=None, field=None):
    return _generic_view(request, receptors, _id, field)

def transmitters_view(request, _id=None, field=None):
    return _generic_view(request, transmitters, _id, field)

def simenvironments_view(request, _id=None, field=None):
    return _generic_view(request, simenvironments, _id, field)


def _generic_view(request, collection, _id, field):
    if _id is not None:
        if _id in collection:
            return _output(request, collection[_id])
        elif str(_id) in collection:
            return _output(request, collection[str(_id)])
        else:
            return HttpResponse("404 Not Found", status=404)
    elif field is not None:
        return _output(request, [item.get(field) for item in collection.values()])
    else:
        return _output(request, list(collection.keys()))
