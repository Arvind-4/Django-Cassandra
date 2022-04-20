import os
import pathlib

from dotenv import load_dotenv

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import (
    register_connection,
    set_default_connection,
)
from django.conf import settings

load_dotenv()

ASTRA_DB_CLIENT_ID = os.environ.get("ASTRA_DB_CLIENT_ID")
ASTRA_DB_CLIENT_SECRET = os.environ.get("ASTRA_DB_CLIENT_SECRET")

BUNDLE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent

if settings.DEBUG:
    print("From Ignored ...")
    CONNECT_BUNDLE = BUNDLE_DIR / "ignored" / "connect.zip"
else:
    print("From Decrypt ...")
    CONNECT_BUNDLE = BUNDLE_DIR / "decrypted" / "connect.zip"


def get_cluster():
    cloud_config = {"secure_connect_bundle": str(CONNECT_BUNDLE)}
    auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster


def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    register_connection(str(session), session=session)
    set_default_connection(str(session))
    return session
