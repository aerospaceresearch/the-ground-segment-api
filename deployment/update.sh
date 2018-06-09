#!/bin/sh

cd ..

set -e

git pull
docker pull python:3.6
docker build --tag=gsapi-prod .
docker rm -f gsapi
docker run -d --link gsapi-db:db -v `pwd`/../data/:/opt/data/ -v `pwd`/gsapi/gsapi/settings/production.py:/opt/code/gsapi/gsapi/settings/production.py --restart=always --name gsapi gsapi-prod
docker rm -f gsapi-nginx
docker run --name gsapi-nginx --net="host" --volumes-from gsapi -v `pwd`/deployment/nginx.conf:/etc/nginx/nginx.conf --restart=always -d nginx

echo "Cleaning up old docker images..."
docker rmi $(docker images | grep "<none>" | awk '{print($3)}')
cd -
