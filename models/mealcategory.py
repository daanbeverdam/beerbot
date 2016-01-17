from peewee import *
from base import Base

class MealCategory(Base):
    """Corresponds to the mealcategory table in the database."""
    id = PrimaryKeyField()
    name = CharField()