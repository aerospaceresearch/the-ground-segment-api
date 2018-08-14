from pprint import pprint
import json
import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID = "f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN = "1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/uploads/'

headers = {'Authorization': 'Token ' + NODE_TOKEN}

r = requests.get(url, headers=headers)
assert r.status_code == 200
pprint(json.loads(r.text))
