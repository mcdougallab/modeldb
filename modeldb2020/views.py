import re
import html
import json
import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_exempt
from . import settings
from . import models
from .models import currents, genes, regions, receptors, transmitters, simenvironments, modelconcepts, modeltypes, celltypes, papers


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

#from .models import currents, genes, regions, receptors, transmitters, simenvironments, modelconcepts, modeltypes, celltypes, papers

def process_model_submit(request):
    # TODO: check for zip file extension (and, ideally being an actual zip file)
    new_id = models.new_object_id()
    # store the file
    with open(os.path.join(settings.security['modeldb_private_zip_dir'], f'{new_id}.zip'), 'wb') as f:
        for chunk in request.FILES['file1'].chunks():
            f.write(chunk)
    # TODO: actually create the private model in the database
    context = {
        'title': 'Model upload successful',
        'request': request,
        'accession_number': new_id,
        'content': str(type(request.FILES['file1']))
    }
    return render(request, 'processmodelsubmit.html', context)


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
        print('next_url', next_url)
        if user is not None:
            login(request, user)
            print('authenticated', user)
            return redirect(request.POST.get('next'))
    else:
        next_url = request.GET.get('next')
        print('next_url', next_url)
    context = {
        'next': next_url
    }
    return render(request, 'login.html', context)

def showmodel_redirect(request, model_id=None):
    if model_id is None:
        return HttpResponse('404 not found', status=404)
    # TODO: handle a missing model more gracefully
    if not ModelDB.has_model(model_id):
        return HttpResponse('404 not found', status=404)
    tab_id = int(request.GET.get('tab', 1))
    if tab_id == 1:
        tab_string = ''
    else:
        tab_string = f'&tab={tab_id}'
    return redirect(f'/showmodel?model={model_id}{tab_string}')

def showmodel(request):
    # TODO: probably can't always assume ints? maybe should recast existing to str?
    model_id = request.GET.get('model', -1)
    tab_id = int(request.GET.get('tab', 1))
    # TODO: handle not having a model argument more gracefully
    if model_id == -1:
        print('model_id == -1')
        return HttpResponse('404 not found', status=404)
    # TODO: handle a missing model more gracefully
    if not ModelDB.has_model(model_id):
        print('did not pass has_model')
        return HttpResponse('404 not found', status=404)

    model = ModelDB.model(model_id)

    if tab_id != 7:
        filename = request.GET.get('file')
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

        # TODO: handle a file specification
        if not ModelDB.has_model(model_id):
            return HttpResponse('404 not found', status=404)

        context = {
            'title': 'ModelDB: Show Model',
            'Model': model,
            'breadcrumbs': breadcrumbs,
            'is_folder': is_folder,
            'content': content,
            'filename': original_filename,
            'tab': tab_id,
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
    if model_id == -1:
        return HttpResponse('Forbidden', status=403)
    # very important: protects against pulling other files
    if not ModelDB.has_model(model_id):
        return HttpResponse('Forbidden', status=403)
    filename = f'{model_id}.zip'
    response = HttpResponse(content_type="application/zip")
    response['Content-Disposition'] = f'attachment; filename={filename}'
    response.write(ModelDB.model(model_id).zip_file())
    return response

def _remap_src(model_id, match, base_filename):
    match_text = match.group()
    src = match_text[5:-1]
    src_lower = src.lower()
    print('_remap_src', src_lower)
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
    print('_remap_src', src_lower)
    if src_lower.startswith('http://') or src_lower.startswith('//') or src_lower.startswith('https://'):
        # TODO: we probably don't want this at all, but not clear what it's trying to do
        src = re.sub(r'(?i)(https?:)?//senselab\.med\.yale\.edu/', '/', src)
    return f'href="{src}"'

@xframe_options_exempt
def download(request):
    model_id = request.GET.get('model', -1)
    if model_id == -1:
        return HttpResponse('Forbidden', status=403)
    model = ModelDB.model(model_id)
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
                if extension == 'hoc':
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