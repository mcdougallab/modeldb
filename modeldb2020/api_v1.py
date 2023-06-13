import json
import os
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_exempt
from . import models
from .models import (
    currents,
    genes,
    regions,
    receptors,
    transmitters,
    simenvironments,
    modelconcepts,
    modeltypes,
    celltypes,
    papers,
)
from .views import unprocessed_refs_access

ModelDB = models.ModelDB()


def _output(request, data):
    # TODO: allow request for indentation
    indent = request.GET.get("indent")
    if isinstance(data, dict):
        data2 = {key: value for key, value in data.items() if key != "_id"}
    else:
        data2 = data
    if indent is None:
        result = json.dumps(data2)
    else:
        result = json.dumps(data2, indent=int(indent))
    return HttpResponse(result, content_type="application/json")


def index(request):
    return _output(
        request,
        sorted(
            [
                "models",
                "celltypes",
                "currents",
                "genes",
                "regions",
                "receptors",
                "transmitters",
                "simenvironments",
                "modelconcepts",
                "modeltypes",
                "papers",
            ]
        ),
    )


def get_filter(request):
    items = {item: value for item, value in request.GET.items() if item != "indent"}
    if not items:
        return lambda item: True

    def result(item):
        for param, condition in items.items():
            val = item.get(param, {"value": []})
            for check in val["value"]:
                if (
                    str(check["object_id"]) == condition
                    or check["object_name"] == condition
                ):
                    break
            else:
                return False
        return True

    return result


def request_make_public(request):
    from .views import all_model_access

    model_id = request.POST.get("id")
    if ModelDB.has_private_model(model_id):
        access = request.session.get(model_id)
        if access == "rw" or all_model_access(request):
            ModelDB.request_to_make_public(model_id)
            return HttpResponse("success")
    return HttpResponse("403 Forbidden", status=403)


def make_public(request):
    from .views import all_model_access

    model_id = request.POST.get("id")
    if ModelDB.has_private_model(model_id):
        if all_model_access(request):
            ModelDB.make_public(model_id)
            return HttpResponse("success")
    print("failed; no access rights")
    return HttpResponse("403 Forbidden", status=403)


def unprocessed_refs_view(request, _id=None):
    data = request.POST.get("data")
    if (not unprocessed_refs_access(request)) or (data is None):
        return HttpResponse("403 Forbidden", status=403)
    paper_id = request.POST.get("paper_id")
    new_id = models.set_unprocessed_refs(paper_id, data)
    return HttpResponse(str(new_id))


def _get_multiselect_data(field, attr_id):
    return {
        "value": [
            {"object_id": int(_id), "object_name": models._object_by_id(_id).name}
            for _id in field.split(",")
            if _id
        ],
        "attr_id": attr_id,
    }


def models_view(request, model_id=None, field=None):
    if model_id is not None:
        model_id = str(model_id)
        if request.method == "GET":
            if ModelDB.has_model(model_id):
                return _output(request, ModelDB.model(model_id)._model)
            else:
                return HttpResponse("404 Not Found", status=404)
        elif request.method == "POST":
            data = {
                "name": request.POST["edit_model_name"],
                "notes": {"value": request.POST["model_notes"], "attr_id": 24},
                "expmotivation": request.POST["expmotivation"],
                "neurons": _get_multiselect_data(request.POST["neurons"], 25),
                "model_type": _get_multiselect_data(request.POST["model_type"], 112),
                "modeling_application": _get_multiselect_data(
                    request.POST["modeling_application"], 114
                ),
                "currents": _get_multiselect_data(request.POST["currents"], 27),
                "model_concept": _get_multiselect_data(
                    request.POST["model_concept"], 113
                ),
                "gene": _get_multiselect_data(request.POST["gene"], 476),
                "region": _get_multiselect_data(request.POST["region"], 471),
                "receptors": _get_multiselect_data(request.POST["receptors"], 26),
                "neurotransmitters": _get_multiselect_data(
                    request.POST["neurotransmitters"], 28
                ),
                "data_to_curate.citation": request.POST["modelcitation"],
                "data_to_curate.implementers": request.POST["modelimplementers"],
            }
            # TODO: new_zip

            from .views import all_model_access

            is_public_model = ModelDB.has_model(model_id)
            if not is_public_model:
                is_private_model = ModelDB.has_private_model(model_id)
            if is_public_model or is_private_model:
                access = request.session.get(model_id)
                if access == "rw" or all_model_access(request):
                    if is_public_model:
                        ModelDB.model(model_id).update(data)
                    else:
                        ModelDB.private_model(model_id).update(data)
                    return HttpResponse("success")
            return HttpResponse("403 Forbidden", status=403)
        else:
            return HttpResponse(
                f"403 Forbidden; unsupported method: {request.method}", status=403
            )
    elif field is not None:
        my_filter = get_filter(request)
        return _output(
            request,
            [item.get(field) for item in models.modeldb.values() if my_filter(item)],
        )
    else:
        my_filter = get_filter(request)
        return _output(
            request,
            [int(item["id"]) for item in models.modeldb.values() if my_filter(item)],
        )


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


def morphology_view(request, _id=None):
    try:
        with open(
            os.path.join(models.settings.security["modelview_dir"], f"{_id}.json")
        ) as f:
            result = f.read()
        return HttpResponse(result, content_type="application/json")
    except:
        return HttpResponse("404 Not Found", status=404)


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
