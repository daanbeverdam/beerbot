from peewee import *
from base import Base

class Beer(Base):
    """The Beer class epresents a beer entry in the database."""
    id = PrimaryKeyField()
    name = CharField()
    meal = CharField()
    mealcategory = CharField()
    kind = CharField()
    sweetness = IntegerField()
    bitterness = IntegerField()
    color = CharField()
    percentage = DecimalField()
    description = CharField()