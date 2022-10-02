import requests
import json


def main():
    data = {
        "settings": {
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 1,
                "analysis": {
                    "analyzer": {
                        "phrase": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": ["lowercase", "shingle"]
                        }
                    },
                    "filter": {
                        "shingle": {
                            "type": "shingle",
                            "min_shingle_size": 2,
                            "max_shingle_size": 3
                        }
                    }
                }
            }
        },
        'mapping': {
            'properties': {
                'word': {
                    'analyzer': 'phrase'
                }
            }
        }
    }
    response = requests.put(
        url="http://localhost:9200/test-index/",
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())


if __name__ == '__main__':
    main()
