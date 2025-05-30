from inspect import isdatadescriptor
import requests
import xml.dom.minidom as m
import xml.etree.ElementTree as ET
import json
from pymongo import MongoClient, ReturnDocument
import json
import requests
from pymongo import MongoClient
import time
import re
import xml
import functools
import unicodedata
from datetime import datetime

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])


invalid_doi = set()  # for Error: Invalid response from Entrez PubMed API


@functools.lru_cache()
def lookup_pmid_from_doi(doi):
    """code adapted from ChatGPT 2023-02-14"""
    if "dryad" not in doi:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={doi}&retmode=json"
        data = requests.get(url).json()
    else:
        invalid_doi.add(doi)

    # Extract the PMID, if it exists
    if (
        "dryad" not in doi
        and "esearchresult" in data
        and "idlist" in data["esearchresult"]
    ):
        if "errorlist" in data["esearchresult"]:
            invalid_doi.add(doi)
            return None
        else:
            id_list = data["esearchresult"]["idlist"]
            if len(id_list) > 0:
                print(doi)
                assert len(id_list) == 1
                pmid = id_list[0]
                return str(pmid)
            else:
                invalid_doi.add(doi)
                return None
    else:
        invalid_doi.add(doi)


def new_object_id():
    """returns a new object id"""
    return sdb.meta.find_one_and_update(
        {}, {"$inc": {"id_count": 1}}, return_document=ReturnDocument.AFTER
    )["id_count"]


# strip_accents from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def new_author_check(author_name):
    stripped_author_name = author_name.strip()
    return (
        sdb.authors.find_one(
            {
                "object_name": {
                    "$regex": re.compile(f"^{stripped_author_name}$", re.IGNORECASE)
                }
            }
        )
        is None
        and sdb.authors.find_one(
            {
                "object_name": {
                    "$regex": re.compile(
                        f"^{strip_accents(stripped_author_name)}$", re.IGNORECASE
                    )
                }
            }
        )
        is None
    )


invalid_author_db = set()
invalid_author_id = set()


def retrieve_author_object_id(author_name):
    author = sdb.authors.find_one(
        {"object_name": {"$regex": re.compile(f"^{author_name}$", re.IGNORECASE)}}
    )
    if not author:
        author = sdb.authors.find_one(
            {
                "object_name": {
                    "$regex": re.compile(
                        f"^{strip_accents(author_name)}$", re.IGNORECASE
                    )
                }
            }
        )
    if author is None:
        invalid_author_db.add(author_name)
    else:
        return author["object_id"]
    invalid_author_id.add(author_name)


no_pmid_or_doi = set()
papers_to_lookup_on_crossref = set()


def get_pmid_from_paper(paper):
    pmid = None
    paper_id = True
    if paper.get("pubmed_id") is None:
        if paper.get("doi") is None or paper.get("doi.value") is None:
            no_pmid_or_doi.add(paper["id"])
            paper_id = False
            print(paper["id"], "has no ids")
        else:
            # print(paper, "\n", paper["doi"]["value"])
            paper["pubmed_id"] = {"value": lookup_pmid_from_doi(paper["doi"]["value"])}
    if paper_id:
        if paper["pubmed_id"]:
            pmid = paper["pubmed_id"]["value"]
            if pmid is None:
                print(
                    f"paper {paper['id']} has no pubmed_id, but you can probably get the authors from crossref"
                )
                papers_to_lookup_on_crossref.add(paper["id"])
    return pmid


# creates paper "name" for papers collection metadata
def paper_name(paper_metadata, paper=None):
    name = ""
    num_of_authors = len(paper_metadata["authors"]["value"])

    if num_of_authors <= 5:
        for author in paper_metadata["authors"]["value"]:
            name += str(author["object_name"])
            num_of_authors -= 1
            if num_of_authors > 0:
                name += ", "
            else:
                name += " "

        if "year" in paper_metadata:
            name += "(" + paper_metadata["year"]["value"] + ")"
        elif paper and "year" in paper:
            name += "(" + paper["year"]["value"] + ")"

    else:
        if "year" in paper_metadata:
            name = (
                str(paper_metadata["authors"]["value"][0]["object_name"])
                + " et al. ("
                + paper_metadata["year"]["value"]
                + ")"
            )
        elif paper and "year" in paper:
            name = (
                str(paper_metadata["authors"]["value"][0]["object_name"])
                + " et al. ("
                + paper["year"]["value"]
                + ")"
            )
        else:
            name = str(paper_metadata["authors"]["value"][0]["object_name"]) + " et al."

    return name


# Run this function to sync authors in papers collection and authors collection
def check_authors():
    pmids_to_process = []
    papers = []
    paper_ids = [paper["id"] for paper in sdb.papers.find()]
    for paper_id in paper_ids:
        paper = sdb.papers.find_one({"id": paper_id})
        pmid = get_pmid_from_paper(paper)
        if pmid is not None:
            pmids_to_process.append(pmid)
            papers.append(paper)
            if len(pmids_to_process) >= 99:
                get_author_info(pmids_to_process, papers)
                pmids_to_process = []
                papers = []
    get_author_info(pmids_to_process, papers)


# this is for getting metadata from pubmed
# and using it to update the papers collection
def get_author_info(pmids_to_process, papers, do_update=True):
    metadata_dict = get_metadata(pmids_to_process)
    for paper in papers:
        pmid = paper["pubmed_id"]["value"]
        if metadata_dict.get(pmid):
            my_metadata = metadata_dict[pmid]

            if not (
                my_metadata["pubmed_id"]["value"] == pmid
                and paper["pubmed_id"]["value"] == pmid
            ):
                print("papers don't line up!?!")
                breakpoint()

            if "authors" not in paper:
                paper["authors"] = {}
            paper["authors"]["value"] = my_metadata["authors"]["value"]
            print(paper["id"], paper["authors"]["value"])

            updated_paper_name = paper_name(my_metadata, paper)
            if do_update:
                current_date = datetime.now().isoformat()

                new_values = {
                    "name": updated_paper_name,
                    "authors.value": paper["authors"]["value"],
                    "ver_date": current_date,
                    "ver_number": paper["ver_number"] + 1,
                    "journal": my_metadata["journal"],
                    "pubmed_id": my_metadata["pubmed_id"],
                }

                if "doi" in my_metadata:
                    new_values["doi"] = my_metadata["doi"]

                if "volume" in my_metadata:
                    new_values["volume"] = my_metadata["volume"]

                if "year" in my_metadata:
                    new_values["year"] = my_metadata["year"]

                if "month" in my_metadata:
                    new_values["month"] = my_metadata["month"]

                if "day" in my_metadata:
                    new_values["day"] = my_metadata["day"]

                sdb.papers.update_one({"id": paper["id"]}, {"$set": new_values})


# adds new authors to authors collection
def add_new_author_to_collection(object_name, lastname, firstname, initials, orcid):
    stripped_object_name = object_name.strip()

    matching_paper = sdb.papers.find_one(
        {
            "authors.value.object_name": {
                "$regex": re.compile(f"^{stripped_object_name}$", re.IGNORECASE)
            }
        }
    )
    if not matching_paper:
        matching_paper = sdb.papers.find_one(
            {
                "authors.value.object_name": {
                    "$regex": re.compile(
                        f"^{strip_accents(stripped_object_name)}$", re.IGNORECASE
                    )
                }
            }
        )
    if matching_paper:
        for author in matching_paper["authors"]["value"]:
            if author["object_name"].lower() == stripped_object_name.lower():
                id_ = author["object_id"]
                break
        else:
            pattern = re.compile(
                f"^{strip_accents(stripped_object_name)}$", re.IGNORECASE
            )
            for author in matching_paper["authors"]["value"]:
                if pattern.match(author["object_name"]):
                    id_ = author["object_id"]
                    break
    else:
        id_ = new_object_id()

    sdb.authors.insert_one(
        {
            "object_id": id_,
            "object_name": stripped_object_name,
            "LastName": lastname,
            "ForeName": firstname,
            "Initials": initials,
            "ORCID": orcid,
        }
    )
    return id_


def get_articles(pmids):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    time.sleep(1)
    r = requests.post(url, data={"id": pmids, "db": "PubMed", "retmode": "xml"})
    return r


def update_orcid(author_name, orcid):
    author = sdb.authors.find_one(
        {"object_name": {"$regex": re.compile(f"^{author_name}$", re.IGNORECASE)}}
    )
    collection_orcid = {"ORCID": orcid}
    if author:
        sdb.authors.update_one(
            {"object_name": {"$regex": re.compile(f"^{author_name}$", re.IGNORECASE)}},
            {"$set": collection_orcid},
        )
    if not author:
        author = sdb.authors.find_one(
            {
                "object_name": {
                    "$regex": re.compile(
                        f"^{strip_accents(author_name)}$", re.IGNORECASE
                    )
                }
            }
        )
        if author:
            sdb.authors.update_one(
                {
                    "object_name": {
                        "$regex": re.compile(
                            f"^{strip_accents(author_name)}$", re.IGNORECASE
                        )
                    }
                },
                {"$set": collection_orcid},
            )
    if author is None:
        invalid_author_db.add(author_name)


# gets author data from xml
def get_author_metadata(article, pmid):
    all_authors = []
    authors = article.getElementsByTagName("Author")
    try:
        authors.length >= 1
    except:
        all_authors.append("No Author")
    else:
        for author in authors:
            author_dict = {}

            if author.getElementsByTagName("LastName"):
                author_last_name = author.getElementsByTagName("LastName")[
                    0
                ].firstChild.nodeValue
            else:
                author_last_name = None
                author_name_issues[pmid] = author_last_name

            if author.getElementsByTagName("ForeName"):
                author_first_name = author.getElementsByTagName("ForeName")[
                    0
                ].firstChild.nodeValue
            else:
                author_first_name = None
                author_name_issues[pmid] = author_last_name

            if author.getElementsByTagName("Initials"):
                author_initials = author.getElementsByTagName("Initials")[
                    0
                ].firstChild.nodeValue
            else:
                author_initials = None
                author_name_issues[pmid] = author_last_name

            # creates object_name
            if author_last_name and author_initials:
                author_object_name = author_last_name + " " + author_initials
            elif author_last_name:
                author_object_name = author_last_name
            elif author.getElementsByTagName("CollectiveName"):
                author_object_name = author.getElementsByTagName("CollectiveName")[
                    0
                ].firstChild.nodeValue
            else:
                author_object_name = None
                print(f"no author object_name:{pmid}")
                no_last_name.append(pmid)

            author_orcid = None
            if author.getElementsByTagName("Identifier"):
                if (
                    "ORCID"
                    == author.getElementsByTagName("Identifier")[0]
                    .getAttributeNode("Source")
                    .nodeValue
                ):
                    author_orcid = author.getElementsByTagName("Identifier")[
                        0
                    ].firstChild.nodeValue

            # add author to author collection if not already there
            if new_author_check(author_object_name):
                author_object_id = add_new_author_to_collection(
                    author_object_name,
                    author_last_name,
                    author_first_name,
                    author_initials,
                    author_orcid,
                )
            else:
                author_object_id = retrieve_author_object_id(author_object_name)
                if author_orcid is not None:
                    update_orcid(author_object_name, author_orcid)

            author_dict["object_id"] = author_object_id
            author_dict["object_name"] = author_object_name
            all_authors.append(author_dict)

    return all_authors


# recursively retrievings article title
#   -- necessary due to use of HTML tags in title e.g. <i>, <sub>
def get_text_content(node):
    content = ""
    for child_node in node.childNodes:
        if child_node.nodeType == child_node.TEXT_NODE:
            content += child_node.nodeValue
        elif child_node.nodeType == child_node.ELEMENT_NODE:
            content += get_text_content(child_node)
    return content


# Run this function to get metadata from a pubmed article
no_last_name = []
author_name_issues = {}


def get_metadata(pmids):
    metadata_w_pmid = {}
    metadata_list = []

    for i in range(3):
        try:
            r = get_articles(pmids)
            doc = m.parseString(r.text)
            break
        except xml.parsers.expat.ExpatError:
            print("uh oh")
            print(r.text)
            print(f"attempt {i} failed")
    else:
        print(f"I give up on {pmids}")
        raise Exception()

    articles = doc.getElementsByTagName("PubmedArticle")

    for article in articles:
        metadata = {}

        # pmid
        pmid = str(article.getElementsByTagName("PMID")[0].firstChild.nodeValue)
        pmid_dict = {"value": pmid, "attr_id": 153}

        # title
        full_title = ""
        titles = article.getElementsByTagName("ArticleTitle")

        for title in titles:
            full_title += get_text_content(title)

        if full_title is None:
            book_title = article.getElementsByTagName("BookTitle")
            if book_title is not None:
                full_title = get_text_content(book_title)
        assert full_title is not None

        title_dict = {"value": full_title, "attr_id": 139}
        metadata["title"] = title_dict

        # authors
        all_authors = get_author_metadata(article, pmid)
        authors_dict = {"value": all_authors, "attr_id": 148}
        metadata["authors"] = authors_dict

        # journal volume
        try:
            volume = article.getElementsByTagName("Volume")[0].firstChild.nodeValue
            volume_dict = {"value": volume, "attr_id": 149}
            metadata["volume"] = volume_dict
        except:
            print(f"no volume for pmid {pmid}")

        # doi
        doi = None
        if article.getElementsByTagName("ELocationID") and (
            "doi"
            == article.getElementsByTagName("ELocationID")[0]
            .getAttributeNode("EIdType")
            .nodeValue
        ):
            doi = article.getElementsByTagName("ELocationID")[0].firstChild.nodeValue
        else:
            idlist = article.getElementsByTagName("ArticleIdList")
            i = idlist[0]
            for article_id in i.getElementsByTagName("ArticleId"):
                if "doi" == article_id.getAttribute("IdType"):
                    doi = article_id.childNodes[0].nodeValue
                    break

        if doi:
            doi_dict = {"value": doi, "attr_id": 339}
            metadata["doi"] = doi_dict

        # pmid insert is here for dict formatting
        metadata["pubmed_id"] = pmid_dict

        # Published date
        pubdate = article.getElementsByTagName("PubDate")[0]
        if pubdate.getElementsByTagName("Year"):
            year = pubdate.getElementsByTagName("Year")[0].childNodes[0].nodeValue
            year_dict = {"value": year, "attr_id": 154}
            metadata["year"] = year_dict

        if pubdate.getElementsByTagName("Month"):
            month = pubdate.getElementsByTagName("Month")[0].childNodes[0].nodeValue
            month_dict = {"value": month, "attr_id": 156}
            metadata["month"] = month_dict

        if pubdate.getElementsByTagName("Day"):
            day = pubdate.getElementsByTagName("Day")[0].childNodes[0].nodeValue
            day_dict = {"value": day, "attr_id": 157}
            metadata["day"] = day_dict

        # journal
        journal_title = article.getElementsByTagName("Title")[0].firstChild.nodeValue
        journal_dict = {"value": journal_title, "attr_id": 158}
        metadata["journal"] = journal_dict

        # combine metadata for all searched pmids
        metadata_w_pmid[pmid] = metadata
        metadata_list.append(metadata)

    return metadata_w_pmid


def get_reference_pmids(pmid):
    pmids_list = []
    dois_list = []
    r = requests.get(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    )
    try:
        doc = m.parseString(r.text)
    except:
        print(r.text)
        raise
    reference_list = doc.getElementsByTagName("ReferenceList")[0]
    ids = reference_list.getElementsByTagName("ArticleIdList")

    for article_id in ids:
        pubmed = False
        for i in article_id.getElementsByTagName("ArticleId"):
            if "pubmed" == i.getAttributeNode("IdType").childNodes[0].nodeValue:
                articleid_pmid = i.childNodes[0].nodeValue
                pmids_list.append(articleid_pmid)
                pubmed = True
        if not pubmed:
            for i in article_id.getElementsByTagName("ArticleId"):
                if "doi" == i.getAttributeNode("IdType").childNodes[0].nodeValue:
                    articleid_doi = i.childNodes[0].nodeValue
                    dois_list.append(articleid_doi)

    pmids_string = ",".join(pmids_list)
    return pmids_string, dois_list


# check if reference is in the papers collection
# True -- new, False -- exists
def check_new_reference(pmid, doi):
    if doi is None:
        return sdb.papers.find_one({"pubmed_id.value": str(pmid)}) is None
    else:
        return sdb.papers.find_one({"doi.value": doi}) is None


def insert_new_paper(metadata_dict):
    new_info_dict = {}

    id_ = new_object_id()
    new_info_dict["id"] = id_
    new_paper_name = paper_name(metadata_dict)

    new_info_dict["name"] = new_paper_name
    new_info_dict["created"] = datetime.now().isoformat()
    new_info_dict["ver_date"] = new_info_dict["created"]
    new_info_dict["ver_number"] = 1

    new_info_dict.update(metadata_dict)
    sdb.papers.insert_one(new_info_dict)

    return id_


def retrieve_paper(pmid):
    paper = sdb.papers.find_one({"pubmed_id.value": str(pmid)})
    return paper


def set_pmid(paper_id, pmid):
    sdb.papers.update_one({"id": paper_id}, {"$set": {"pubmed_id": {'value': str(pmid), 'attr_id': 153}}})


def get_reference_metadata(pmid):
    reference_pmids, reference_dois = get_reference_pmids(pmid)
    reference_metadata_dict = get_metadata(reference_pmids)
    missing_references = []

    for pmid in reference_metadata_dict:
        if check_new_reference(pmid, None):
            new_paper_id = insert_new_paper(reference_metadata_dict[pmid])
            reference_metadata_dict[pmid]["id"] = new_paper_id
        else:
            paper = retrieve_paper(pmid)
            reference_metadata_dict[pmid] = paper

    for doi in reference_dois:
        reference_doi_to_pmid = lookup_pmid_from_doi(doi)
        if reference_doi_to_pmid is not None:
            if check_new_reference(reference_doi_to_pmid, None):
                time.sleep(1)
                doi_metadata = get_metadata(reference_doi_to_pmid)
                reference_metadata_dict.update(doi_metadata)
                new_paper_id = insert_new_paper(
                    reference_metadata_dict[reference_doi_to_pmid]
                )
                reference_metadata_dict[reference_doi_to_pmid]["id"] = new_paper_id
            else:
                paper = retrieve_paper(reference_doi_to_pmid)
                reference_metadata_dict[reference_doi_to_pmid] = paper
        elif reference_doi_to_pmid is None:
            missing_references.append(doi)

    if missing_references:
        reference_metadata_dict.setdefault("missing_references", {})[
            "value"
        ] = missing_references
        reference_metadata_dict["missing_references"]["attr_id"] = 211

    return reference_metadata_dict


def insert_paper_with_references(pmid):
    metadata = get_metadata(pmid)[str(pmid)]
    metadata["pubmed_id"] = {"value": pmid, "attr_id": 153}
    try:
        # returns new papers id
        reference_metadata = get_reference_metadata(pmid)
        # get_author_info([pmid], [metadata], do_update=False)
        if "missing_references" in reference_metadata:
            metadata["missing_references"] = reference_metadata["missing_references"]
            del reference_metadata["missing_references"]
        metadata["references"] = {
            "value": [
                {"object_id": item["id"], "object_name": item["name"]}
                for item in reference_metadata.values()
                if "name" in item
            ],
            "attr_id": 140,
        }
    except IndexError:
        # this happens when no references
        ...
    return insert_new_paper(metadata)


# Updates references for singular existing paper
def add_references_to_existing_paper(paper_id):
    metadata = sdb.papers.find_one({"id": paper_id})
    pmid = metadata["pubmed_id"]["value"]
    reference_metadata = get_reference_metadata(pmid)

    if "missing_references" in reference_metadata:
        metadata["missing_references"] = reference_metadata["missing_references"]
        del reference_metadata["missing_references"]

    # the if statement here comes up with e.g. books (paper 267767's Ito reference)
    metadata["references"] = {
        "value": [
            {"object_id": item["id"], "object_name": item["name"]}
            for item in reference_metadata.values()
            if "name" in item and "id" in item
        ],
        "attr_id": 140,
    }

    metadata["ver_date"] = datetime.now().isoformat()
    metadata["ver_number"] = 1 + metadata.get("ver_number", 0)

    sdb.papers.update_one({"id": paper_id}, {"$set": metadata})


# Updates entire paper collection's references
def add_missing_references_to_paper_collection():
    all_model_papers = sdb.models.distinct("model_paper.value.object_id")
    for paper_id in all_model_papers:
        paper = sdb.papers.find_one({"id": paper_id})
        if "pubmed_id" in paper:
            if not paper.get("references", {}).get("value"):
                try:
                    add_references_to_existing_paper(paper_id)
                    print(
                        "successfully added references to paper",
                        paper_id,
                        "PMID:",
                        paper["pubmed_id"]["value"],
                    )
                except:
                    print(
                        "failed to add references to paper",
                        paper_id,
                        "PMID:",
                        paper["pubmed_id"]["value"],
                    )


def add_paper_to_model(paper_id, model_id):
    model_data = sdb.models.find_one({"id": model_id}).get("model_paper", {"value": [], "attr_id": 155})
    paper_data = sdb.papers.find_one({"id": paper_id})["name"]
    model_data["value"].append({"object_id": paper_id, "object_name": paper_data})
    sdb.models.update_one({"id": model_id}, {"$set": {"model_paper": model_data}})


def add_implementer_to_model(implementer_id, model_id):
    model = sdb.models.find_one({"id": model_id})
    model_data = model.get("implemented_by", {"value": [], "attr_id": 299})
    all_implementers = sdb.models.distinct("implemented_by.value")
    for implementer in all_implementers:
        if implementer["object_id"] == implementer_id:
            implementer_data = implementer["object_name"]
            break
    else:
        raise ValueError("Unknown implementer")
    model_data["value"].append({"object_id": implementer_id, "object_name": implementer_data})
    current_date = datetime.now().isoformat()
    sdb.models.update_one({"id": model_id}, {"$set": {"implemented_by": model_data, "ver_date": current_date, "ver_number": model["ver_number"] + 1}})

def add_simulator_to_model(simulator_id, model_id):
    model = sdb.models.find_one({"id": model_id})
    model_data = model.get("modeling_application", {"value": [], "attr_id": 114})
    all_simulators = sdb.models.distinct("modeling_application.value")
    for simulator in all_simulators:
        if simulator["object_id"] == simulator_id:
            simulator_data = simulator["object_name"]
            break
    else:
        raise ValueError("Unknown simulator")
    model_data["value"].append({"object_id": simulator_id, "object_name": simulator_data})
    current_date = datetime.now().isoformat()
    sdb.models.update_one({"id": model_id}, {"$set": {"modeling_application": model_data, "ver_date": current_date, "ver_number": model["ver_number"] + 1}})

def add_new_implementer_to_model(implementer_name, model_id):
    model = sdb.models.find_one({"id": model_id})
    model_data = model.get("implemented_by", {"value": [], "attr_id": 299})
    implementer_id = new_object_id()
    model_data["value"].append({"object_id": implementer_id, "object_name": implementer_name})
    current_date = datetime.now().isoformat()
    sdb.models.update_one({"id": model_id}, {"$set": {"implemented_by": model_data, "ver_date": current_date, "ver_number": model["ver_number"] + 1}})


def find_implementer_containing(name):
    return [
        implementer
        for implementer in sdb.models.distinct("implemented_by.value")
        if name.lower() in implementer["object_name"].lower()
    ]


def find_simulator_containing(name):
    return [
        simulator
        for simulator in sdb.models.distinct("modeling_application.value")
        if name.lower() in simulator["object_name"].lower()
    ]

def manually_add_paper(input_dict):
    metadata = {}
    all_authors = []

    title_dict = {
        "value": input_dict["title"],
        "attr_id": 139
    }
    metadata["title"] = title_dict

    for author in dict["authors"]:
        author_dict = {}
        if author['last_name'] and author['initials']:
            author_object_name = author['last_name'] + " " + author['initials']
        else:
            author_object_name = author['last_name']
        if new_author_check(author_object_name):
            author_object_id = add_new_author_to_collection(
                author_object_name,
                author["last_name"],
                author["first_name"],
                author["initials"],
                author["orcid"],
            )
        else:
            author_object_id = retrieve_author_object_id(author_object_name)
        author_dict["object_id"] = author_object_id
        author_dict["object_name"] = author_object_name
        all_authors.append(author_dict)

    authors_dict = {
        "value": all_authors,
        "attr_id": 148
    }
    metadata["authors"] = authors_dict

    if input_dict['journal']:
        journal_dict = {
            "value": input_dict['journal'],
            "attr_id": 158
        }
        metadata["journal"] = journal_dict

    if input_dict['year']:
        year_dict = {
            "value": str(input_dict['year']),
            "attr_id": 154
        }
        metadata["year"] = year_dict
        
    insert_new_paper(metadata)
    return metadata


def change_model_title(model_id, new_title):
    model = sdb.models.find_one({"id": model_id})
    if not model:
        print(f"Model with id {model_id} not found.")
        return
    updated_model = {
        "name": new_title,
        "ver_date": datetime.now().isoformat(),
        "ver_number": model.get("ver_number", 1) + 1
    }
    sdb.models.update_one({"id": model_id}, {"$set": updated_model})
    print(f"Model {model_id} title has been updated to '{new_title}'.")


def request_to_make_public(model_id):
    document = {"id": str(model_id)}
    if not sdb.requested_public.find_one(document):
        sdb.requested_public.insert_one(document)


def remove_request_to_make_public(model_id):
    document = {"id": str(model_id)}
    if sdb.requested_public.find_one(document):
        sdb.requested_public.delete_one(document)


def associate_file_with_biology_type(file_hash, biology_type):
    """
    Associates a file (identified by its hash) with a biology_type identifier.
    Adds the identifier to the biology_type field list in sdb.model_files.
    """
    # Find all entries with the given hash
    files = sdb.model_files.find({"hash": file_hash})

    has_files = False
    for file in files:
        has_files = True
        # Ensure the biology_type field exists and is a list
        if "biology_type" not in file:
            file["biology_type"] = []
        elif not isinstance(file["biology_type"], list):
            file["biology_type"] = [file["biology_type"]]

        # Add the biology_type identifier if it's not already in the list
        if biology_type not in file["biology_type"]:
            file["biology_type"].append(biology_type)
            # Update the document in the database
            sdb.model_files.update_one(
                {"_id": file["_id"]},
                {"$set": {"biology_type": file["biology_type"]}}
            )
    
    if not has_files:
        print(f"No files found with hash {file_hash}.")

if __name__ == "__main__":
    input("Type enter to run check_authors or ctrl^c to quit")
    check_authors()
    # get_metadata(pmid)
    # get_reference_metadata(pmid)
