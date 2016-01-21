from peewee import *
from base import Base

class User(Base):
    """Represents an user in the database."""
    # User information:
    id = PrimaryKeyField()
    chat_id = IntegerField() # Telegram chat id
    name = CharField() # First name
    # Preferences of the user:
    color = CharField() # light or dark
    bitterness = IntegerField() # 1-5 scale
    sweetness = IntegerField() # 1-5 scale
    percentage = CharField() # alcohol percentage