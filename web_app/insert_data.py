from elasticsearch import Elasticsearch
from datetime import datetime


def main():
    words_q = []
    with open('web_app/words.txt', 'r') as f:
        while f.readline():
            s = f.readline()
            s = s.replace('\n', '')
            words_q.append(s)

    print(len(words_q))
    es = Elasticsearch("http://localhost:9200")

    for index, word in enumerate(words_q):
        doc = {
            'text': word,
            'timestamp': datetime.now(),
        }
        es.index(index='test-index', document=doc)
        if index % 1000 == 0:
            print(f'Index is {index}, word is {word}')


if __name__ == '__main__':
    main()
