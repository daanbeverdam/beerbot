from peewee import *
from database import ApplicationDatabase

class BeerMeal(Model):
    """The BeerMeal class epresents a beer_meal connection in the database."""
    id = PrimaryKeyField()
    name = CharField()
    class Meta:
        database = ApplicationDatabase.connect()