from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from typing import List

client = Elasticsearch(
    "https://localhost:9200",
    # "https://elastic:9200",
    # ca_certs="/usr/share/elasticsearch/config/certs/ca/ca.crt",
    ca_certs="ca.crt",
    basic_auth=("elastic", "elastic"),
)


def search_match(term_match: str):
    """
        fazendo busca usando o "match" no elasticsearch
    Args:
        term_match (str): texto para fazer a busca

    Returns:
        List[Dict]: Lista com score e o resultado da busca
    """
    lista_resp: List = []

    search_query = Search(using=client).query(
        "match", name=term_match
    )  # .exclude("match", description="beta")

    response = search_query.execute()

    for hit in response:
        # print(hit.meta.score, hit.name)
        lista_resp.append({"score": hit.meta.score, "name": hit.name})
    return lista_resp
