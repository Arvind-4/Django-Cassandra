"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()

import os

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"
# os.environ["CASSANDRA_FALLBACK_ORDER_BY_PYTHON"] = "true"

import django

django.setup()

import pathlib
from django.core.asgi import get_asgi_application
from cassandra.cqlengine.management import sync_table

# from scripts.encryptdb import encrypt_dir, decrypt_dir

from backend.scripts.encryptdb import encrypt_dir, decrypt_dir

from backend.db.cassandradb import get_session
from books.models import Book

BUNDLE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

encrypt_dir(BUNDLE_DIR / "ignored", BUNDLE_DIR / "encrypted")
decrypt_dir(BUNDLE_DIR / "encrypted", BUNDLE_DIR / "decrypted")

global DB_SESSION

application = get_asgi_application()

print("Syncing Cassandra keyspace...")
DB_SESSION = get_session()

sync_table(Book)

print("Synced Cassandra keyspace.")
