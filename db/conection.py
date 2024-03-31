import os
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from typing import List
import pandas as pd
from loguru import logger

client = Elasticsearch(
    os.environ["HOST"],
    ca_certs=os.environ["CA_CRT"],
    basic_auth=(os.environ["ELASTIC_USER"], os.environ["ELASTIC_PASSWORD"]),
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
        "match", bloco=term_match
    )  # .exclude("match", description="beta")

    response = search_query.execute()

    for hit in response:
        lista_resp.append({"score": hit.meta.score, "bloco": hit.bloco})
    return lista_resp

def insert_data():
    "Inserindo dados usando a api body"
    df = pd.read_csv("dados.csv")
    doc = {}
    for i in df.itertuples():
        doc["bloco"] = i.text_bloco
        resp = client.index(index="bloco_text", body=doc)
        logger.info("Dados inseridos:", resp["result"])
