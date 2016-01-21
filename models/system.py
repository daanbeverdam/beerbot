from beer import Beer
from meal import Meal
from beer_meal import BeerMeal
from mealcategory import MealCategory
from user import User
import random

class BeerAdvisor(object):
    """Main class which manipulates and retrieves data from the database in
    order to generate beer recommendations."""

    def __init__(self):
        self.input = None # will contain the user input (meal)
        self.user = None # will contain the user info and preferences

    def find_match(self):
        candidate_beers = [] # empty array which will contain the cadidates
        # Each bear is coupled to a meal(category). If a beer's meal(category)
        # is the same as the user input it will be considered a candidate.

        # First, we search meal names:
        query = Beer.select().where(Beer.meal == self.input)
        if len(query) > 0: # if the query yields some beers...
            for candidate in query:
                if candidate.name not in [beer.name for beer in candidate_beers]:
                    candidate_beers.append(candidate) #...add those beers to the candidate list

        # Second, we search meal categories:
        query = Beer.select().where(Beer.mealcategory == self.input)
        if len(query) > 0: # if the query yields some beers...
            for candidate in query:
                if candidate.name not in [beer.name for beer in candidate_beers]:
                    candidate_beers.append(candidate) #...add those beers to the candidate list

        # And lastly, we return the best choice:
        if len(candidate_beers) > 0: # if there are any candidate beers...
            candidate_beers = self.assign_scores(candidate_beers) # assign penalty scores to those beers
            candidate_beers.sort(key=lambda x: x.penalties) # sort the candidate list ascending by penalty count

            # This code block prints all the found candidates and their penalty
            # scores to the terminal. Uncomment for debugging purposes, or if
            # you're just curious. ;-)
            for beer in candidate_beers:
               print beer.name
               print beer.penalties

            return candidate_beers[0] # return the first (best) candidate

        else: # if there are no candidate beers...
            self.emergency_plan(sirens=True) # ...sound the alarm!
            return None

    def assign_scores(self, candidate_beers):
        percentages = {'<5%': '<5', '5%-8%': '>=5 and %s <= 8', '>8%': '>8'}

        # For every beer in the candidate list the system will assign penalties
        # if the beer properties don't match the user preferences.
        for beer in candidate_beers:
            beer.penalties = 0

            if beer.color != self.user.color: # if the colors don't match...
                beer.penalties += 1 #... give a penalty to that beer

            if not eval(str(beer.percentage) + percentages[self.user.percentage] % str(beer.percentage)):
                beer.penalties += 1 # assign penalty if alcohol percentage is not in preferred range

            # Penalties for sweetness and bitterness is the difference between
            # the beer taste properties and the user taste preferences:
            beer.penalties += abs(beer.sweetness - self.user.sweetness)
            beer.penalties += abs(beer.bitterness - self.user.bitterness)

        return candidate_beers

    def input_data(self, query, user):
        self.input = query
        self.user = user

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

