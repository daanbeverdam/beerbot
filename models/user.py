from peewee import *
from base import Base

class User(Base):
    """Represents an user in the database."""
    id = PrimaryKeyField()
    chat_id = IntegerField()
    name = CharField()
    preferences_id = IntegerField()