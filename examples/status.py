import datetime
import psutil
import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID = "f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN = "1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/status/'

cpu_count = psutil.cpu_count()
cpu_load = psutil.cpu_percent(interval=2) / 100.0 * cpu_count

headers = {'Authorization': 'Token ' + NODE_TOKEN}
payload = {'status_code': 'OK',
           'node_time_utc': str(datetime.datetime.utcnow()),
           'data': {
               'load': str(cpu_load),
               'cpu_count': cpu_count
               }
           }

r = requests.post(url, json=payload, headers=headers)
assert r.status_code == 201
print(r.text)
