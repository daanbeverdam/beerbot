from peewee import *
from base import Base

class Beer(Base):
    """The Beer class epresents a beer entry in the database."""
    id = PrimaryKeyField()
    name = CharField()