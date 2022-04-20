#!/bin/bash

source .env

cd web

echo "Deleting cache and migration files ..."

find . -path "*/migrations/*" -name "*.py" -not -path "*__init__*" -delete
find . -path "*/migrations/*" -name "*.pyc" -delete
find . -path "*/__pycache__/*" -name "*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -rf {} +

rm -rf __pycache__
rm -rf *.sqlite3

echo "Makemigrations and Migrate DB ..."

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Creating Superuser ..."

DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME \
DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD \
DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL \
python manage.py createsuperuser --noinput


