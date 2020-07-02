import re
import html
import json
import os
import datetime
import bcrypt
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_sameorigin
from . import settings
from . import models
from .models import currents, genes, regions, receptors, transmitters, simenvironments, modelconcepts, modeltypes, celltypes, papers
from .models import Paper


ModelDB = models.ModelDB()

# need this because f-strings cannot include a backslash
_newline = '\n'

def index(request):
    context = {
        'title': 'ModelDB',
        'ModelDB': ModelDB,
        'request': request
    }
    return render(request, 'index.html', context)


def _id_and_name(data):
    return sorted([(item['id'], item['name']) for item in data.values()], key=lambda item: item[1])


def models_with_uncurated_references(request):
    # TODO: this should really be about the users authentication level not the simple act of being authenticated
    if request.user.is_authenticated:
        uncurated_models = models.models_with_uncurated_papers()
        context = {
            'request': request,
            'models': uncurated_models
        }
        return render(request, 'models-with-uncurated-references.html', context)
    else:
        return redirect(f'/login?next={request.path}')


def process_model_submit(request):
    # TODO: probably some of this should move into models?
    the_file = request.FILES['zipfile']
    filename = the_file.name
    if not filename.lower().endswith('.zip'):
        return HttpResponse('403 Forbidden: non-zip upload; hit back and try again', status=403)

    new_id = models.new_object_id()
    # store the file
    with open(os.path.join(settings.security['modeldb_private_zip_dir'], f'{new_id}.zip'), 'wb') as f:
        for chunk in the_file.chunks():
            f.write(chunk)

    # salt is used for hashing passwords and stored with the hash; it does not need to be stored separately
    salt = bcrypt.gensalt()

    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    entry = {
        'id': int(new_id),
        'name': request.POST.get('name'),
        'created': now,
        'ver_number': 1,
        'ver_date': now,
        'class_id': 19,
        'notes': {"value": request.POST.get('notes'), "attr_id": 24},
        'license': request.POST.get('license'),
        'expmotivation': request.POST.get('expmotivation'),
        "public_submitter_email": {"value": request.POST['modeleremail'], "attr_id": 309},
        'data_to_curate': {
            'rwac': bcrypt.hashpw(request.POST['rwac'].encode('utf8'), salt).decode('utf8'),
            'othertags': request.POST.get('othertags'),
            'citation': request.POST.get('citation'),
            'implementers': request.POST.get('implementers'),
            'modelername': request.POST.get('modelername')
        }
    }

    if request.POST.get('rac'):
        entry['data_to_curate']['rac'] = bcrypt.hashpw(request.POST['rac'].encode('utf8'), salt).decode('utf8')

    _process_submit_list(request, 'celltypes', 'neurons', 25, entry)
    _process_submit_list(request, 'receptors', 'receptors', 26, entry)
    _process_submit_list(request, 'currents', 'currents', 27, entry)
    _process_submit_list(request, 'transmitters', 'neurotransmitters', 28, entry)
    _process_submit_list(request, 'model_type', 'model_type', 112, entry)
    _process_submit_list(request, 'concepts', 'model_concept', 113, entry)
    _process_submit_list(request, 'simenvironment', 'modeling_application', 114, entry)
    _process_submit_list(request, 'genes', 'gene', 476, entry)
    _process_submit_list(request, 'regions', 'region', 471, entry)

    models.add_private_model(entry)

    context = {
        'title': 'Model upload successful',
        'request': request,
        'accession_number': new_id
    }
    return render(request, 'processmodelsubmit.html', context)


def _process_submit_list(request, listname, fieldname, attr_id, entry):
    objs = [{'object_id': int(id_), 'object_name': ModelDB.object_by_id(id_).name} for id_ in request.POST.getlist(listname)]
    if objs:
        entry[fieldname] = {
            'value': objs,
            'attr_id': attr_id
        }

def submit_model(request):
    metadata = [
        ['Neurons', 'celltypes', _id_and_name(celltypes)],
        ['Currents', 'currents', _id_and_name(currents)],
        ['Neurotransmitters', 'transmitters', _id_and_name(transmitters)],
        ['Receptors', 'receptors', _id_and_name(receptors)],
        ['Genes', 'genes', _id_and_name(genes)],
        ['Concepts', 'concepts', _id_and_name(modelconcepts)],
        ['Region or organism', 'regions', _id_and_name(regions)],
        ['Simulation environment', 'simenvironment', _id_and_name(simenvironments)]
    ]
    context = {
        'title': 'Submit Model',
        'request': request,
        'metadata': metadata
    }
    return render(request, 'submitmodel.html', context)

def static(request, page='', title=''):
    context = {
        'title': f'ModelDB: {title}',
        'request': request
    }
    return render(request, f'{page}.html', context)


def modellist(request):
    object_id = request.GET.get('id')
    if object_id is None:
        return listbymodelname(request)
    
    obj = ModelDB.object_by_id(object_id)
    if obj is None:
        return listbymodelname(request)
    seealso = {}
    if object_id == '3537':
        seealso = {cell['name']: f"?id={cell['id']}" for cell in sorted(celltypes.values(), key=lambda item: item['name'])}
    elif object_id == '3540':
        seealso = {channel['name']: f"?id={channel['id']}" for channel in sorted(currents.values(), key=lambda item: item['name'])}
    elif 'children' in obj._data:
        children = [ModelDB.object_by_id(_id) for _id in obj._data['children']]
        seealso = {child.name: f'?id={child._id}' for child in children}

    context = {
        'title': f'ModelDB: Models that contain {obj.name}',
        'obj': obj,
        'seealso': seealso
    }
    return render(request, 'modellist.html', context)

def listbymodelname(request):
    context = {
        'title': 'ModelDB: Models List',
        'all_models': ModelDB.models_by_name()
    }
    return render(request, 'listbymodelname.html', context)

    

def my_logout(request):
    logout(request)
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('/')

def my_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if password is not None:
        user = authenticate(username=username, password=password)
        next_url = request.POST.get('next')
        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next'))
    else:
        next_url = request.GET.get('next')
    context = {
        'next': next_url
    }
    return render(request, 'login.html', context)

def showmodel_redirect(request, model_id=None, tab_id=None, filename=None):
    # TODO: handle filename
    if model_id is None:
        return HttpResponse('404 not found', status=404)
    try:
        m = int(model_id)
    except ValueError:
        return HttpResponse('404 not found', status=404)
    # TODO: handle a missing model more gracefully
    if (not ModelDB.has_model(model_id)) and (not ModelDB.has_private_model(model_id)):
        return HttpResponse('404 not found', status=404)
    if tab_id is None:
        tab_id = int(request.GET.get('tab', 1))
    if tab_id == 1:
        tab_string = ''
    else:
        tab_string = f'&tab={tab_id}'
    return redirect(f'/showmodel?model={model_id}{tab_string}')

def forget_access(request):
    model_id = request.GET.get('model', -1)
    request.session[model_id] = None
    del request.session[model_id]
    return showmodel_redirect(request, model_id=model_id)


def showmodel(request):
    model_id = request.GET.get('model', -1)
    tab_id = int(request.GET.get('tab', 1))
    filename = request.GET.get('file')
    access = None

    # TODO: handle not having a model argument more gracefully
    if model_id == -1:
        model_id = request.POST.get('model')
        if model_id is None:
            return HttpResponse('404 not found', status=404)
        else:
            tab_id = int(request.POST.get('tab', 1))
            filename = request.POST.get('file')


    if not ModelDB.has_model(model_id):
        if ModelDB.has_private_model(model_id):
            access = request.session.get(model_id)
            if access is None:
                code = request.POST.get('access_code')
                # TODO: refactor this block of code; it is repetitive
                if code is None:
                    context = {
                        'request': request,
                        'title': 'Private model access',
                        'msg': '',
                        'tab_id': tab_id,
                        'model': int(model_id),
                        'file': filename
                    }
                    return render(request, 'showmodel_login.html', context)
                else:
                    access = ModelDB.auth_private_model(model_id, code)
                    if access is not None:
                        request.session[model_id] = access
                        return showmodel_redirect(request, model_id=model_id, tab_id=tab_id, filename=filename)
                    else:
                        context = {
                            'request': request,
                            'title': 'Private model access',
                            'msg': 'Login failed; try again.',
                            'tab_id': tab_id,
                            'model': int(model_id),
                            'file': filename
                        }
                    return render(request, 'showmodel_login.html', context)
            model = ModelDB.private_model(model_id)
        else:
            # TODO: handle a missing model more gracefully
            return HttpResponse('404 not found', status=404)
    else:
        model = ModelDB.model(model_id)

    if tab_id != 7:
        if tab_id != 2:
            filename = model.readme_file
            filename = filename.replace('\\', '/').strip('/')
        elif tab_id == 2 and filename is None:
            filename = model.readme_file
            filename = filename.replace('\\', '/').strip('/').split('/')[0]

        original_file_valid = model.has_path(filename)
        if not original_file_valid:
            filename = model.readme_file
        is_folder = model.has_folder(filename)
        original_filename = filename
        filename = filename.split('/')
        breadcrumbs = []
        for i, name in enumerate(filename):
            link = f'/showmodel?tab=2&model={model_id}&file={"/".join(filename[0: i + 1])}'
            breadcrumbs.append(f'<a href="{link}">{name}</a>')
        if original_file_valid:
            breadcrumbs[-1] = name
        else:
            breadcrumbs[0] = f'<span style="color:red!important">Requested file does not exist</span>; showing {breadcrumbs[0]}'
        
        if is_folder:
            content = model.folder_contents(original_filename)
        else:
            content = 'foo' # TODO: this probably shouldn't be this way

        context = {
            'title': 'ModelDB: Show Model',
            'Model': model,
            'breadcrumbs': breadcrumbs,
            'is_folder': is_folder,
            'content': content,
            'filename': original_filename,
            'tab': tab_id,
            'access': access,
            'extension': original_filename.split('.')[-1].lower()
        }
        if tab_id == 2:
            return render(request, 'showmodel2.html', context)
        else:
            return render(request, 'showmodel.html', context)
    else:
        papers = model.papers
        citation_data = _prep_citations(papers)
        context = {
            'title': 'ModelDB: Model Citations',
            'Model': model,
            'tab': tab_id,
            'citation_data': citation_data,
            'showtabs': True
        }
        return render(request, 'showmodel7.html', context)

def mdbcitations(request):
    # TODO: probably can't always assume ints? maybe should recast existing to str?
    paper_id = str(request.GET.get('id', -1))
    # TODO: handle not having a model argument more gracefully
    if paper_id == '-1':
        return HttpResponse('Forbidden', status=403)
    # TODO: we actually know what datatype this is
    papers = [ModelDB.object_by_id(paper_id)]
    citation_data = _prep_citations(papers)
    context = {
        'title': 'ModelDB: Paper information',
        'Model': None,
        'citation_data': citation_data,
        'showtabs': False
    }
    return render(request, 'showmodel7.html', context)


def _prep_citations(papers):
    references = [[paper for paper in model_paper.references] for model_paper in papers]
    sorted_references=[]
    for reference_group in references:
        tmp_sorted_list=sorted(reference_group, key=magic)
        sorted_references.append(tmp_sorted_list)
    #citations = [[paper.html for paper in model_paper.citations] for model_paper in papers]
    citations = [[paper for paper in model_paper.citations] for model_paper in papers]
    sorted_citations=[]
    for citation_group in citations:
        #tmp_sorted_list=sorted(citation_group, key=lambda item: item.authors+[item.year])
        tmp_sorted_list=sorted(citation_group, key=magic)# lambda item: item.authors+[item.year])
        #except:
        #    tmp_sorted_list = citation_group
        sorted_citations.append(tmp_sorted_list)
    return zip(papers, sorted_references, sorted_citations)



def download_zip(request):
    model_id = request.GET.get('o', -1)
    model = _get_model(request, model_id)
    if model is None:
        return HttpResponse('Forbidden', status=403)
    filename = f'{model_id}.zip'
    response = HttpResponse(content_type="application/zip")
    response['Content-Disposition'] = f'attachment; filename={filename}'
    response.write(model.zip_file())
    return response

def _remap_src(model_id, match, base_filename):
    match_text = match.group()
    src = match_text[5:-1]
    src_lower = src.lower()
    if src_lower.startswith('http://') or src_lower.startswith('//') or src_lower.startswith('https://'):
        # TODO: we probably don't want this at all, but not clear what it's trying to do
        src = re.sub(r'(?i)(https?:)?//senselab\.med\.yale\.edu/', '/', src)
    else:
        while base_filename.startswith('/'):
            base_filename = base_filename[1:]
        src = f'/getmodelfile?model={model_id}&file={base_filename}{src}'
        src = src.replace('/./', '/').replace('//', '/')
    return 'src="' + src + '"'

def _remap_href(model_id, match, base_filename):
    match_text = match.group()
    src = match_text[6:-1]
    src_lower = src.lower()
    if src_lower.startswith('http://') or src_lower.startswith('//') or src_lower.startswith('https://'):
        # TODO: we probably don't want this at all, but not clear what it's trying to do
        src = re.sub(r'(?i)(https?:)?//senselab\.med\.yale\.edu/', '/', src)
    return f'href="{src}"'

def _get_model(request, model_id, permissions=None):
    if permissions is None:
        permissions = ['r', 'rw']
    elif isinstance(permissions, str):
        permissions = [permissions]
    if ModelDB.has_model(model_id):
        model = ModelDB.model(model_id)
    elif ModelDB.has_private_model(model_id) and request.session[model_id] in permissions:
        model = ModelDB.private_model(model_id)
    else:
        model = None
    return model


@xframe_options_sameorigin
def download(request):
    model_id = request.GET.get('model', -1)
    model = _get_model(request, model_id)
    if model is None:
        return HttpResponse('Forbidden', status=403)
    filename = request.GET.get('file')
    if not model.has_path(filename):
        return HttpResponse('Forbidden', status=403)
    embed = request.GET.get('embed', '').lower() == 'true'
    contents = model.file(filename)
    # discard path information; only keep filename
    filename = filename.replace('\\', '/')
    short_filename = filename.split('/')[-1]
    base_filename = filename[:-len(short_filename)]
    filename = short_filename
    if embed:
        response = HttpResponse()
        extension = filename.split('.')[-1].lower()
        if extension in ('html', 'htm'):
            contents = contents.decode('utf-8')
            contents = re.sub('src="(.*?)"|src=\'(.*?)\'', lambda match: _remap_src(model_id, match, base_filename), contents)
            contents = re.sub('href="(.*?)"|href=\'(.*?)\'', lambda match: _remap_href(model_id, match, base_filename), contents)
            # have to specify a base target otherwise will try to load links inside the iframe
            contents = f'<base target="_parent">{contents}'
        else:
            try:
                # TODO: be smarter about handling extensions
                # workaround for HOC using C
                if extension in ('hoc', 'ses'):
                    extension = 'c'
                if extension in ('py', 'cpp', 'c', 'bas', 'js', 'cxx', 'h', 'f90', 'f95', 'json', 'java', 'md', 'r', 'sql', 'vba', 'vbs', 'yaml', 'yml', 'pl', 'lisp', 'lua', 'hs', 'go', 'css', 'c++', 'hpp', 'cs'):
                    contents = f'<link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.14.2/styles/vs.min.css" rel="stylesheet" /><script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.14.2/highlight.min.js"></script><script>hljs.initHighlightingOnLoad();</script><pre><code class="{extension}">{html.escape(contents.decode("utf-8"))}</code></pre>'
                else:
                    contents = f'<pre>{html.escape(contents.decode("utf-8"))}</pre>'
            except:
                contents = 'This file is not encoded as UTF-8. Download it to view.'
            contents = f'<html><body>{contents}</body></html>'
    else:
        response = HttpResponse(content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename={filename}'
    response.write(contents)
    return response    

def magic(item):
    if item.authors:
        return item.authors + [item.year]
    else:
        return [item.name, item.year]

def findbyregionlist(request):
    context = {
        'title': 'ModelDB: Browse by current',
        'content': _render_tree(celltypes, '/ModelDB/ModelList'),
        'header': 'Find models of a particular neuron',
        'subhead': 'Click on a neuron/cell to show a list of models of that type.'
    }
    return render(request, 'treepage.html', context)


def trends(request):
    filters = [
        ('modelconcepts', sorted([(item['id'], item['name']) for item in modelconcepts.values()], key=lambda item: item[1]), 'model concept'),
        ('simenvironments', sorted([(item['id'], item['name']) for item in simenvironments.values()], key=lambda item: item[1]), 'simulation environment'),
        ('celltypes', sorted([(item['id'], item['name']) for item in celltypes.values()], key=lambda item: item[1]), 'cell type'),
        ('currents', sorted([(item['id'], item['name']) for item in currents.values()], key=lambda item: item[1]), 'current')
    ]
    context =  {
        'title': 'Models by create date',
        'request': request, 
        'filters': filters
    }
    return render(request, "modelsbycreatedate.html", context)

def findbycurrent(request):
    context = {
        'title': 'ModelDB: Browse by current',
        'content': _render_tree(currents, '/ModelDB/ModelList'),
        'header': 'Find models that contain a particular ionic current',
        'subhead': 'Click on an ionic current to show a list of models that contain or implement that current.<br/><br/>Click <a href="https://senselab.med.yale.edu/neurondb/ndbregions">here</a> to view brief definitions of currents in NeuronDB.'
    }
    return render(request, 'treepage.html', context)

def findbyreceptor(request):
    context = {
        'title': 'ModelDB: Browse by receptor',
        'content': _render_tree(receptors, '/ModelDB/ModelList'),
        'header': 'Find models that contain a particular ionic current',
        'subhead': 'Click on a receptor to show a list of models that contain or implement that receptor.<br/>'
    }
    return render(request, 'treepage.html', context)

def findbytransmitter(request):
    context = {
        'title': 'ModelDB: Browse by neurotransmitter',
        'content': _render_tree(transmitters, '/ModelDB/ModelList'),
        'header': 'Find models that contain a particular neurotransmitter',
        'subhead': 'Click on a neurotransmitter to show a list of models that implement a mechanism for release of that transmitter.<br/>'
    }
    return render(request, 'treepage.html', context)

def findbygene(request):
    context = {
        'title': 'ModelDB: Browse by gene',
        'content': _render_tree(genes, '/ModelDB/ModelList'),
        'header': 'Find models containing a particular gene',
        'subhead': 'Click on a gene name to show a list of electrical or chemical models of the associated channel or receptor.<br/>'
    }
    return render(request, 'treepage.html', context)

def findbyconcept(request):
    context = {
        'title': 'ModelDB: Browse by concept',
        'content': _render_tree(modelconcepts, '/ModelDB/ModelList'),
        'header': 'Find models by concept',
        'subhead': 'Click on a concept to show a list of models that incorporate or demonstrate that concept.<br/>'
    }
    return render(request, 'treepage.html', context)

def findbysimulator(request):
    context = {
        'title': 'ModelDB: Browse by simulation environment',
        'content': _render_tree(simenvironments, '/ModelDB/ModelList'),
        'header': 'Find models by simulation environment',
        'subhead': 'Click on a link to show a list of models implemented in that simulation environment or programming language.<br/>'
    }
    return render(request, 'treepage.html', context)

def _render_tree_element(obj, collection, base_link):
    subtree = ''
    if 'children' in obj:
        subtree = f"<ul>{_newline.join(_render_tree_element(collection[child], collection, base_link) for child in sorted(obj['children'], key=lambda _id: collection[_id]['name'].lower()))}</ul>"
    return f'<li><a href="{base_link}?id={obj["id"]}">{obj["name"]}{subtree}</li>'

def _render_tree(collection, base_link):
    root_nodes = [item for item in collection.values() if not 'parent' in item or item['parent'] is None]
    root_nodes = sorted(root_nodes, key=lambda obj: obj['name'].lower())
    return f'<ul>{_newline.join(_render_tree_element(node, collection, base_link) for node in root_nodes)}</ul>'

def _update_search_query(query, item, name):
    if item:
        query.append({'name': name, 'search': item.strip(';')})

def _parse_search(item):
    if item:
        return [term.strip() for term in item.split(';')]
    else:
        return []

def _get_names(collection_data):
    return json.dumps(sorted([item['name'] for item in collection_data.values()]))

def search(request):
    my_transmitters = request.GET.get('transmitters')
    my_receptors = request.GET.get('receptors')
    my_genes = request.GET.get('genes')
    my_simenvironment = request.GET.get('simenvironment')
    my_modelconcepts = request.GET.get('modelconcepts')
    my_celltypes = request.GET.get('celltypes')
    my_modeltype = request.GET.get('modeltype')
    my_brainregions = request.GET.get('brainregions')
    my_channels = request.GET.get('channels')
    my_authors = None
    my_title = request.GET.get('title')

    if my_transmitters or my_receptors or my_genes or my_simenvironment or my_modelconcepts or my_celltypes or my_modeltype or my_brainregions or my_channels or my_authors or my_title:
        query = []
        _update_search_query(query, my_channels, 'Currents')
        _update_search_query(query, my_transmitters, 'Transmitters')
        _update_search_query(query, my_receptors, 'Receptors')
        _update_search_query(query, my_genes, 'Genes')
        _update_search_query(query, my_simenvironment, 'Simulation Environment')
        _update_search_query(query, my_modelconcepts, 'Model Concepts')
        _update_search_query(query, my_celltypes, 'Cell Types')
        _update_search_query(query, my_modeltype, 'Model Type')
        _update_search_query(query, my_brainregions, 'Brain Region/Organism')
        _update_search_query(query, my_title, 'Title')
        _update_search_query(query, my_authors, 'Author')

        results = ModelDB.find_models(
            channels = _parse_search(my_channels),
            transmitters = _parse_search(my_transmitters),
            receptors = _parse_search(my_receptors),
            genes = _parse_search(my_genes),
            simenvironment = _parse_search(my_simenvironment),
            modelconcepts = _parse_search(my_modelconcepts),
            celltypes = _parse_search(my_celltypes),
            modeltype = _parse_search(my_modeltype),
            brainregions = _parse_search(my_brainregions),
            title = _parse_search(my_title),
            authors = _parse_search(my_authors)
        )

        # do the actual search
        context = {
            'title': 'ModelDB: search',
            'query': query,
            'results': results
        }
        return render(request, 'searchresults.html', context)
    else:

        context = {
            'title': 'ModelDB: search',
            'modeltype_tags': _get_names(modeltypes),
            'receptors_tags': _get_names(receptors),
            'genes_tags': _get_names(genes),
            'channels_tags': _get_names(currents),
            'brainregions_tags': _get_names(regions),
            'celltypes_tags': _get_names(celltypes),
            'modelconcepts_tags': _get_names(modelconcepts),
            'transmitters_tags': _get_names(transmitters),
            'simenvironment_tags': _get_names(simenvironments),
            'ModelDB': ModelDB
        }
        return render(request, 'search.html', context)