from elasticsearch import Elasticsearch


def find(elastic, query):
    resp = elastic.search(
        index="test-index",
        query={"match": {"text": {'query': query}}}
    )
    print(f"Got {resp['hits']['total']['value']} Hits:")
    for hit in resp['hits']['hits']:
        print(hit["_source"])


if __name__ == '__main__':
    es = Elasticsearch("http://localhost:9200")

    while True:
        try:
            query_word = input('Please input search word: ')
            find(elastic=es, query=query_word)
        except KeyboardInterrupt:
            break
