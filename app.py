from elasticsearch import Elasticsearch
import requests
import json

# connect to our cluster
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# let's iterate over swapi people documents and index them

i = 1

while True:
    r = requests.get('http://swapi.co/api/people/' + str(i))

    if r.status_code != 200:
        break

    es.index(index='sw', doc_type='people', id=i+1, body=json.loads(r.content))
    i += 1

person = es.get(index='sw', doc_type='people', id=5)

print(f"person: {person}")
