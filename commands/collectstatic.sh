#!/bin/bash

cd web

rm -rf static && python manage.py collectstatic --noinput