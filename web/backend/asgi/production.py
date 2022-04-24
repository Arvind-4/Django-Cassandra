import os
import pathlib

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"

import django

django.setup()

from django.core.asgi import get_asgi_application
from cassandra.cqlengine.management import sync_table

from backend.db.cassandradb import get_session
from backend.scripts.encryptdb import encrypt_dir, decrypt_dir
from books.models import Book

BUNDLE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent

encrypt_dir(BUNDLE_DIR / "ignored", BUNDLE_DIR / "encrypted")
decrypt_dir(BUNDLE_DIR / "encrypted", BUNDLE_DIR / "decrypted")

global DB_SESSION

application = get_asgi_application()

print("Syncing Cassandra Tables...")
DB_SESSION = get_session()

sync_table(Book)

print("Synced Cassandra Tables.")
