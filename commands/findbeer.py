from pybot.command import Command
from models.system import BeerAdvisor

class FindBeerCommand(Command):

    def reply(self):
        """Main function of the command (required by the PyBot framework)."""
        if self.is_active():
            self.activate(False) # deactivates the listener
            return self.handle_input(self.message.text)
        elif self.arguments:
            return self.handle_input(self.arguments)
        else:
            self.activate() # activates the listener so it can receive input
            keyboard = self.format_keyboard(BeerAdvisor().get_categories())
            return {'message': self.dialogs['specify'], 'keyboard': keyboard}

    def handle_input(self, query):
        """Handles the input from the user and returns appropriate message."""
        system = BeerAdvisor() # initialize beer advisory system

        if system.check_database_for(meal_name=query):  # check if name in database
            system.input_meal(query)  # input meal by name
        elif system.check_database_for(category_name=query):  # check if category in database
            system.input_category(query)  # input category
        else:
            meal_categories = system.get_categories()
            keyboard = self.format_keyboard(meal_categories)
            return {'message': self.dialogs['no_such_meal'], 'keyboard': keyboard}

        recommended_beer = system.find_match() # find a match
        reply = self.format_reply(recommended_beer) # turn the beer object into a human readable reply
        return {'message': reply, 'keyboard': None} # return the reply to the user

    def format_reply(self, recommended_beer):
        """Returns a human readable reply. Input should be a beer object."""
        return recommended_beer.name # for now just returns the name
        # much TODO

    def get_picture(self):
        """Gets the image associated with the beer."""
        pass # much TODO
