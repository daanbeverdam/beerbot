from peewee import *
from base import Base

class MealCategory(Base):
    """Corresponds to the mealcategory table in the database."""
    id = PrimaryKeyField()
    beer_id = IntegerField()
    meal_id = IntegerField()