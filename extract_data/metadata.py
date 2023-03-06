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

SETTINGS_PATH = "/home/bitnami/modeldb-settings.json"

with open(SETTINGS_PATH) as f:
    security = json.load(f)

mongodb = MongoClient()
sdb = mongodb[security["db_name"]]
sdb.authenticate(security["mongodb_user"], security["mongodb_pw"])

invalid_doi = set() # for Error: Invalid response from Entrez PubMed API
@functools.lru_cache()
def lookup_pmid_from_doi(doi):
    """code adapted from ChatGPT 2023-02-14"""
    if "dryad" not in doi:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={doi}&retmode=json"
        data = requests.get(url).json()
    else:
        invalid_doi.add(doi)

    # Extract the PMID, if it exists
    if "dryad" not in doi and "esearchresult" in data and "idlist" in data["esearchresult"]:
        if "errorlist" in data["esearchresult"]:
            invalid_doi.add(doi)
            return None
        else:
            id_list = data["esearchresult"]["idlist"]
            if len(id_list) > 0:
                print(doi)
                assert(len(id_list) == 1)
                pmid = id_list[0]
                return pmid
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
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def new_author_check(author_name): 
    stripped_author_name = author_name.strip()
    return sdb.authors.find_one({"object_name": {"$regex": re.compile(f"^{stripped_author_name}$", re.IGNORECASE)}}) is None and sdb.authors.find_one({"object_name": {"$regex": re.compile(f"^{strip_accents(stripped_author_name)}$", re.IGNORECASE)}}) is None 


invalid_author_db = set()
invalid_author_id = set()
def retrieve_author_object_id(author_name): 
    author = sdb.authors.find_one({"object_name": {"$regex": re.compile(f"^{author_name}$", re.IGNORECASE)}})
    if not author:
        author = sdb.authors.find_one({"object_name": {"$regex": re.compile(f"^{strip_accents(author_name)}$", re.IGNORECASE)}})
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
        if paper.get("doi") is None:
            no_pmid_or_doi.add(paper['id'])
            paper_id = False
            print(paper['id'], "has no ids")
        else:
            paper["pubmed_id"] = {"value": lookup_pmid_from_doi(paper["doi"]["value"])}
    if paper_id:
        if paper["pubmed_id"]:
            pmid = paper["pubmed_id"]["value"] 
            if pmid is None:
                print(f"paper {paper['id']} has no pubmed_id, but you can probably get the authors from crossref")
                papers_to_lookup_on_crossref.add(paper['id'])
    return pmid, paper["id"]


# check database for authors not in author collection
def check_authors():
    pmids_to_process = []
    papers = []
    for paper in sdb.papers.find({}, no_cursor_timeout=True):
        pmid, paper_id = get_pmid_from_paper(paper)
        if pmid is not None:
            pmids_to_process.append(pmid)
            papers.append(paper)
            if len(pmids_to_process) >= 99:
                get_author_info(pmids_to_process, papers)
                pmids_to_process = []
                papers = []
    get_author_info(pmids_to_process, papers)


def get_author_info(pmids_to_process, papers):
    metadata = get_metadata(pmids_to_process)
    # this assumes things are in the same order. If they're not, uh oh
    for paper, (pmid, my_metadata) in zip(papers, metadata.items()):
        if "authors" not in paper:
            paper["authors"] = {}
        paper["authors"]["value"] = my_metadata["authors"]["value"]
        print(paper["id"], paper["authors"]["value"])
        sdb.papers.update_one({"id": paper["id"]}, 
            {"$set": {
                "authors.value": paper["authors"]["value"],
                "doi": my_metadata["doi"],
                "journal": my_metadata["journal"], 
                "year": my_metadata["year"],
                "month": my_metadata["month"],
                "day": my_metadata["day"],
                }
            }
        
        )



# to delete
author_repeats = {}
def check_authors_old(): 
    for paper in sdb.papers.find({}, no_cursor_timeout=True): 
        if "authors" in paper:
            called_get_metadata = False
            paper_id = True
            for author in paper["authors"]['value']:
                if new_author_check(author["object_name"]): #can change to checking object id maybe
                    if paper.get("pubmed_id") is None:
                        if paper.get("doi") is None:
                            no_pmid_or_doi.add(paper['id'])
                            paper_id = False
                            print(paper['id'], "has no ids")
                        else:
                            paper["pubmed_id"] = {"value": lookup_pmid_from_doi(paper["doi"]["value"])}
                    if paper_id:
                        if paper["pubmed_id"]:
                            pmid = paper["pubmed_id"]["value"] 
                            if pmid is None:
                                print(f"paper {paper['id']} has no pubmed_id, but you can probably get the authors from crossref")
                                papers_to_lookup_on_crossref.add(paper['id'])
                                continue
                            print(pmid, paper["id"])
                            if called_get_metadata:
                                print(f"    papers metadata for authors doesn't match pubmed; hadn't found {author['object_name']}")
                                author_repeats[pmid] = author['object_name']
                            else:
                                called_get_metadata = True
                                get_metadata(
                                    pmid
                                )  


def add_new_author_to_collection(object_name, lastname, firstname, initials, orcid): 
    stripped_object_name = object_name.strip()

    matching_paper = sdb.papers.find_one({"authors.value.object_name": {"$regex": re.compile(f"^{stripped_object_name}$", re.IGNORECASE)}})
    if not matching_paper:
        matching_paper = sdb.papers.find_one({"authors.value.object_name": {"$regex": re.compile(f"^{strip_accents(stripped_object_name)}$", re.IGNORECASE)}})    
    if matching_paper:       
        for author in matching_paper["authors"]["value"]:
            if author["object_name"].lower() == stripped_object_name.lower():
                id_ = author["object_id"]
                break
        else:
            pattern = re.compile(f"^{strip_accents(stripped_object_name)}$", re.IGNORECASE)
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


"""
def get_title_metadata(article): 
def get_author_metadata(article):
def get_journal_metadata(article):
def get_doi_metadata(article):
def get_date_metadata(article):
"""


def get_text_content(node):
    content = ""
    for child_node in node.childNodes:
        if child_node.nodeType == child_node.TEXT_NODE:
            content += child_node.nodeValue
        elif child_node.nodeType == child_node.ELEMENT_NODE:
            content += get_text_content(child_node)
    return content


no_last_name = []
author_name_issues = {}
def get_metadata(pmids):
    metadata_w_pmid = {}

    for i in range(3):
        try:
            r = get_articles(pmids)
            doc = m.parseString(r.text)
            break
        except xml.parsers.expat.ExpatError:
            print("uh oh")
            print(r.text)
            print(f"attenpt {i} failed")
    else:
        print(f"I give up on {pmids}")
        raise Exception()

    articles = doc.getElementsByTagName("PubmedArticle")

    for article in articles:
        metadata = {}

        # pmid
        pmid = int(article.getElementsByTagName("PMID")[0].firstChild.nodeValue)
        pmid_dict = {}
        pmid_dict["value"] = pmid
        pmid_dict["attr_id"] = 153
        metadata["pubmed_id"] = pmid_dict

        # title
        # full_title = get_title_metadata(article)
        full_title = ''
        titles = article.getElementsByTagName("ArticleTitle")

        for title in titles:
            full_title += (get_text_content(title))
        
        if full_title is None:
            book_title = article.getElementsByTagName("BookTitle")
            if book_title is not None:
                full_title = get_text_content(book_title)
        assert full_title is not None

        title_dict = {}
        title_dict["value"] = full_title
        title_dict["attr_id"] = 139
        metadata["title"] = title_dict

        # authors
        # get_author_metadata(article)
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
                    author_last_name = author.getElementsByTagName("LastName")[0].firstChild.nodeValue
                else:
                    author_last_name = None
                    author_name_issues[pmid] = author_last_name

                if author.getElementsByTagName("ForeName"):
                    author_first_name = author.getElementsByTagName("ForeName")[0].firstChild.nodeValue
                else:
                    author_first_name = None
                    author_name_issues[pmid] = author_last_name

                if author.getElementsByTagName("Initials"):
                    author_initials = author.getElementsByTagName("Initials")[0].firstChild.nodeValue
                else:
                    author_initials = None
                    author_name_issues[pmid] = author_last_name                
                    

                if author_last_name and author_initials:
                    author_object_name = (
                        author_last_name
                        + " "
                        + author_initials
                    )
                elif author_last_name:
                    author_object_name = author_last_name
                elif author.getElementsByTagName("CollectiveName"):
                    author_object_name = author.getElementsByTagName("CollectiveName")[0].firstChild.nodeValue
                else:
                    #raise Exception(f"no last name?: {pmid}")
                    author_object_name = None
                    print(f"no author object_name:{pmid}")
                    no_last_name.append(pmid)
                    

                if author.getElementsByTagName("Identifier"):
                    if (
                        "ORCID"
                        == author.getElementsByTagName("Identifier")[0]
                        .getAttributeNode("Source")
                        .nodeValue
                    ):
                        author_orcid = author.getElementsByTagName("Identifier")[0].firstChild.nodeValue
                else:
                    author_orcid = None


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

                author_dict["object_id"] = author_object_id
                author_dict["object_name"] = author_object_name
                all_authors.append(author_dict)  # list of dictionaries

        authors_dict = {}
        authors_dict["value"] = all_authors
        authors_dict["attr_id"] = 148
        metadata["authors"] = authors_dict

        # journal
        # get_journal_metadata(journal)
        journal_title = article.getElementsByTagName("Title")[0].firstChild.nodeValue
        journal_dict = {}
        journal_dict["value"] = journal_title
        journal_dict["attr_id"] = 158
        metadata["journal"] = journal_dict















        #add journal volume










        # doi
        #def get_doi_metadata(article):
        if article.getElementsByTagName("ELocationID") and (
            "doi"
            == article.getElementsByTagName("ELocationID")[0]
            .getAttributeNode("EIdType")
            .nodeValue
        ):  # needs else statement, may not cover everything
            doi = article.getElementsByTagName("ELocationID")[0].firstChild.nodeValue
        else:
            doi = None
        doi_dict = {}
        doi_dict["value"] = doi
        doi_dict["attr_id"] = 339
        metadata["doi"] = doi_dict

        # date completed
        # def get_date_metadata(article):
        year = article.getElementsByTagName("Year")[0].firstChild.nodeValue 
        month = article.getElementsByTagName("Month")[0].firstChild.nodeValue
        day = article.getElementsByTagName("Day")[0].firstChild.nodeValue
        year_dict = {}
        year_dict["value"] = year
        year_dict["attr_id"] = 154
        metadata["year"] = year_dict

        month_dict = {}
        month_dict["value"] = month
        month_dict["attr_id"] = 156
        metadata["month"] = month_dict

        day_dict = {}
        day_dict["value"] = day
        day_dict["attr_id"] = 157
        metadata["day"] = day_dict

        metadata_w_pmid[pmid] = metadata

    return metadata_w_pmid


def get_reference_pmids(pmid):
    pmids_list = []
    dois_list = []
    r = requests.get(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    )
    doc = m.parseString(r.text)
    ids = doc.getElementsByTagName("ArticleIdList")
    for i in ids:
        if "pubmed" == i.getElementsByTagName("ArticleId")[0].getAttribute("IdType"):
            x = i.getElementsByTagName("ArticleId")[0].childNodes[0].nodeValue
            pmids_list.append(x)
        elif "doi" == i.getElementsByTagName("ArticleId")[0].getAttribute("IdType"):
            y = i.getElementsByTagName("ArticleId")[0].childNodes[0].nodeValue
            dois_list.append(y)
        # check_references_in_papers(x, y)

    if int(pmids_list[0]) = pmid:
        pmids = ",".join(pmids_list[1:])
    else:
        pmids = ",".join(pmids_list)
    dois = ",".join(dois_list)

    return pmids, dois

#check the references in the papers collection, add to papers collection or attach previous object id
#to be used in get_reference_pmids()
#def check_references_in_papers(pmid, doi):
 #   if sdb.papers.find_one("pubmed_id": pmid) is None:
  #  if sdb.papers.find_one("doi": doi) is None:


def get_reference_metadata(pmid):
    reference_pmids, reference_dois = get_reference_pmids(pmid)
    reference_metadata_dict = get_metadata(reference_pmids)
    #loop through reference_dois list // lookup_pmid_from_doi(reference_dois), reference_metadata_dict[pmid] = return 

    return reference_metadata_dict


if __name__ == "__main__":
    check_authors()
    #get_metadata(pmid)
    #get_reference_metadata(pmid)