import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model as PythonCassandraModel
from django_cassandra_engine.models import DjangoCassandraModel
from django.conf import settings

# Create your columns here.


class Book(DjangoCassandraModel, PythonCassandraModel):
    __keyspace__ = settings.ASTRA_DB_KEYSPACE
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text(required=True)
    author = columns.Text()
    description = columns.Text()

    class Meta:
        ordering = ("title",)
        db_table = "books"

    def __str__(self):
        return self.title
