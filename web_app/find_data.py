from elasticsearch import Elasticsearch
from datetime import datetime


def main():
    es = Elasticsearch("http://localhost:9200")

    resp = es.search(
        index="test-index",
        query={"match": {"text": {'query': "au"}}}
    )
    print(f"Got {resp['hits']['total']['value']} Hits:")
    for hit in resp['hits']['hits']:
        print(hit["_source"])


if __name__ == '__main__':
    main()
