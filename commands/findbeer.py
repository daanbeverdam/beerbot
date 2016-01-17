from pybot.command import Command
from models.system import BeerAdvisor

class FindBeerCommand(Command):

    def reply(self):
        if self.is_active():
            self.activate(False) # deactivates the listener
            return self.handle_input(self.message.text)
        elif self.arguments:
            return self.handle_input(self.arguments)
        else:
            self.activate() # activates the listener so it can receive input
            return {'message': self.dialogs['specify']}

    def handle_input(self, query):
        system = BeerAdvisor() # initialize beer advisory system
        if system.check_database_for(query):  # check if name in the database
            system.input_meal(query)  # input meal by name
            # TODO: input meal by category?
            recommended_beer = system.find_match() # find a match
            reply = self.format_reply(recommended_beer) # turn the beer object into a human readable reply
            return {'message': reply} # return the reply to the user
        else:
            meal_categories = system.get_categories()
            return {'message': self.dialogs['no_such_meal']} # or disappoint them

    def format_reply(self, recommended_beer):
        """Returns a human readable reply. Input should be a beer object."""
        return recommended_beer.name # for now just returns the name
        # much TODO

    def get_picture(self):
        """Gets the image associated with the beer."""
        pass # much TODO
