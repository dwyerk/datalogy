#!/bin/bash
cd /app
gulp &
sleep 2
pipenv run datalogy/manage.py runserver 0.0.0.0:8000

