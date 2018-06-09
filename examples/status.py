import datetime
import psutil
import requests

## requirements: python (tested windows, linux)

## modify:
NODE_UUID="f5dba253-c0ea-475e-9f8b-3733168dc42e"
url = 'http://localhost:8023/api/v1/nodes/' + NODE_UUID + '/status/'

cpu_count = psutil.cpu_count()
cpu_load = psutil.cpu_percent(interval=2) / 100.0 * cpu_count

payload = {'status_code': 'OK',
           'node_time_utc': str(datetime.datetime.utcnow()),
           'data': {
               'load': str(cpu_load),
               'cpu_count': cpu_count
               }
           }

r = requests.post(url, json=payload)
print(r.text)