#!/usr/bin/env bash
# exit on error
set -o errexit

apt-get update
apt-get install python3
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate