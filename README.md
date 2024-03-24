# Api ElasticSearch

Api usando o FastApi para fazer busca no ElasticSearch

#### Comando elastic

### Instalação do ElasticSearch e kibana com docker

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

### Reset senha do kibana_system

```
docker exec -it api_elasticsearch-elastic-1 /usr/share/elasticsearch/bin/elasticsearch-reset-password -i -u kibana_system --url https://localhost:9200/
```

### Copiando Certificado

```
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
```
