import os

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"

import django

django.setup()

from django.core.asgi import get_asgi_application
from cassandra.cqlengine.management import sync_table

from backend.db.cassandradb import get_session
from books.models import Book

global DB_SESSION

application = get_asgi_application()

print("Syncing Cassandra Tables...")
DB_SESSION = get_session()

sync_table(Book)

print("Synced Cassandra Tables.")
