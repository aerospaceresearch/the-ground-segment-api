import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID = "f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN = "1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/job/'

headers = {'Authorization': 'Token ' + NODE_TOKEN}
payload = {'start': '2018-08-04 18:00:00+0200',
           'stop': '2018-08-04 20:00:01+0200',
           'description': 'no description',
           'task': [
               {
                   'mode': 'rx',
                   'frequency': '145825000.0',
                   'samplerate': '2048000',
                   'gain': '0',
                   'chunksize': '300000000',
               }]}

r = requests.post(url, json=payload, headers=headers)
assert r.status_code == 201
print(r.text)
