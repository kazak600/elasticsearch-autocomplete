import requests
import json


def find(query):
    suggest_query = {
        "suggest": {
            'text_suggest': {
                'prefix': query,
                'completion': {
                    'field': 'text',
                    'size': 5,
                    'skip_duplicates': 'true',
                    'fuzzy': {
                        'fuzziness': 'auto:1,3',
                        'transpositions': 'true',
                        'min_length': 3,
                        'prefix_length': 1
                    }
                }
            }
        }
    }
    response = requests.post(
        url="http://localhost:9200/test-index/_search",
        data=json.dumps(suggest_query),
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())


if __name__ == '__main__':
    while True:
        try:
            query_word = input('Please input search word: ')
            find(query=query_word)
        except KeyboardInterrupt:
            break
