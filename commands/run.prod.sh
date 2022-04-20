#!/bin/bash

cd web
gunicorn backend.asgi:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000