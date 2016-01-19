from beer import Beer
from meal import Meal
from beer_meal import BeerMeal
from mealcategory import MealCategory
from user import User

class BeerAdvisor(object):
    """Main class which manipulates and retrieves data from the database in
    order to generate beer recommendations."""

    def __init__(self):
        self.meal = None # will contain meal that user inputs
        self.category = None # will contain category that user inputs

    def find_match(self):
        candidate_beers = []

        if self.meal: # if user input is a meal
            query = BeerMeal.select().where(BeerMeal.meal_id == self.meal.id)
            for relation in query:
                candidate = Beer.get(Beer.id == relation.beer_id)
                candidate_beers.append(candidate)
        elif self.category: # if user input is a meal category
            pass # TODO implement match finding via category

        if len(candidate_beers) > 0:
            return candidate_beers[0] # for now just return the first beer
        else:
            self.emergency_plan(sirens=True) # What? No beer? This shouldn't happen. Sound the alarm!

    def input_meal(self, meal_name):
        self.meal = Meal.get(Meal.name == meal_name)

    def input_category(self, category_name):
        self.category = MealCategory.get(MealCategory.name == category_name)

    def check_database_for(self, meal_name=None, beer_name=None,
                           category_name=None, user_chat_id=None):
        """Checks the database for various things. Returns truth value."""
        if meal_name:
            query = Meal.select().where(Meal.name == meal_name)
        elif beer_name:
            query = Beer.select().where(Beer.name == beer_name)
        elif category_name:
            query = MealCategory.select().where(MealCategory.name == category_name)
        elif user_chat_id:
            query = User.select().where(User.chat_id == user_chat_id)
        else:
            print 'No query specified!'
            return False
        if len(query) > 0:
            return True # return true when results are found
        return False

    def get_categories(self, desired_categories='meal'):
        """Gets categories from the database and returns them as a list."""
        if desired_categories == 'meal':
            query = MealCategory.select()
            categories = [category.name for category in query]
        return categories

    def emergency_plan(self, sirens=False):
        if sirens:
            print "Sound the alarm! PEEEWEEEWEEE!"
        else:
            print "Sound the alarm! *silent alarm*"

