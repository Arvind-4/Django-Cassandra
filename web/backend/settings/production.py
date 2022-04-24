import os
from dotenv import load_dotenv

from .base import *

load_dotenv()

SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY", "BAD-KEY"))

DEBUG = bool(int(os.environ.get("DJANGO_DEBUG", "1")))

ALLOWED_HOSTS = []

ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get("DJANGO_ALLOWED_HOSTS").split(","),
    )
)

INSTALLED_APPS = DEFAULT_DJANGO_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "static"

CASSANDRA_FALLBACK_ORDER_BY_PYTHON = True

ASTRA_DB_KEYSPACE = str(os.environ.get("ASTRA_DB_KEYSPACE"))
