#!/bin/sh

# Normally this will be read from the env
export PROMETHEUS_USERNAME="user"
export PROMETHEUS_PASSWORD="pass"
export TRAINING_USER='user'
export TRAINING_PASSWORD="pass"
#gunicorn -c gunicorn.py --log-config gunicorn_logging.conf wsgi:server
gunicorn -c gunicorn.py --log-config gunicorn_logging.conf wsgi:server > /log/logs.json 2>&1