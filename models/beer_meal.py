from peewee import *
from database import ApplicationDatabase

class BeerMeal(Model):
    """The BeerMeal class epresents a beer_meal connection in the database."""
    id = PrimaryKeyField()
    beer_id = IntegerField()
    meal_id = IntegerField()
    class Meta:
        database = ApplicationDatabase()
        database = database.connect()