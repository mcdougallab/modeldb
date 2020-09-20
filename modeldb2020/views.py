import re
import html
import json
import os
import datetime
import smtplib
import heapq
import collections
import itertools
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlencode
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import ensure_csrf_cookie
from . import settings
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
from .models import Paper


ModelDB = models.ModelDB()

# need this because f-strings cannot include a backslash
_newline = "\n"


def index(request):
    context = {"title": "ModelDB", "ModelDB": ModelDB, "request": request}
    return render(request, "index.html", context)


def _id_and_name(data):
    return sorted(
        [(item["id"], item["name"]) for item in data.values()], key=lambda item: item[1]
    )


def sendmail(
    to, subject, msg, msg_html=None, sent_by="ModelDB Curator <curator@modeldb.science>"
):
    server_name = settings.security.get("smtp_server")
    smtp_user = settings.security.get("smtp_user")
    smtp_password = settings.security.get("smtp_password")
    if server_name and smtp_user and smtp_password:
        server = smtplib.SMTP(server_name)
        server.starttls()
        server.login(smtp_user, smtp_password)
        if not msg_html:
            msg = f"""To: {to}
    From: {sent_by}
    Subject: {subject}
    {msg}"""
        else:
            my_msg = MIMEMultipart("alternative")
            my_msg["Subject"] = subject
            my_msg["From"] = sent_by
            my_msg["To"] = to
            my_msg.attach(MIMEText(msg, "plain"))
            my_msg.attach(MIMEText(msg_html, "html"))
            msg = my_msg.as_string()
        server.sendmail(sent_by, to, msg)
        server.quit()
    else:
        print("not sending email; smtp not setup")


def private_models(request):
    # note that find_private_models reads every zip file, which could potentially be a bottleneck
    if all_model_access(request):
        context = {
            "title": "ModelDB: Private Models",
            "request": request,
            "obj": {"classname": "Private Models",},
            "models": ModelDB.find_private_models(),
            "hide_header": True,
        }
        return render(request, "modellist.html", context)
    else:
        return redirect(f"/login?next={request.path}")


def all_model_access(request):
    # TODO: this should really be about the users authentication level not the simple act of being authenticated
    return request.user.is_authenticated


def unprocessed_refs_access(request):
    # TODO: this should really be about the users authentication level not the simple act of being authenticated
    return request.user.is_authenticated


def list_by_any_author(request):
    return _display_author_list(request, models.all_authors, "Model Authors")


def list_by_first_author(request):
    return _display_author_list(request, models.first_authors, "Model First Authors")


def _display_author_list(request, authors, kind):
    order = sorted(authors)
    data = [{"n": name, "c": len(authors[name])} for name in order]
    context = {
        "kind": kind,
        "datajson": json.dumps(data),
        "title": f"ModelDB: {kind}",
        "request": request,
    }
    return render(request, "listbyauthor.html", context)


def _filter_models_for_top_category(the_models, category, container, ignore=None):
    items = []
    for model in the_models:
        my_items = model._model.get(category)
        if my_items is not None:
            items.extend(
                [
                    item["object_id"]
                    for item in my_items["value"]
                    if item["object_name"] != ignore
                ]
            )
    items = collections.Counter(items).most_common(10)
    items = [
        (item[0], container[str(item[0])]["name"], item[1])
        for item in items
        if str(item[0]) in container
    ]
    return items


def modelauthor(request, author=None, kind=None):
    # kind should be either "first" or "model"
    if kind == "first":
        authors = models.first_authors
    elif kind == "model":
        authors = models.all_authors
    else:
        # should never get here
        return HttpResponse("404 not found", status=404)
    if author not in authors:
        return HttpResponse("404 not found", status=404)
    the_models = sorted(
        [models.Model(entry, files_needed=False) for entry in authors[author]],
        key=lambda model: model.name,
    )
    concepts = _filter_models_for_top_category(
        the_models, "model_concept", modelconcepts
    )
    neurons = _filter_models_for_top_category(the_models, "neurons", celltypes)

    # find the set of all papers, drop duplicates
    papers_all = itertools.chain.from_iterable([model.papers for model in the_models])
    papers = []
    paper_ids = set()
    for paper in papers_all:
        paper_id = paper.id
        if paper_id not in paper_ids:
            papers.append(paper)
            paper_ids.add(paper_id)

    coauthors = [
        name
        for name in itertools.chain.from_iterable([paper.authors for paper in papers])
        if name != author
    ]
    coauthors = collections.Counter(coauthors).most_common(10)
    context = {
        "title": f"ModelDB: {author}",
        "content": author + kind,
        "kind": kind,
        "author": author,
        "num_first_author": len(models.first_authors.get(author, [])),
        "num_author": len(models.all_authors.get(author, [])),
        "models": the_models,
        "coauthors": coauthors,
        "concepts": concepts,
        "neurons": neurons,
    }
    return render(request, "modelauthor.html", context)


def models_with_uncurated_references(request):
    if unprocessed_refs_access(request):
        uncurated_models = models.models_with_uncurated_papers()
        context = {"request": request, "models": uncurated_models}
        return render(request, "models-with-uncurated-references.html", context)
    else:
        return redirect(f"/login?next={request.path}")


def process_model_submit(request):
    from email.utils import parseaddr

    # TODO: probably some of this should move into models?
    the_file = request.FILES["zipfile"]
    filename = the_file.name
    if not filename.lower().endswith(".zip"):
        return HttpResponse(
            "403 Forbidden: non-zip upload; hit back and try again", status=403
        )

    # a little error checking on the emails
    modeler_email = parseaddr(request.POST["modeleremail"])[1]
    if "@" not in modeler_email or "." not in modeler_email:
        return HttpResponse(
            "403 Forbidden: invalid email; hit back and try again", status=403
        )

    new_id = models.new_object_id()
    # store the file
    with open(
        os.path.join(settings.security["modeldb_private_zip_dir"], f"{new_id}.zip"),
        "wb",
    ) as f:
        for chunk in the_file.chunks():
            f.write(chunk)

    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    entry = {
        "id": int(new_id),
        "name": request.POST.get("name"),
        "created": now,
        "ver_number": 1,
        "ver_date": now,
        "class_id": 19,
        "notes": {"value": request.POST.get("notes"), "attr_id": 24},
        "license": request.POST.get("license"),
        "expmotivation": request.POST.get("expmotivation"),
        "public_submitter_email": {"value": modeler_email, "attr_id": 309,},
        "data_to_curate": {
            "rwac": models.get_salted_code(request.POST["rwac"]),
            "othertags": request.POST.get("othertags"),
            "citation": request.POST.get("citation"),
            "implementers": request.POST.get("implementers"),
            "modelername": request.POST.get("modelername"),
        },
    }

    if request.POST.get("rac"):
        entry["data_to_curate"]["rac"] = models.get_salted_code(request.POST["rac"])

    _process_submit_list(request, "celltypes", "neurons", 25, entry)
    _process_submit_list(request, "receptors", "receptors", 26, entry)
    _process_submit_list(request, "currents", "currents", 27, entry)
    _process_submit_list(request, "neurotransmitters", "neurotransmitters", 28, entry)
    _process_submit_list(request, "model_type", "model_type", 112, entry)
    _process_submit_list(request, "concepts", "model_concept", 113, entry)
    _process_submit_list(request, "simenvironment", "modeling_application", 114, entry)
    _process_submit_list(request, "gene", "gene", 476, entry)
    _process_submit_list(request, "region", "region", 471, entry)
    _process_submit_list(request, "model_type", "model_type", 112, entry)

    models.add_private_model(entry)

    sendmail(
        modeler_email,
        f"Your New ModelDB Entry: {new_id}",
        f"""
Dear {request.POST.get("modelername", "modeler")},

This URL reminder was automatically generated from the ModelDB web site
in response to a model submission which you just submitted:
http://modeldb.science/{new_id}

Thank you for your contribution to open science!

Remember you must open your model entry and click "request to make public"
before the model will be publicly accessible. In the meantime, you can use
the read-write access code to modify your entry, or you may share the 
read access code with e.g. your paper reviewers.

If you are receiving this in error, you may safely ignore this message,
or reply to let us know about the issue.

Thank you,

The ModelDB Group
""",
    )

    context = {
        "title": "Model upload successful",
        "request": request,
        "accession_number": new_id,
    }
    return render(request, "processmodelsubmit.html", context)


def _process_submit_list(request, listname, fieldname, attr_id, entry):
    objs = [
        {"object_id": int(id_), "object_name": ModelDB.object_by_id(id_).name}
        for id_ in request.POST.getlist(listname)
    ]
    if objs:
        entry[fieldname] = {"value": objs, "attr_id": attr_id}


def submit_model(request):
    metadata = [
        ["Model type", "model_type", _id_and_name(modeltypes)],
        ["Neurons", "celltypes", _id_and_name(celltypes)],
        ["Currents", "currents", _id_and_name(currents)],
        ["Neurotransmitters", "neurotransmitters", _id_and_name(transmitters)],
        ["Receptors", "receptors", _id_and_name(receptors)],
        ["Genes", "gene", _id_and_name(genes)],
        ["Concepts", "concepts", _id_and_name(modelconcepts)],
        ["Region or organism", "region", _id_and_name(regions)],
        ["Simulation environment", "simenvironment", _id_and_name(simenvironments)],
    ]
    context = {"title": "Submit Model", "request": request, "metadata": metadata}
    return render(request, "submitmodel.html", context)


def static(request, page="", title=""):
    context = {"title": f"ModelDB: {title}", "request": request}
    return render(request, f"{page}.html", context)


def modellist(request):
    object_id = request.GET.get("id")
    all_simu = request.GET.get("all_simu", "")
    if object_id is None:
        return listbymodelname(request)

    obj = ModelDB.object_by_id(object_id)
    if obj is None:
        return listbymodelname(request)

    if isinstance(obj, models.SimEnvironment) and all_simu.lower() == "true":
        name = obj.name.strip()
        i = name.find("(web link")
        if i >= 0:
            name = name[:i].strip()
        my_models = []
        for sim_env_id, sim_env in simenvironments.items():
            sim_name = sim_env["name"].strip()
            if sim_name == name or sim_name.startswith(f"{name} (web link"):
                # this next if ensures we're always using the non-web-link information in the all_simu case
                if sim_name == name:
                    obj = models.SimEnvironment(sim_env_id)
                # be sure not to list the same model twice
                prior_ids = set([model.id for model in my_models])
                my_models += [
                    models.Model(model["id"], files_needed=False)
                    for model in models.SimEnvironment(sim_env_id).models()
                    if model["id"] not in prior_ids
                ]
    else:
        my_models = [
            models.Model(model["id"], files_needed=False) for model in obj.models()
        ]

    # find the set of all papers, drop duplicates
    papers_all = itertools.chain.from_iterable([model.papers for model in my_models])
    papers = []
    paper_ids = set()
    for paper in papers_all:
        paper_id = paper.id
        if paper_id not in paper_ids:
            papers.append(paper)
            paper_ids.add(paper_id)

    authors = [
        name
        for name in itertools.chain.from_iterable([paper.authors for paper in papers])
    ]
    authors = collections.Counter(authors).most_common(10)

    ref_count = models.count_references(my_models)
    top_refs = [
        {
            "id": paper_id,
            "text": models.Paper(paper_id).text,
            "count": ref_count[paper_id],
        }
        for paper_id in heapq.nlargest(5, ref_count, key=lambda item: ref_count[item])
    ]

    concepts = _filter_models_for_top_category(
        my_models, "model_concept", modelconcepts, ignore=obj.name
    )
    neurons = _filter_models_for_top_category(
        my_models, "neurons", celltypes, ignore=obj.name
    )
    my_currents = _filter_models_for_top_category(
        my_models, "currents", currents, ignore=obj.name
    )

    seealso = {}
    more_info = ""
    logo = None
    homepage = None
    object_id = str(object_id)
    if object_id == "3537":
        seealso = {
            cell["name"]: f"?id={cell['id']}"
            for cell in sorted(celltypes.values(), key=lambda item: item["name"])
        }
    elif object_id == "3540":
        seealso = {
            channel["name"]: f"?id={channel['id']}"
            for channel in sorted(currents.values(), key=lambda item: item["name"])
        }
    elif "children" in obj._data:
        children = [ModelDB.object_by_id(_id) for _id in obj._data["children"]]
        seealso = {child.name: f"?id={child._id}" for child in children}
    if object_id in simenvironments:
        simenv = simenvironments[object_id]
        try:
            more_info = simenv["description"]["value"]
        except:
            pass
        try:
            logo = simenv["logo"]["value"][0]
        except:
            logo = None
        try:
            homepage = simenv["homepage"]["value"]
        except:
            homepage = None

    # logos do not work well on the page; remove
    logo = None

    context = {
        "title": f"ModelDB: Models that contain {obj.name}",
        "obj": obj,
        "seealso": seealso,
        "moreinfo": more_info,
        "logo": logo,
        "homepage": homepage,
        "authors": authors,
        "concepts": concepts,
        "neurons": neurons,
        "currents": my_currents,
        "top_refs": top_refs,
        "all_simu": all_simu,
        "models": my_models,
    }
    return render(request, "modellist.html", context)


def ptrm(request):
    context = {
        "title": "Papers that reference ModelDB",
        "datajson": json.dumps(
            [
                {"p": paper.html, "u": paper.modeldb_usage}
                for paper in ModelDB.paper_mentions
            ]
        ),
    }
    return render(request, "ptrm.html", context)


@ensure_csrf_cookie
def models_requested_public(request):
    if all_model_access(request):
        context = {
            "title": "ModelDB: models requested to be made public",
            "datajson": json.dumps(
                [
                    {"id": model.id, "t": model.name}
                    for model in ModelDB.get_requested_public()
                ]
            ),
        }
        return render(request, "models-requested-public.html", context)
    else:
        return redirect(f"/login?next={request.path}")


def listbymodelname(request):
    context = {"title": "ModelDB: Models List", "all_models": ModelDB.models_by_name()}
    return render(request, "listbymodelname.html", context)


def my_logout(request):
    logout(request)
    next_url = request.GET.get("next")
    if next_url:
        return redirect(next_url)
    else:
        return redirect("/")


def my_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if password is not None:
        user = authenticate(username=username, password=password)
        next_url = request.POST.get("next", "/")
        if user is not None:
            login(request, user)
            return redirect(next_url)
    else:
        next_url = request.GET.get("next", "/")
    context = {"next": next_url}
    context.update(base_context)
    return render(request, "login.html", context)


def rwac_reset_p(request, code=None):
    data = models.rwac_reset_model(code)
    if not data:
        context = {"title": "Invalid Access Code Reset Link"}
        return render(request, "rwac_reset0.html", context)
    model_id = data["model"]
    if not ModelDB.has_private_model(model_id):
        # no longer a private model; could be deleted or public
        context = {"title": "Invalid Access Code Reset Link"}
        return render(request, "rwac_reset0.html", context)
    new_rwac = request.POST.get("rwac")
    if new_rwac:
        models.update_rwac(model_id, new_rwac)
        models.invalidate_rwac_reset_code(code)
        context = {"model": model_id, "title": "Change successful"}
        return render(request, "rwac_reset4.html", context)
    else:
        context = {
            "model": model_id,
            "title": "Enter new read-write access code",
            "code": code,
        }
        return render(request, "rwac_reset3.html", context)


def rwac_reset(request, model_id=None):
    if not ModelDB.has_private_model(model_id):
        # can only reset private models
        return HttpResponse("404 not found", status=404)
    email = request.POST.get("email")
    context = {"model": model_id, "title": "Access Code Reset Request"}
    if email:
        model = models.PrivateModel(model_id)
        model_email = model.public_submitter_email.strip()
        if model_email == email.strip():
            code = models.new_rwac_reset(model_id)
            print(f"emails match; code = {code}")
            sendmail(
                model_email,
                f"ModelDB Access Code Reset: Model {model_id}",
                f"""To reset your ModelDB read-write access code for Model {model_id},
please visit:

http://modeldb.science/rwac-reset/p{code}

within the next hour.""",
                f"""To reset your ModelDB read-write access code for Model {model_id},
please visit:
<br><br>
<a href="http://modeldb.science/rwac-reset/p{code}">http://modeldb.science/rwac-reset/p{code}</a>
<br><br>
within the next hour.""",
            )

        else:
            print("emails do not match")
        return render(request, "rwac_reset2.html", context)
    else:
        return render(request, "rwac_reset.html", context)


def showmodel_redirect(request, model_id=None, tab_id=None, filename=None):
    # TODO: handle filename
    if model_id is None:
        return HttpResponse("404 not found", status=404)
    try:
        m = int(model_id)
    except ValueError:
        return HttpResponse("404 not found", status=404)
    # TODO: handle a missing model more gracefully
    if (not ModelDB.has_model(model_id)) and (not ModelDB.has_private_model(model_id)):
        return HttpResponse("404 not found", status=404)
    if tab_id is None:
        tab_id = int(request.GET.get("tab", 1))
    if tab_id == 1:
        tab_string = ""
    else:
        tab_string = f"&tab={tab_id}"
    return redirect(f"/showmodel?model={model_id}{tab_string}")


def search_redirect(request):
    args = urlencode(request.GET)
    return redirect(f"/search?{args}")


def uri_cleanup_redirect(request, uri=None):
    uri_lower = uri.lower()
    if uri_lower[-5:] == ".html":
        uri = uri[:-5]
    elif uri_lower[-7:] == ".cshtml":
        uri = uri[:-7]

    args = urlencode(request.GET)
    if not args:
        return redirect(f"/{uri}")
    else:
        return redirect(f"/{uri}?{args}")


def forget_access(request):
    model_id = request.GET.get("model", -1)
    request.session[model_id] = None
    del request.session[model_id]
    return showmodel_redirect(request, model_id=model_id)


def _showmodel_edit_context(full_collection, present):
    return {
        "all": _id_and_name(full_collection),
        "present": [item["object_id"] for item in present.get("value", [])],
    }


@ensure_csrf_cookie
def showmodel(request):
    model_id = request.GET.get("model", -1)
    tab_id = int(request.GET.get("tab", 1))
    filename = request.GET.get("file")
    access = None

    # TODO: handle not having a model argument more gracefully
    if model_id == -1:
        model_id = request.POST.get("model")
        if model_id is None:
            return HttpResponse("404 not found", status=404)
        else:
            tab_id = int(request.POST.get("tab", 1))
            filename = request.POST.get("file")

    if not ModelDB.has_model(model_id):
        if ModelDB.has_private_model(model_id):
            access = request.session.get(model_id)
            if all_model_access(request):
                access = "rw"
            if access is None:
                code = request.POST.get("access_code")
                # TODO: refactor this block of code; it is repetitive
                if code is None:
                    context = {
                        "request": request,
                        "title": "Private model access",
                        "msg": "",
                        "tab_id": tab_id,
                        "model": int(model_id),
                        "file": filename,
                    }
                    return render(request, "showmodel_login.html", context)
                else:
                    access = ModelDB.auth_private_model(model_id, code)
                    if access is not None:
                        request.session[model_id] = access
                        return showmodel_redirect(
                            request, model_id=model_id, tab_id=tab_id, filename=filename
                        )
                    else:
                        context = {
                            "request": request,
                            "title": "Private model access",
                            "msg": "Login failed; try again.",
                            "tab_id": tab_id,
                            "model": int(model_id),
                            "file": filename,
                        }
                    return render(request, "showmodel_login.html", context)
            model = ModelDB.private_model(model_id)
        else:
            # TODO: handle a missing model more gracefully
            return HttpResponse("404 not found", status=404)
    else:
        model = ModelDB.model(model_id)

    if tab_id == 7:
        papers = model.papers
        citation_data = _prep_citations(papers)
        context = {
            "title": "ModelDB: Model Citations",
            "Model": model,
            "tab": tab_id,
            "citation_data": citation_data,
            "showtabs": True,
        }
        return render(request, "showmodel7.html", context)
    elif tab_id == 4:
        params = model.modelview("parameters")
        if params is not None and "by_file" in params:
            params["by_file"].sort(key=lambda item: item["filename"])
        context = {
            "title": "ModelDB: Parameters",
            "Model": model,
            "tab": tab_id,
            "showtabs": True,
            "data": params,
        }
        return render(request, "showmodel4.html", context)
    else:
        if tab_id != 2:
            filename = model.readme_file
            filename = filename.replace("\\", "/").strip("/")
        elif tab_id == 2 and filename is None:
            filename = model.readme_file
            filename = filename.replace("\\", "/").strip("/").split("/")[0]

        original_file_valid = model.has_path(filename)
        if not original_file_valid:
            filename = model.readme_file
        is_folder = model.has_folder(filename)
        original_filename = filename
        filename = filename.split("/")
        breadcrumbs = []
        for i, name in enumerate(filename):
            link = (
                f'/showmodel?tab=2&model={model_id}&file={"/".join(filename[0: i + 1])}'
            )
            breadcrumbs.append(f'<a href="{link}">{name}</a>')
        if original_file_valid:
            breadcrumbs[-1] = name
        else:
            breadcrumbs[
                0
            ] = f'<span style="color:red!important">Requested file does not exist</span>; showing {breadcrumbs[0]}'

        if is_folder:
            content = model.folder_contents(original_filename)
        else:
            content = "foo"  # TODO: this probably shouldn't be this way

        context = {
            "title": "ModelDB: Show Model",
            "Model": model,
            "breadcrumbs": breadcrumbs,
            "is_folder": is_folder,
            "content": content,
            "filename": original_filename,
            "tab": tab_id,
            "access": access,
            "extension": original_filename.split(".")[-1].lower(),
        }
        if access == "rw":
            context["neurons"] = _showmodel_edit_context(celltypes, model.neurons)
            context["currents"] = _showmodel_edit_context(currents, model.currents)
            context["receptors"] = _showmodel_edit_context(receptors, model.receptors)
            context["region"] = _showmodel_edit_context(regions, model.region)
            context["model_type"] = _showmodel_edit_context(
                modeltypes, model.model_type
            )
            context["gene"] = _showmodel_edit_context(genes, model.gene)
            context["neurotransmitters"] = _showmodel_edit_context(
                transmitters, model.neurotransmitters
            )
            context["model_concept"] = _showmodel_edit_context(
                modelconcepts, model.model_concept
            )
            context["modeling_application"] = _showmodel_edit_context(
                simenvironments, model.modeling_application
            )
        if tab_id == 2:
            if not is_folder:
                file_contents = model.file(original_filename)
                duplicate_files = [
                    row
                    for row in models.files_with_matching_hash(file_contents)
                    if row["model_id"] != int(model_id)
                ]
                duplicate_files_by_model = {}
                for row in duplicate_files:
                    duplicate_files_by_model.setdefault(row["model_id"], [])
                    duplicate_files_by_model[row["model_id"]].append(row)
                duplicate_files_final = []
                for model, data in duplicate_files_by_model.items():
                    name = models.Model(model, files_needed=False).name
                    duplicate_files_final.append(
                        {"model_name": name, "model": model, "data": data}
                    )
                context["duplicate_files"] = duplicate_files_final
            context["is_mod_file"] = original_filename.lower().endswith(".mod")
            if context["is_mod_file"]:
                context["has_celsius"] = b"celsius" in file_contents
                mod_name = name[:-4]  # throw away the .mod
                model_id_int = int(model_id)
                try:
                    icg_data = models.icg[int(model_id)][mod_name]
                except KeyError:
                    icg_data = None
                context["icg_data"] = icg_data
            return render(request, "showmodel2.html", context)
        else:
            return render(request, "showmodel.html", context)


def mdbcitations(request):
    # TODO: probably can't always assume ints? maybe should recast existing to str?
    paper_id = str(request.GET.get("id", -1))
    # TODO: handle not having a model argument more gracefully
    if paper_id == "-1":
        return HttpResponse("Forbidden", status=403)
    # TODO: we actually know what datatype this is
    papers = [ModelDB.object_by_id(paper_id)]
    citation_data = _prep_citations(papers)
    context = {
        "title": "ModelDB: Paper information",
        "Model": None,
        "citation_data": citation_data,
        "showtabs": False,
    }
    return render(request, "showmodel7.html", context)


def _prep_citations(papers):
    references = [[paper for paper in model_paper.references] for model_paper in papers]
    sorted_references = []
    for reference_group in references:
        tmp_sorted_list = sorted(reference_group, key=paper_sort_rule)
        sorted_references.append(tmp_sorted_list)
    # citations = [[paper.html for paper in model_paper.citations] for model_paper in papers]
    citations = [[paper for paper in model_paper.citations] for model_paper in papers]
    sorted_citations = []
    for citation_group in citations:
        # tmp_sorted_list=sorted(citation_group, key=lambda item: item.authors+[item.year])
        tmp_sorted_list = sorted(citation_group, key=paper_sort_rule)
        # except:
        #    tmp_sorted_list = citation_group
        sorted_citations.append(tmp_sorted_list)
    return zip(papers, sorted_references, sorted_citations)


def download_zip(request):
    model_id = request.GET.get("o", -1)
    model = _get_model(request, model_id)
    if model is None:
        return HttpResponse("Forbidden", status=403)
    filename = f"{model_id}.zip"
    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={filename}"
    response.write(model.zip_file())
    return response


def _remap_src(model_id, match, base_filename):
    match_text = match.group()
    src = match_text[5:-1]
    src_lower = src.lower()
    if (
        src_lower.startswith("http://")
        or src_lower.startswith("//")
        or src_lower.startswith("https://")
    ):
        # TODO: we probably don't want this at all, but not clear what it's trying to do
        src = re.sub(r"(?i)(https?:)?//senselab\.med\.yale\.edu/", "/", src)
    else:
        while base_filename.startswith("/"):
            base_filename = base_filename[1:]
        src = f"/getmodelfile?model={model_id}&file={base_filename}{src}"
        src = src.replace("/./", "/").replace("//", "/")
    return 'src="' + src + '"'


def _remap_href(model_id, match, base_filename):
    match_text = match.group()
    src = match_text[6:-1]
    src_lower = src.lower()
    if (
        src_lower.startswith("http://")
        or src_lower.startswith("//")
        or src_lower.startswith("https://")
    ):
        # TODO: we probably don't want this at all, but not clear what it's trying to do
        src = re.sub(r"(?i)(https?:)?//senselab\.med\.yale\.edu/", "/", src)
    return f'href="{src}"'


def _get_model(request, model_id, permissions=None):
    if permissions is None:
        permissions = ["r", "rw"]
    elif isinstance(permissions, str):
        permissions = [permissions]
    if ModelDB.has_model(model_id):
        model = ModelDB.model(model_id)
    elif ModelDB.has_private_model(model_id) and (
        request.session.get(model_id) in permissions or all_model_access(request)
    ):
        model = ModelDB.private_model(model_id)
    else:
        model = None
    return model


@xframe_options_sameorigin
def download(request):
    model_id = request.GET.get("model", -1)
    model = _get_model(request, model_id)
    if model is None:
        return HttpResponse("Forbidden", status=403)
    filename = request.GET.get("file")
    if not model.has_path(filename):
        return HttpResponse("Forbidden", status=403)
    embed = request.GET.get("embed", "").lower() == "true"
    contents = model.file(filename)
    # discard path information; only keep filename
    filename = filename.replace("\\", "/")
    short_filename = filename.split("/")[-1]
    base_filename = filename[: -len(short_filename)]
    filename = short_filename
    if embed:
        response = HttpResponse()
        extension = filename.split(".")[-1].lower()
        if extension in ("html", "htm"):
            contents = contents.decode("utf-8")
            contents = re.sub(
                "src=\"(.*?)\"|src='(.*?)'",
                lambda match: _remap_src(model_id, match, base_filename),
                contents,
            )
            contents = re.sub(
                "href=\"(.*?)\"|href='(.*?)'",
                lambda match: _remap_href(model_id, match, base_filename),
                contents,
            )
            # have to specify a base target otherwise will try to load links inside the iframe
            contents = f'<base target="_parent">{contents}'
        else:
            try:
                # TODO: be smarter about handling extensions
                # workaround for HOC using C
                if extension in ("hoc", "ses"):
                    extension = "c"
                if extension in (
                    "py",
                    "cpp",
                    "c",
                    "bas",
                    "js",
                    "cxx",
                    "h",
                    "f90",
                    "f95",
                    "json",
                    "java",
                    "md",
                    "r",
                    "sql",
                    "vba",
                    "vbs",
                    "yaml",
                    "yml",
                    "pl",
                    "lisp",
                    "lua",
                    "hs",
                    "go",
                    "css",
                    "c++",
                    "hpp",
                    "cs",
                ):
                    contents = f'<link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.14.2/styles/vs.min.css" rel="stylesheet" /><script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.14.2/highlight.min.js"></script><script>hljs.initHighlightingOnLoad();</script><pre><code class="{extension}">{html.escape(contents.decode("utf-8"))}</code></pre>'
                else:
                    contents = f'<pre>{html.escape(contents.decode("utf-8"))}</pre>'
            except:
                contents = "This file is not encoded as UTF-8. Download it to view."
            contents = f"<html><body>{contents}</body></html>"
    else:
        response = HttpResponse(content_type="application/octet-stream")
        response["Content-Disposition"] = f"attachment; filename={filename}"
    response.write(contents)
    return response


def paper_sort_rule(item):
    if item.authors:
        return item.authors + [item.year]
    else:
        return [item.name, item.year]


def model_sort_rule(item):
    return item.name.lower()


def findbyregionlist(request):
    context = {
        "title": "ModelDB: Browse by current",
        "content": _render_tree(celltypes, "/ModelList"),
        "header": "Find models of a particular neuron",
        "subhead": "Click on a neuron/cell to show a list of models of that type.",
    }
    return render(request, "treepage.html", context)


def trends(request):
    filters = [
        (
            "modelconcepts",
            sorted(
                [(item["id"], item["name"]) for item in modelconcepts.values()],
                key=lambda item: item[1],
            ),
            "model concept",
        ),
        (
            "simenvironments",
            sorted(
                [(item["id"], item["name"]) for item in simenvironments.values()],
                key=lambda item: item[1],
            ),
            "simulation environment",
        ),
        (
            "celltypes",
            sorted(
                [(item["id"], item["name"]) for item in celltypes.values()],
                key=lambda item: item[1],
            ),
            "cell type",
        ),
        (
            "currents",
            sorted(
                [(item["id"], item["name"]) for item in currents.values()],
                key=lambda item: item[1],
            ),
            "current",
        ),
    ]
    context = {"title": "Models by create date", "request": request, "filters": filters}
    return render(request, "modelsbycreatedate.html", context)


def findbycurrent(request):
    context = {
        "title": "ModelDB: Browse by current",
        "content": _render_tree(currents, "/ModelList"),
        "header": "Find models that contain a particular ionic current",
        "subhead": 'Click on an ionic current to show a list of models that contain or implement that current.<br/><br/>Click <a href="https://senselab.med.yale.edu/neurondb/ndbregions">here</a> to view brief definitions of currents in NeuronDB.',
    }
    return render(request, "treepage.html", context)


def findbyreceptor(request):
    context = {
        "title": "ModelDB: Browse by receptor",
        "content": _render_tree(receptors, "/ModelList"),
        "header": "Find models that contain a particular ionic current",
        "subhead": "Click on a receptor to show a list of models that contain or implement that receptor.<br/>",
    }
    return render(request, "treepage.html", context)


def findbytransmitter(request):
    context = {
        "title": "ModelDB: Browse by neurotransmitter",
        "content": _render_tree(transmitters, "/ModelList"),
        "header": "Find models that contain a particular neurotransmitter",
        "subhead": "Click on a neurotransmitter to show a list of models that implement a mechanism for release of that transmitter.<br/>",
    }
    return render(request, "treepage.html", context)


def findbygene(request):
    context = {
        "title": "ModelDB: Browse by gene",
        "content": _render_tree(genes, "/ModelList"),
        "header": "Find models containing a particular gene",
        "subhead": "Click on a gene name to show a list of electrical or chemical models of the associated channel or receptor.<br/>",
    }
    return render(request, "treepage.html", context)


def findbyconcept(request):
    context = {
        "title": "ModelDB: Browse by concept",
        "content": _render_tree(modelconcepts, "/ModelList"),
        "header": "Find models by concept",
        "subhead": "Click on a concept to show a list of models that incorporate or demonstrate that concept.<br/>",
    }
    return render(request, "treepage.html", context)


def findbysimulator(request):
    counts = ModelDB.simenvironment_counts
    counts_processed = {}
    for key, value in counts.items():
        key = str(key)
        name = simenvironments[str(key)]["name"].strip()
        i = name.find("(web link")
        if i >= 0:
            short_name = name[:i].strip()
        else:
            short_name = name

        if short_name not in counts_processed:
            counts_processed[short_name] = {
                "name": short_name,
                "link": 0,
                "hosted": 0,
                "id": 0,
                "linkid": 0,
                "total": 0,
            }
        item = counts_processed[short_name]
        if "(web link" in name:
            item["link"] += value
            item["linkid"] = key
        else:
            item["hosted"] += value
            item["id"] = key
        item["total"] += value

    context = {
        "title": "ModelDB: Browse by simulation environment",
        "counts": sorted(
            counts_processed.values(), key=lambda item: item["name"].lower()
        ),
        "header": "Find models by simulation environment",
        "subhead": "Click on a link to show a list of models implemented in that simulation environment or programming language.<br/>",
    }
    return render(request, "findbysimulator.html", context)


def _render_tree_element(obj, collection, base_link):
    subtree = ""
    if "children" in obj:
        subtree = f"<ul>{_newline.join(_render_tree_element(collection[child], collection, base_link) for child in sorted(obj['children'], key=lambda _id: collection[_id]['name'].lower()))}</ul>"
    return f'<li><a href="{base_link}?id={obj["id"]}">{obj["name"]}{subtree}</a></li>'


def _render_tree(collection, base_link):
    root_nodes = [
        item
        for item in collection.values()
        if not "parent" in item or item["parent"] is None
    ]
    root_nodes = sorted(root_nodes, key=lambda obj: obj["name"].lower())
    return f"<ul>{_newline.join(_render_tree_element(node, collection, base_link) for node in root_nodes)}</ul>"


def _update_search_query(query, item, name):
    if item:
        query.append({"name": name, "search": item.strip(";")})


def _parse_search(item):
    if item:
        return [term.strip() for term in item.split(";")]
    else:
        return []


def _get_names(collection_data):
    return json.dumps(sorted([item["name"] for item in collection_data.values()]))


def top_papers(request):
    import time

    ref_count = models.count_references()
    top_refs = [
        {
            "id": int(paper_id),
            "p": models.Paper(paper_id).text,
            "c": ref_count[paper_id],
        }
        for paper_id in heapq.nlargest(100, ref_count, key=lambda item: ref_count[item])
    ]
    context = {"title": "ModelDB: top cited papers", "datajson": json.dumps(top_refs)}
    return render(request, "top-papers.html", context)


def search(request):
    my_transmitters = request.GET.get("transmitters")
    my_receptors = request.GET.get("receptors")
    my_genes = request.GET.get("genes")
    my_simenvironment = request.GET.get("simenvironment")
    my_modelconcepts = request.GET.get("modelconcepts")
    my_celltypes = request.GET.get("celltypes")
    my_modeltype = request.GET.get("modeltype")
    my_brainregions = request.GET.get("brainregions")
    my_channels = request.GET.get("channels")
    my_authors = None
    my_title = request.GET.get("title")
    my_q = request.GET.get("q")

    if (
        my_transmitters
        or my_receptors
        or my_genes
        or my_simenvironment
        or my_modelconcepts
        or my_celltypes
        or my_modeltype
        or my_brainregions
        or my_channels
        or my_authors
        or my_title
    ) and (my_q is None):
        query = []
        _update_search_query(query, my_channels, "Currents")
        _update_search_query(query, my_transmitters, "Transmitters")
        _update_search_query(query, my_receptors, "Receptors")
        _update_search_query(query, my_genes, "Genes")
        _update_search_query(query, my_simenvironment, "Simulation Environment")
        _update_search_query(query, my_modelconcepts, "Model Concepts")
        _update_search_query(query, my_celltypes, "Cell Types")
        _update_search_query(query, my_modeltype, "Model Type")
        _update_search_query(query, my_brainregions, "Brain Region/Organism")
        _update_search_query(query, my_title, "Title")
        _update_search_query(query, my_authors, "Author")

        results = ModelDB.find_models(
            channels=_parse_search(my_channels),
            transmitters=_parse_search(my_transmitters),
            receptors=_parse_search(my_receptors),
            genes=_parse_search(my_genes),
            simenvironment=_parse_search(my_simenvironment),
            modelconcepts=_parse_search(my_modelconcepts),
            celltypes=_parse_search(my_celltypes),
            modeltype=_parse_search(my_modeltype),
            brainregions=_parse_search(my_brainregions),
            title=_parse_search(my_title),
            authors=_parse_search(my_authors),
        )

        # do the actual search
        context = {"title": "ModelDB: search", "query": query, "results": results}
        return render(request, "searchresults.html", context)
    elif my_q is not None:
        # remove excess whitespace
        my_q = my_q.strip()

        context = {
            "title": f"ModelDB: search: {my_q}",
            "query": my_q,
            "celltype_results": models.find_celltypes_by_name(my_q),
            "model_results": sorted(
                ModelDB.find_models(title=[my_q]), key=model_sort_rule
            ),
            "paper_results": sorted(
                models.find_papers_by_doi(my_q)
                + models.find_papers_by_author(my_q)
                + models.find_papers_by_title(my_q),
                key=paper_sort_rule,
            ),
            "author_results": sorted(models.find_authors(my_q)),
            "simenvironment_results": models.find_simenvironments_by_name(my_q),
            "current_results": models.find_currents_by_name(my_q),
            "concept_results": models.find_concepts_by_name(my_q),
            "region_results": models.find_regions_by_name(my_q),
            "receptor_results": models.find_receptors_by_name(my_q),
            "transmitter_results": models.find_transmitters_by_name(my_q),
            "gene_results": models.find_genes_by_name(my_q),
        }
        return render(request, "searchq.html", context)
    else:

        context = {
            "title": "ModelDB: search",
            "modeltype_tags": _get_names(modeltypes),
            "receptors_tags": _get_names(receptors),
            "genes_tags": _get_names(genes),
            "channels_tags": _get_names(currents),
            "brainregions_tags": _get_names(regions),
            "celltypes_tags": _get_names(celltypes),
            "modelconcepts_tags": _get_names(modelconcepts),
            "transmitters_tags": _get_names(transmitters),
            "simenvironment_tags": _get_names(simenvironments),
            "ModelDB": ModelDB,
        }
        return render(request, "search.html", context)
