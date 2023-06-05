#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip freeze -r requirements.txt
python manage.py migrate
python manage.py collectstatic
# python manage.py collectstatic --no-input