from peewee import *
from database import ApplicationDatabase

class Meal(Model):
    """The Meal class epresents a meal entry in the database."""
    id = PrimaryKeyField()
    name = CharField()
    class Meta:
        database = ApplicationDatabase()
        database = database.connect()