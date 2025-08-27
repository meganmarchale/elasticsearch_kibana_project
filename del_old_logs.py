from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200")
client.indices.delete(index="logs", ignore=[400, 404])