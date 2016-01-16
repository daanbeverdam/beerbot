from peewee import *
from base import Base

class BeerMeal(Base):
    """The BeerMeal class epresents a beer_meal connection in the database."""
    id = PrimaryKeyField()
    beer_id = IntegerField()
    meal_id = IntegerField()