from peewee import *
from base import Base

class Preferences(Base):
    """Represents the preferences table in the database."""
    id = PrimaryKeyField()
    color = IntegerField()
    bitternes = CharField()
    sweetness = IntegerField()
    percentage = DecimalField()