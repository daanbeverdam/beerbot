from peewee import *
from base import Base

class Meal(Base):
    """The Meal class epresents a meal entry in the database."""
    id = PrimaryKeyField()
    name = CharField()