from beer import Beer
from meal import Meal
from beer_meal import BeerMeal

class BeerAdvisor(object):
    """Main class which manipulates and retrieves data from the database in
    order to generate beer recommendations."""

    def __init__(self):
        self.meal = None # will contain meal object representing user input

    def find_match(self):
        query = BeerMeal.select().where(BeerMeal.meal_id == self.meal.id)
        candidate_beers = []
        for relation in query:
            candidate = Beer.get(Beer.id == relation.beer_id)
            candidate_beers.append(candidate)
        return str(candidate_beers)

    def input_meal(self, meal_name):
        meal_id = self.get_meal_id(meal_name)
        if meal_id:
            self.meal = Meal(id=meal_id, name=meal_name) # construct meal object

    def get_meal_id(self, meal_name):
        meals = Meal.select() # select all meals in the database
        for meal in meals:
            if meal.name == meal_name:
                return meal.id # return id if meal is found in the database
        return None # return None if meal is not in the database
