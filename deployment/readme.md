### deployment using docker

1) install server with docker

2) checkout this repository

3) add production.py

```
# coding=utf-8

import os
from .base import *

DEBUG=False
SECRET_KEY = 'ADD SOMETHING SECRET WITH SOME CHARACTERS HERE'
STATIC_ROOT = '/opt/data/gsapi/static/'
MEDIA_ROOT = '/opt/data/gsapi/media/'

ALLOWED_HOSTS = ['*']
```

4) create database container

```
docker run -d --restart=always --name gsapi-db postgres:10
```

5) create data folder

```
mkdir ../../data
chown 1000 ../../data
```

(this folder should be outside of git checkout and Dockerfile)

5) first run of update.sh

comment both ``docker rm`` lines and run ``update.sh``

