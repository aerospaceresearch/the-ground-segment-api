import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID="f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN="1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/upload/'

headers = {'Authorization': 'Token ' + NODE_TOKEN}
payload = {'upload_type': 'testupload'}
files = {'upload': open('test10.raw', 'rb')}

r = requests.post(url, data=payload, headers=headers, files=files)
print(r.text)
