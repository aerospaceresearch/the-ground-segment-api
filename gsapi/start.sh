#!/bin/bash
export DJANGO_SETTINGS_MODULE=gsapi.settings.production
export PYTHONUNBUFFERED=0
mkdir -p /opt/data/gsapi
mkdir -p /opt/data/gsapi/logs
mkdir -p /opt/data/gsapi/run
chmod -R 777 /opt/data/gsapi/run
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn gsapi.wsgi:application --log-level=info --bind=unix:/opt/data/gsapi/run/server.sock -w 3
