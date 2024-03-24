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


def search(term: str):
    lista_resp: List = []
    search_query = Search(using=client).query(
        "match", name="Tale"
    )  # .exclude("match", description="beta")

    response = search_query.execute()

    for hit in response:
        print(hit.meta.score, hit.name)
        lista_resp.append({"score": hit.meta.score, "name": hit.name})
    return lista_resp
