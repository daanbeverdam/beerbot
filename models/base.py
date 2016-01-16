from peewee import *
from database import ApplicationDatabase

class Base(Model):
    """A base Model which contains database info."""
    class Meta:
        database = ApplicationDatabase()
        database = database.get()