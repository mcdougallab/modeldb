import json
import zipfile
import os
import hashlib
import threading
import shutil
import uuid
import time
import fnmatch
import bcrypt
from pymongo import MongoClient, ReturnDocument
from django.db import models
from . import settings
import pandas as pd
import itertools
import unicodedata
import re

mongodb = MongoClient()
sdb = mongodb[settings.security["db_name"]]
sdb.authenticate(settings.security["mongodb_user"], settings.security["mongodb_pw"])

network_models_pd = pd.read_csv(settings.security["network_info"]).to_dict("records")
network_models = {
    model["model"]: {key: value for key, value in model.items() if not pd.isna(value)}
    for model in network_models_pd
}
del network_models_pd


def regions_tree():
    result = {
        "Species": [],
        "Vertebrate regions": [],
        "Invertebrate regions": [],
        "Miscellaneous": [],
    }
    for r in sdb.regions.find():
        try:
            parent = r["parent"]["object_name"]
        except:
            continue
        result.setdefault(parent, []).append(r["id"])
    # make sure we end with miscellaneous
    misc = result["Miscellaneous"]
    del result["Miscellaneous"]
    result["Miscellaneous"] = misc
    return result


with open(settings.security["metadata-predictor-rules"], "r") as f:
    metadata_predictor_rules = json.load(f)

# metadata prediction code based on McDougal et al., 2019
token = re.compile("[a-zA-Z0-9]+")


# identify alternative models
alternative_models = {}
for model in sdb.models.find({"alternative_version": {"$exists": True}}):
    for ver in model["alternative_version"]["value"]:
        alternative_models[ver["object_id"]] = model["id"]


def tokenize(text):
    """not doing stop word removal"""
    return [word for word in token.findall(text)]


def get_n_grams_with_spaces(tokens, n):
    """return the n-grams comprised of consecutive tokens"""
    return [" %s " % " ".join(tokens[i : n + i]) for i in range(len(tokens) - n + 1)]


def an_item_matches(items, original_pattern):
    patterns = [
        ("(?i) (%s) " if pattern.islower() else " (%s) ") % pattern
        for pattern in original_pattern.split("$")
    ]
    for item in items:
        for pattern in patterns:
            if not re.search(pattern, item):
                break
        else:
            return True
    return False


def predict_metadata(text, check_new_match=True, check_fulltext_first=True):
    """takes a text, returns a list of predicted ModelDB terms"""
    dont_check_new_match = not check_new_match
    dont_check_fulltext_first = not check_fulltext_first
    tokens = tokenize(text)
    processed_text = [" %s " % " ".join(tokens)]
    n_grams = get_n_grams_with_spaces(tokens, 5)
    result = set([])
    for pattern, rule in metadata_predictor_rules.items():
        # only test a rule if it would give something new
        result_if_matched = result.union(rule)
        if dont_check_new_match or len(result_if_matched) > len(result):
            # check the full text first before running on all n-grams
            if dont_check_fulltext_first:
                if an_item_matches(n_grams, pattern):
                    result = result_if_matched
            elif an_item_matches(processed_text, pattern):
                if "$" not in pattern or an_item_matches(n_grams, pattern):
                    result = result_if_matched
    return sorted(
        [[item, _object_by_id(item).name] for item in result], key=lambda x: x[1]
    )


def clean_rwac_collection():
    """delete any rwac reset info that is over an hour old"""
    now = time.time()
    sdb.rwac_reset.delete_many({"time": {"$lt": now - 3600}})


def invalidate_rwac_reset_code(code):
    sdb.rwac_reset.delete_many({"code": code})


def update_rwac(model_id, new_rwac):
    model = sdb.private_models.find_one_and_update(
        {"id": int(model_id)},
        {"$set": {"data_to_curate.rwac": get_salted_code(new_rwac)}},
    )


def get_salted_code(code):
    return bcrypt.hashpw(code.encode("utf8"), bcrypt.gensalt()).decode("utf8")


def rwac_reset_model(code):
    """returns either the rwac reset info corresponding to code, or None if no such info.

    Note: this invalidates the code."""
    clean_rwac_collection()
    return sdb.rwac_reset.find_one({"code": code})


def new_rwac_reset(model_id):
    """return a code that can be used for a rwac reset within an hour"""
    now = time.time()
    clean_rwac_collection()
    code = uuid.uuid4().hex
    sdb.rwac_reset.insert_one({"model": model_id, "time": now, "code": code})
    return code


def get_health_about(object_id):
    concept = sdb.modelconcepts.find_one({"id": int(object_id)})
    if concept:
        return concept.get("health"), concept.get("general_info")
    else:
        return None, None


def new_object_id():
    """returns a new object id"""
    return sdb.meta.find_one_and_update(
        {}, {"$inc": {"id_count": 1}}, return_document=ReturnDocument.AFTER
    )["id_count"]


def add_private_model(entry):
    sdb.private_models.insert_one(entry)


def set_unprocessed_refs(paper_id, data):
    # TODO: make this more forgiving of lines with whitespace but no content
    id_ = new_object_id()
    lines = data.split("\n")
    items = []
    if "\n\n" in data:
        item = []
        for line in lines:
            if line:
                item.append(line)
            else:
                if item:
                    items.append("\n".join(item))
                item = []
        if item:
            items.append("\n".join(item))
    else:
        items = [line for line in lines if line]

    folder = os.path.join(settings.security["unprocessed_refs_dir"], str(id_))
    os.makedirs(folder)

    for i, item in enumerate(items):
        with open(os.path.join(folder, f"{i}.json"), "w") as f:
            content = {"text": item, "process_stage": 0}
            f.write(json.dumps(content))

    content = {"paper": paper_id, "ref_process_stage": [0 for item in items], "id": id_}

    sdb.unprocessed_refs.insert_one(content)

    return id_


# TODO: force object_id to be string here so we don't have to do it later
def load_collection(name):
    new_collection = {str(item["id"]): item for item in getattr(sdb, name).find()}
    if name != "regions":
        # expand parent data (if any) into reciprocal parent-child data
        for item in new_collection.values():
            if "parent" in item:
                item["parent"] = str(item["parent"])
                new_collection[item["parent"]].setdefault("children", [])
                new_collection[item["parent"]]["children"].append(str(item["id"]))
    return new_collection


# strip_accents from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
def strip_accents(s):
    s = unicodedata.normalize("NFD", s)
    s = re.sub(r"[\u0300-\u036f\u1dc0-\u1dff\u20d0-\u20ff\ufe20-\ufe2f]", "", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def has_accents(name):
    if strip_accents(name) == name:
        return False
    else:
        return True


def refresh():
    global modeldb, currents, genes, regions, receptors
    global transmitters, simenvironments, modelconcepts
    global modeltypes, celltypes, papers, cites_paper_unsorted
    global all_authors, all_author_accent_mapping, first_authors, icg, models_by_paper, ptrm
    global all_implementers

    modeldb = load_collection("models")
    currents = load_collection("currents")
    genes = load_collection("genes")
    regions = load_collection("regions")
    receptors = load_collection("receptors")
    transmitters = load_collection("transmitters")
    simenvironments = load_collection("simenvironments")
    modelconcepts = load_collection("modelconcepts")
    modeltypes = load_collection("modeltypes")
    celltypes = load_collection("celltypes")
    papers = load_collection("papers")
    icg = {item["id"]: item["data"] for item in sdb.icg.find()}
    models_by_paper = {}
    for model_id, model_data in modeldb.items():
        for item in model_data.get("model_paper", {"value": []})["value"]:
            models_by_paper.setdefault(item["object_id"], [])
            models_by_paper[item["object_id"]].append(model_id)

    all_authors = {}
    first_authors = {}
    all_implementers = {}

    no_authors_listed = "No authors listed"

    missing_papers = []
    for model in modeldb.values():
        if "implemented_by" in model:
            for implementer in model["implemented_by"]["value"]:
                name = implementer["object_name"]
                all_implementers.setdefault(name, [])
                all_implementers[name].append(model["id"])
        for paper in model.get("model_paper", {"value": []})["value"]:
            paper_id = str(paper["object_id"])
            if paper_id not in papers:
                missing_papers.append(paper_id)
                continue
            if "authors" not in papers[paper_id]:
                all_authors.setdefault(no_authors_listed, [])
                first_authors.setdefault(no_authors_listed, [])
                all_authors[no_authors_listed].append(model["id"])
                first_authors[no_authors_listed].append(model["id"])
            else:
                try:
                    for i, author in enumerate(papers[paper_id]["authors"]["value"]):
                        author_name = author["object_name"]
                        all_authors.setdefault(author_name, [])
                        all_authors[author_name].append(model["id"])
                        if i == 0:
                            first_authors.setdefault(author_name, [])
                            first_authors[author_name].append(model["id"])
                except KeyError:
                    pass

    if missing_papers:
        print("not all papers are present")
        print("fix this with:")
        print(
            "    python3 load_obj.py papers "
            + " ".join(str(item) for item in missing_papers)
        )
    all_authors = {name: list(set(models)) for name, models in all_authors.items()}
    first_authors = {name: list(set(models)) for name, models in first_authors.items()}

    # all_author_accent_mapping = {accentless_name: [accented_name1, accented_name2, ..]}
    all_author_accent_mapping = {}
    for author in all_authors:
        if has_accents(author):
            unaccented_name = strip_accents(author).lower()
            all_author_accent_mapping.setdefault(unaccented_name, []).append(author)

    # Prepare dictionary used to provide the "references that cite a paper" on citation display pages

    cites_paper_unsorted = {}  # will contain value key pairs like
    # cites_paper_unsorted[paper_obj_id]=[list of obj ids of refs that cite paper_obj_id]

    # Loop over all the papers.  Actually the citing_paper_obj_id is not necessarily "citing" until it is found to have refs a line below
    for citing_paper_obj_id, paper in papers.items():
        citing_paper_obj_id = str(citing_paper_obj_id)
        if "references" in paper:
            # loop over the list of references in the paper:
            for ref in paper["references"]["value"]:
                cited_paper_obj_id = str(ref["object_id"])
                cites_paper_unsorted.setdefault(cited_paper_obj_id, [])
                cites_paper_unsorted[cited_paper_obj_id].append(citing_paper_obj_id)

    # lowercase hack (TODO: should be in DB?)
    for paper in papers.values():
        if "doi" in paper and paper["doi"]["value"] is not None:
            paper["doi"]["value_lower"] = paper["doi"]["value"].lower().strip()

    # find papers that reference ModelDB (too expensive to be done as a search everytime)
    # TODO: could be done live if it was actually a DB query on an indexed field
    ptrm = []
    for paper_id in papers:
        paper = Paper(paper_id)
        if paper.modeldb_usage:
            ptrm.append(paper)


def find_celltypes_by_name(name):
    name = name.strip().lower()
    result = []
    if name:
        for id_, celltype in celltypes.items():
            if name in celltype["name"].lower():
                result.append(CellType(id_))
    return result


def _find_thing_by_name(name, collection, constructor):
    name = name.strip().lower()
    result = []
    if name:
        for id_, item in collection.items():
            if name in item["name"].lower():
                result.append(constructor(id_))
    return result


def find_currents_by_name(name):
    return _find_thing_by_name(name, currents, Current)


def find_simenvironments_by_name(name):
    return _find_thing_by_name(name, simenvironments, SimEnvironment)


def find_transmitters_by_name(name):
    return _find_thing_by_name(name, transmitters, Transmitter)


def find_receptors_by_name(name):
    return _find_thing_by_name(name, receptors, Receptor)


def find_concepts_by_name(name):
    return _find_thing_by_name(name, modelconcepts, ModelConcept)


def find_genes_by_name(name):
    return _find_thing_by_name(name, genes, Gene)


def find_regions_by_name(name):
    return _find_thing_by_name(name, regions, Region)


def find_papers_by_doi(doi):
    doi = doi.strip()
    if doi:
        result = sdb.papers.distinct(
            "id", {"doi.value": re.compile(re.escape(doi), re.IGNORECASE)}
        )
    else:
        result = []
    return [Paper(id) for id in result]

    """
    if doi:
        for paper in papers.values():
            if "doi" in paper and paper["doi"]["value"] is not None:
                if paper["doi"]["value_lower"] == doi:
                    result.append(Paper(paper["id"]))                
    return result
    """


def find_authors(author):
    """finds model authors but not paper authors"""
    author_q = author.strip().lower()
    author_q_no_accents = strip_accents(author_q)

    author_possibilities = list(
        itertools.chain.from_iterable(
            [
                accented_authors
                for author, accented_authors in all_author_accent_mapping.items()
                if author_q_no_accents in author
            ]
        )
    )

    return list(
        set(
            [
                author
                for author in all_authors
                if author_q in author.lower() or author_q_no_accents in author.lower()
            ]
            + author_possibilities
        )
    )


def find_papers_by_author(author):
    # TODO: this should probably just query the DB with a lowercase solution instead of looping thru papers
    author = author.strip().lower()
    no_accent_author = strip_accents(author)
    result = []
    if " " in no_accent_author:
        for paper in papers.values():
            if "authors" in paper:
                if any(
                    name.startswith(no_accent_author)
                    for name in (
                        strip_accents(item["object_name"].lower())
                        for item in paper["authors"]["value"]
                    )
                ):
                    result.append(Paper(paper["id"]))

    elif no_accent_author:
        for paper in papers.values():
            if "authors" in paper:
                for item in paper["authors"]["value"]:
                    name = strip_accents(item["object_name"]).split()
                    if name and no_accent_author == name[0].lower():
                        result.append(Paper(paper["id"]))
                        break
    return result


def find_papers_by_title(text):
    # TODO: this should probably just query the DB with a lowercase solution instead of looping thru papers
    # TODO: integrate accent stripping from title search ?
    text = text.strip().lower()
    result = []
    for paper in papers.values():
        if "title" in paper:
            if text in paper["title"]["value"].lower():
                result.append(Paper(paper["id"]))
    return result


class ModelDB(models.Model):
    class Meta:
        app_label = ("modeldb2020",)
        permissions = [
            ("can_admin", "Can do admin"),
            ("can_pipeline", "Can use pipeline"),
            ("can_edit_model", "Can edit model"),
            ("can_view_private_models", "Can view private models"),
            ("can_change_privacy", "Can make models private or public"),
        ]

    @property
    def paper_mentions(self):
        return ptrm

    @property
    def news(self):
        try:
            with open(settings.security["news"]) as f:
                return f.read()
        except:
            return ""

    def has_private_model(self, id_):
        return bool(sdb.private_models.find_one({"id": int(id_)}))

    def auth_private_model(self, id_, pwd):
        """returns None, rw, or r depending on access rights"""
        raw_model = sdb.private_models.find_one({"id": int(id_)})
        if not raw_model:
            return None
        pwd = pwd.encode("utf8")
        rwac = raw_model["data_to_curate"]["rwac"]
        rac = raw_model["data_to_curate"].get("rac")
        print("rac", rac)
        if bcrypt.checkpw(pwd, rwac.encode("utf8")):
            return "rw"
        elif rac and bcrypt.checkpw(pwd, rac.encode("utf8")):
            return "r"
        else:
            return None

    def find_private_models(self):
        # TODO: allow filtering like in find_models
        return [self.private_model(model["id"]) for model in sdb.private_models.find()]

    def find_models(
        self,
        channels=[],
        transmitters=[],
        receptors=[],
        genes=[],
        simenvironment=[],
        modelconcepts=[],
        celltypes=[],
        modeltype=[],
        brainregions=[],
        title=[],
        model_id=None,
        authors=[],
    ):
        result = []
        for model in modeldb.values():
            if (
                hasany(model.get("transmitters"), transmitters)
                and hasany(model.get("receptors"), receptors)
                and hasany(model.get("genes"), genes)
                and hasany(model.get("modeling_application"), simenvironment)
                and hasany(model.get("model_concept"), modelconcepts)
                and hasany(model.get("neurons"), celltypes)
                and hasany(model.get("model_type"), modeltype)
                and hasany(model.get("currents"), channels)
                # and hasany(model.get('authors'), authors)
                and hasanytitle([model.get("name")], title, add_star=True)
                and hasany(model.get("brainregions"), brainregions)
                and (model_id is None or model_id == model["id"])
            ):
                result.append(self.model(model["id"]))

        return result

    def request_to_make_public(self, model_id):
        document = {"id": model_id}
        if not sdb.requested_public.find_one(document):
            sdb.requested_public.insert_one(document)

    def get_requested_public(self, search={}):
        return [
            self.private_model(doc["id"]) for doc in sdb.requested_public.find(search)
        ]

    def make_public(self, model_id):
        global _refresh_thread
        private_model = self.private_model(model_id)._model
        new_model = dict(private_model)
        del new_model["data_to_curate"]
        new_model["_citation_text"] = private_model["data_to_curate"].get("citation")
        new_model["_implementers_text"] = private_model["data_to_curate"].get(
            "implementers"
        )
        sdb.private_models.delete_one(private_model)
        sdb.models.insert_one(new_model)
        document = {"id": str(model_id)}
        sdb.requested_public.delete_one(document)
        shutil.move(
            os.path.join(
                settings.security["modeldb_private_zip_dir"], f"{model_id}.zip"
            ),
            os.path.join(settings.security["modeldb_zip_dir"], f"{model_id}.zip"),
        )
        _refresh_thread = threading.Thread(target=refresh, daemon=True)
        _refresh_thread.start()

    def get_models(self):
        return modeldb

    def __getitem__(self, name):
        return getattr(self, name)

    def has_model(self, id_):
        return id_ in modeldb or int(id_) in alternative_models

    def object_by_id(self, object_id):
        return _object_by_id(object_id)

    def model(self, id_):
        return Model(id_)

    def private_model(self, id_):
        return PrivateModel(id_)

    @property
    def num_models(self):
        return len(modeldb)

    def models_by_name(self):
        return sorted(
            [{"id": key, "name": model["name"]} for key, model in modeldb.items()],
            key=lambda item: item["name"],
        )

    @property
    def simenvironment_counts(self):
        counts = {}
        for model in modeldb.values():
            for simulator in model.get("modeling_application", {"value": []})["value"]:
                sim_id = simulator["object_id"]
                counts.setdefault(sim_id, 0)
                counts[sim_id] += 1
        return counts


def count_references(models=None):
    if models is None:
        models = [Model(model_id, files_needed=False) for model_id in modeldb]
    ref_counts = {}
    for model in models:
        for paper in model.papers:
            for ref in paper.references:
                ref_counts.setdefault(ref._id, 0)
                ref_counts[ref._id] += 1
    return ref_counts


def _object_by_id(object_id):
    object_id = str(object_id)
    test_list = [
        modeldb,
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
    ]
    classes = [
        Model,
        Current,
        Gene,
        Region,
        Receptor,
        Transmitter,
        SimEnvironment,
        ModelConcept,
        ModelType,
        CellType,
        Paper,
    ]
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
            check = "*" + check + "*"
        check = check.lower().strip()
        if check:
            for item in present["value"]:
                if fnmatch.fnmatch(item["object_name"].lower(), check):
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
            check = "*" + check + "*"
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
        return self._data["name"]

    @property
    def description(self):
        try:
            return self._data["Description"]["value"]
        except KeyError:
            try:
                return self._data["description"]["value"]
            except KeyError:
                return ""

    def __repr__(self):
        return repr(self._data)

    def __getitem__(self, name):
        return getattr(self, name)

    @property
    def id(self):
        return self._data["id"]

    def models(self):
        # TODO: include children
        # TODO: respect access rights (include private if logged in)
        result = []
        for model_id, data in modeldb.items():
            if self.attr_name in data:
                for obj in data[self.attr_name]["value"]:
                    # TODO: see the TODO on load_collection that will allow removing this str()
                    if str(obj["object_id"]) == self._id:
                        result.append({"id": model_id, "name": data["name"]})
                        break
        return sorted(result, key=lambda item: item["name"])


class Current(SenseLabClass):
    classname = "Current"
    attr_name = "currents"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = currents[_id]

    @property
    def function(self):
        try:
            return self._data["Function"]["value"]
        except KeyError:
            return ""


class Gene(SenseLabClass):
    classname = "Gene"
    attr_name = "gene"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = genes[_id]


class Region(SenseLabClass):
    classname = "Brain Region/Organism"
    attr_name = "region"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = regions[_id]
        print("constructed region", _id)


class Receptor(SenseLabClass):
    classname = "Receptor"
    attr_name = "receptors"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = receptors[_id]


class Transmitter(SenseLabClass):
    classname = "Transmitter"
    attr_name = "neurotransmitters"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = transmitters[_id]


class SimEnvironment(SenseLabClass):
    classname = "Simulation Environment"
    attr_name = "modeling_application"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = simenvironments[_id]


class ModelConcept(SenseLabClass):
    classname = "Model Concept"
    attr_name = "model_concept"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = modelconcepts[_id]


class ModelType(SenseLabClass):
    classname = "Model Type"
    attr_name = "model_type"

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = modeltypes[_id]


class CellType(SenseLabClass):
    classname = "Cell Type"
    attr_name = "neurons"
    class_id = 18

    def __init__(self, _id):
        SenseLabClass.__init__(self, _id)
        self._data = celltypes[_id]

    def picture(self):
        try:
            return self._data["Picture"]["value"][0]["file_content"].replace("\n", "")
        except:
            return None

    def links(self):
        return {
            item: self._data[item]
            for item in ["interlex", "neuromorpho_url", "neuroelectro"]
            if item in self._data
        }


def models_with_uncurated_papers():
    print("models_with_uncurated_papers")
    result = []
    for id_ in modeldb:
        m = Model(id_, files_needed=False)
        papers = m.papers
        for paper in papers:
            if not paper.references:
                result.append(m)
                break
    return result


def find_ode_files(file_hierarchy):
    result = []
    for item in file_hierarchy:
        name = item["name"]
        item_type = item["type"]
        if item_type == "folder":
            result.extend(
                [f"{name}/{old_name}" for old_name in find_ode_files(item["contents"])]
            )
        elif item_type == "ode":
            result.append(name)
    return result


def get_ode_params(ode_contents):
    "extract parameter, value pairs from an ode file"
    result = []
    try:
        ode_contents = ode_contents.decode("utf8")
    except:
        return []
    lines = ode_contents.split("\n")
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line.lower().startswith(
            (
                "p ",
                "pa ",
                "par ",
                "para ",
                "param ",
                "parame ",
                "paramet ",
                "paramete ",
                "parameter ",
                "parameters ",
            )
        ):
            for param in ("".join(line.split()[1:])).split(","):
                try:
                    name, value = param.split("=")
                    if value[0] == ".":
                        value = f"0{value}"
                    result.append({"name": name, "value": value})
                except:
                    pass
    return sorted(result, key=lambda item: item["name"].lower())


def files_with_matching_hash(file_contents):
    my_hash = hashlib.sha256(file_contents).hexdigest()
    return sdb.model_files.find({"hash": my_hash})


def get_parameters(model):
    result = []
    for filename in find_ode_files(model.file_hierarchy):
        params = get_ode_params(model.file(filename))
        if params:
            result.append({"filename": filename, "params": params})
    return {"by_file": result}


class Model:
    def __init__(self, model_id, files_needed=True):
        if int(model_id) in alternative_models:
            self.id2 = model_id
            model_id = alternative_models[int(model_id)]
        else:
            self.id2 = model_id
        self._model = modeldb[str(model_id)]
        self._zip = None
        if files_needed:
            self._readme_file = None
            self._setup_filetree()
        # raise Exception(str(self._model['alternative_version']))

    def modelview(self, data_type):
        if data_type == "parameters":
            ode_files = get_parameters(self)
            return ode_files
        return None

    def update(self, data):
        print(f"Model {self.id2} update (not implemented)")
        print("Current data:")
        _model = dict(self._model)
        del _model["_id"]
        print(json.dumps(_model, indent=4))
        print("New data:")
        print(json.dumps(data, indent=4))

    @property
    def papers(self):
        if "model_paper" in self._model:
            return [
                Paper(item["object_id"]) for item in self._model["model_paper"]["value"]
            ]
        else:
            return []

    @property
    def alternative_version(self):
        if "alternative_version" not in self._model:
            return "test"  # []
        else:
            return self._model["alternative_version"]

    def __getattr__(self, key):
        if key in self._model:
            return self._model[key]
        elif (
            self._model["id"] in network_models
            and key in network_models[self._model["id"]]
        ):
            result = network_models[self._model["id"]][key]
            if pd.isna(result):
                result = None
            return result
        elif (
            self._model["id"] in network_models
            and key.startswith("short_")
            and key[6:] in network_models[self._model["id"]]
        ):
            result = network_models[self._model["id"]][key[6:]]
            if isinstance(result, str):
                result = result.split(";")[0].strip()
                if result == "partial":
                    result = "yes"
            if pd.isna(result):
                result = None
            return result
        else:
            return {}

    def zip(self):
        if self._zip is None:
            self._zip = zipfile.ZipFile(
                os.path.join(
                    settings.security["modeldb_zip_dir"],
                    f"{self.id2}.zip",
                )
            )
        return self._zip

    @property
    def readme_file(self):
        return self._readme_file

    @property
    def file_hierarchy(self):
        return self._file_hierarchy

    @property
    def public_submitter_email(self):
        return self._model.get("public_submitter_email", {}).get("value")

    def has_path(self, path):
        return path in self.zip().namelist() or self.has_folder(path)

    def file(self, path):
        return self.zip().read(path)

    def has_folder(self, path):
        name_list = self.zip().namelist()
        path = path.strip("/") + "/"
        return any(item.startswith(path) for item in name_list)

    def zip_file(self):
        filename = f"{self.id2}.zip"
        with open(
            os.path.join(settings.security["modeldb_zip_dir"], filename), "rb"
        ) as f:
            return f.read()

    def folder_contents(self, path, _hierarchy=None):
        def _filter(items):
            return sorted(
                [
                    {"name": item["name"], "type": item["type"].lower()}
                    for item in items
                ],
                key=lambda item: item["name"].lower(),
            )

        if _hierarchy is None:
            _hierarchy = self.file_hierarchy
        if "/" in path:
            first, rest = path.split("/", 1)
        else:
            first, rest = path, None
        for item in _hierarchy:
            if item["name"] == first:
                if rest:
                    return self.folder_contents(rest, _hierarchy=item["contents"])
                return _filter(item["contents"])
        assert False

    def _setup_filetree(self):
        if self._readme_file is None:
            file_hierarchy = []
            readme_file = None
            first_file = ""
            for subfilename in self.zip().namelist():
                if not first_file and os.path.split(subfilename)[1]:
                    first_file = subfilename
                if (
                    #                   ("readme" in subfilename.lower() and not self.zip().getinfo(subfilename).is_dir())
                    subfilename.lower().split("/")[-1]
                    in (
                        "index.html",
                        "index.htm",
                        "readme.txt",
                        "readme.html",
                        "readme.htm",
                        "readme.md",
                        "readme",
                    )
                ):
                    if readme_file is None or len(subfilename) < len(readme_file):
                        readme_file = subfilename
                path = subfilename.split("/")
                my_file_hierarchy = file_hierarchy
                for i, item in enumerate(path):
                    for mfh in my_file_hierarchy:
                        if mfh["name"] == item:
                            my_file_hierarchy = mfh["contents"]
                            break
                    else:
                        my_file_hierarchy.append({"name": item})
                        if i != len(path) - 1:
                            my_file_hierarchy[-1]["type"] = "folder"
                            my_file_hierarchy[-1]["contents"] = []
                            my_file_hierarchy = my_file_hierarchy[-1]["contents"]
                        else:
                            if "." not in item:
                                my_file_hierarchy[-1]["type"] = "file"
                            else:
                                my_file_hierarchy[-1]["type"] = item.split(".")[-1]
            self._readme_file = readme_file if readme_file else first_file
            self._file_hierarchy = file_hierarchy
        return self._readme_file, self._file_hierarchy

    @property
    def reused_files(self):
        model_id = self.id2
        all_reuse = []
        for file_info in sdb.model_files.find({"model_id": self.id2}):
            if file_info["basename"]:
                file_hash = file_info["hash"]
                all_matches = sdb.model_files.find({"hash": file_hash})
                my_results = []
                for match in all_matches:
                    if match["model_id"] != self.id2:
                        my_results.append(
                            {"model_id": match["model_id"], "path": match["path"]}
                        )
                if my_results:
                    all_reuse.append(
                        {
                            "basename": file_info["basename"],
                            "path": file_info["path"],
                            "reuse": my_results,
                        }
                    )
        return all_reuse


def lookup_title(model_id):
    return sdb.models.find_one({"id": model_id})["name"]


class Paper:
    def __init__(self, paper_id):
        self._id = str(paper_id)

    @property
    def _raw(self):
        return papers[str(self._id)]

    @property
    def authors(self):
        try:
            return [item["object_name"] for item in self._raw["authors"]["value"]]
        except:
            return []

    @property
    def year(self):
        try:
            return self._raw["year"]["value"]
        except:
            return ""

    @property
    def model_link(self):
        try:
            return self._raw["model_link"]
        except:
            return ""

    @property
    def title(self):
        try:
            return self._raw["title"]["value"]
        except:
            return ""

    @property
    def journal(self):
        try:
            return self._raw["journal"]["value"]
        except:
            return ""

    @property
    def volume(self):
        try:
            return self._raw.get("volume", {"value": ""})["value"]
        except:
            return ""

    @property
    def modeldb_usage(self):
        try:
            return self._raw["stated_usage"]["value"][0]["object_name"]
        except:
            return ""

    @property
    def url(self):
        try:
            return self._raw["url"]["value"]
        except:
            return ""

    @property
    def doi(self):
        try:
            return self._raw["doi"]["value"]
        except:
            return ""

    @property
    def pubmed(self):
        try:
            return self._raw["pubmed_id"]["value"]
        except:
            return ""

    @property
    def html(self):
        url = self.doi
        if not url:
            url = self.url
        else:
            url = "https://doi.org/" + url

        if url:
            link_prefix = '<a href="{}">'.format(url)
            link_suffix = "</a>"
        else:
            link_prefix = link_suffix = ""

        pubmed = self.pubmed
        if pubmed:
            pubmed = ' [<a href="https://www.ncbi.nlm.nih.gov/pubmed?holding=modeldb&term={}">PubMed</a>]'.format(
                pubmed
            )

        if len(self.authors) <= 5:
            base_info = ", ".join(self.authors) + f". ({self.year})."
        else:
            base_info = f"{self.authors[0]} et al. ({self.year})."

        base_info = f'<a href="/citations/{self._id}">{base_info}</a>'
        return (
            base_info
            + f" {self.title} <i>"
            + link_prefix
            + self.journal
            + link_suffix
            + "</i>. "
            + self.volume
            + pubmed
        )

    @property
    def text(self):
        base_info = ", ".join(self.authors) + f". ({self.year})."
        return f"{base_info} {self.title} {self.journal}. {self.volume}"

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def references(self):
        if "references" in self._raw:
            return [
                Paper(item["object_id"]) for item in self._raw["references"]["value"]
            ]
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
        return self._raw["name"]

    @property
    def id(self):
        return self._id

    @property
    def models(self):
        # print(self._id, models_by_paper.keys())
        if int(self._id) in models_by_paper:
            return [
                Model(_id, files_needed=False) for _id in models_by_paper[int(self._id)]
            ]
        else:
            return []


class PrivateModel(Model):
    def __init__(self, model_id):
        self._model = sdb.private_models.find_one({"id": int(model_id)})
        self._zip = None
        self.id2 = model_id
        self._readme_file = None
        self._setup_filetree()
        self._model.setdefault("model_paper", {"value": []})

    def update(self, data):
        print(f"Private model {self.id2} update")
        print(json.dumps(data, indent=4))
        sdb.private_models.update_one({"id": int(self.id2)}, {"$set": data})
        self._model = sdb.private_models.find_one({"id": int(self.id2)})
        print("New data:")
        model = dict(self._model)
        del model["_id"]
        print(json.dumps(model, indent=4))

    def zip_file(self):
        filename = f"{self._model['id']}.zip"
        with open(
            os.path.join(settings.security["modeldb_private_zip_dir"], filename), "rb"
        ) as f:
            return f.read()

    def zip(self):
        if self._zip is None:
            self._zip = zipfile.ZipFile(
                os.path.join(
                    settings.security["modeldb_private_zip_dir"],
                    f"{self._model['id']}.zip",
                )
            )
        return self._zip


refresh()
