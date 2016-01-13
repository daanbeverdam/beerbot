from peewee import *
from database import ApplicationDatabase

class Beer(Model):
    """The Beer class epresents a beer entry in the database."""
    id = PrimaryKeyField()
    name = CharField()
    class Meta:
        database = ApplicationDatabase.connect()
