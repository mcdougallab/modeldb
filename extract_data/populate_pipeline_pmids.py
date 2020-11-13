"""populate the pipeline from pmid list"""

import pandas as pd
import pprint
from pymongo import MongoClient, ReturnDocument
import json
import xml.etree.ElementTree as ET
import requests
import functools
import time

PMID_FILE = '/home/bitnami/pipeline-pmids.txt'
STATUS = 'evantriage'

try:
    import tqdm

    progress_bar = tqdm.tqdm
except:
    progress_bar = lambda x: x

TEST_ONLY = True

with open("/home/bitnami/app-settings.json") as f:
    app_settings = json.load(f)


last_time = time.time()
min_delay = 0.4


def paced_request(url):
    global last_time
    now = time.time()
    time.sleep(max(0, min_delay - (now - last_time)))
    result = requests.get(url)
    last_time = time.time()
    return result

@functools.lru_cache()
def get_pubtator_data(pmid):
    pubtator = 'https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/biocjson?pmids='

    article = json.loads(paced_request(f"{pubtator}{pmid}").text)
    title = None
    abstract = None
    pubtator = {}
    for passage in article["passages"]:
        infons_type = passage["infons"]["type"]
        if infons_type == "title":
            title = passage["text"]
            pubtator["title_annotations"] = passage["annotations"]
        elif infons_type == "abstract":
            abstract = passage["text"]
            pubtator["abstract_annotations"] = passage["annotations"]

    result = {
        "pmid": int(article["pmid"]),
        "pmcid": article.get("pmcid"),
        "title": title,
        "journal": article["journal"],
        "pubtator": pubtator,
        "abstract": abstract,
        "year": int(article["year"]),
    }
    if result["pmcid"] is None:
        for passage in article["passages"]:
            print(passage)
            infon = passage["infons"]
            pmcid = infon.get("article-id_pmc")
            if pmcid is not None:
                result["pmcid"] = pmcid
                break
    return result

mongodb = MongoClient()
db = mongodb[app_settings["db_name"]]
db.authenticate(
    app_settings["mongodb_user"], app_settings["mongodb_pw"]
)

# and prepare to start building it again
collection = getattr(db, app_settings["collection_name"])

def get_pubmed_data(article):
    try:
        my_article = article.find("MedlineCitation")
        pmid = int(my_article.find("PMID").text)
        mesh_heading = my_article.find("MeshHeadingList")
        doi = None
        try:
            for item in article.find("PubmedData").find("ArticleIdList"):
                if item.get("IdType") == "doi":
                    doi = item.text
                    break
        except:
            pass
        my_article = my_article.find("Article")

        author_list = []
        author_list_tree = my_article.find("AuthorList")
        if author_list_tree:
            for author in author_list_tree.findall("Author"):
                affiliation = author.find("AffiliationInfo")
                if affiliation:
                    affiliation = affiliation.find("Affiliation").text
                initials = tree_text(author, "Initials")
                first_name = tree_text(author, "ForeName")
                last_name = tree_text(author, "LastName")
                my_initials = initials
                if not my_initials:
                    my_initials = ""
                my_last_name = last_name
                if not my_last_name:
                    my_last_name = ""
                full_name = f"{my_initials} {my_last_name}".strip()

                author_list.append(
                    {
                        "last_name": last_name,
                        "first_name": first_name,
                        "initials": initials,
                        "affiliation": affiliation,
                        "full_name": full_name,
                    }
                )

        mesh = None
        if mesh_heading is not None:
            mesh = []
            for item in mesh_heading.getchildren():
                item = item.find("DescriptorName")
                if item is not None:
                    mesh.append({"text": item.text, "mesh_id": item.get("UI")})
        return {
            "pmid": int(pmid),
            "mesh": [item["text"] for item in mesh] if mesh else [],
            "authors": author_list,
            "doi": doi,
        }
    except AttributeError:
        return {}

def tree_text(tree, item):
    try:
        return tree.find(item).text
    except AttributeError:
        return None

def insert(pmids):
    initial_length = len(pmids)
    reject_count = 0
    while pmids:
        print(
            f"{len(pmids)} remaining out of {initial_length}; had to reject {reject_count}"
        )
        query_path = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/biocjson?pmids="
        count = 0
        my_ids = ""
        while pmids:
            my_pmid = int(pmids.pop())
            if not collection.find_one({'pmid': my_pmid}):
                my_ids += f"{my_pmid},"
                # limited to 2048 characters, 100 queries at a time
                if len(my_ids) > 1900 or count > 90:
                    break
                count += 1

        my_ids = my_ids.strip(",")
        query_path = query_path + my_ids
        pubmed_query_path = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="
            + my_ids
        )

        tree = ET.fromstring(paced_request(pubmed_query_path).text)

        for article in tree:
            processed_article = get_pubmed_data(article)
            if processed_article:
                pubmed_data = {
                    "mesh": processed_article["mesh"],
                    "authors": processed_article["authors"],
                    "doi": processed_article["doi"],
                }
                data = get_pubtator_data(processed_article["pmid"])
                data["pubtator"] = list(set([item['text'] for item in data['pubtator']['abstract_annotations']]))
                data["status"] = STATUS
                data["field_order"] = ["authors", "journal", "year", "mesh", "pubtator", "abstract"]
                if data["pmcid"]:
                    data["url"] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{data['pmcid']}/"
                else:
                    data["url"] = f"https://pubmed.gov/{data['pmid']}"
                data["notes"] = ""

                pubmed_data.update(data)
                collection.insert(pubmed_data)

if __name__ == "__main__":
    with open(PMID_FILE) as f:
        pmids = [int(line) for line in f]

    insert(pmids)
