from beer import Beer
from meal import Meal
from beer_meal import BeerMeal
from mealcategory import MealCategory

class BeerAdvisor(object):
    """Main class which manipulates and retrieves data from the database in
    order to generate beer recommendations."""

    def __init__(self):
        self.meal = None # will contain meal that user inputs
        self.category = None # will contain category that user inputs

    def find_match(self):
        query = BeerMeal.select().where(BeerMeal.meal_id == self.meal.id)
        candidate_beers = []
        for relation in query:
            candidate = Beer.get(Beer.id == relation.beer_id)
            candidate_beers.append(candidate)
        if len(candidate_beers) > 0:
            return candidate_beers[0]
        else:
            pass # What? No beer? This shouldn't happen. Do something to fix!

    def input_meal(self, meal_name):
        self.meal = Meal.get(Meal.name == meal_name)

    def input_category(self, category_name):
        self.category = MealCategory.get(MealCategory.name == category_name)

    def check_database_for(self, meal_name=None, beer_name=None,
                           category_name=None):
        """Checks whether or not a meal or beer name is in the database."""
        if meal_name:
            query = Meal.select().where(Meal.name == meal_name)
        elif beer_name:
            query = Beer.select().where(Beer.name == beer_name)
        elif category_name:
            query = MealCategory.select().where(MealCategory.name == category_name)
        else:
            print 'No meal or beer name specified!'
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
