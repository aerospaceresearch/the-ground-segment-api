import os.path
import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID = "f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN = "1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/upload/'

headers = {'Authorization': 'Token ' + NODE_TOKEN}
payload = {'upload_type': 'testupload'}
files = {'upload': open('test10.raw', 'rb')}

r = requests.post(url, data=payload, headers=headers, files=files)
assert r.status_code == 201
print(r.text)
upload_url = r.json()['upload']

# download file
r = requests.get(upload_url, stream=True)
path = 'test10.raw.download'
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

print(os.path.getsize(path))
