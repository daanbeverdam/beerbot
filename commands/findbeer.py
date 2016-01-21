from pybot.command import Command
from models.system import BeerAdvisor
from models.user import User
import StringIO

class FindBeerCommand(Command):

    def reply(self):
        """Main function of the command (required by the PyBot framework)."""
        if not self.user_exists(self.message.chat_id):
            return {'message': 'Please enter your preferences first by using /start.'}
        elif self.is_active():
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
        user = User.get(User.chat_id == self.message.chat_id)
        system.input_data(query, user)
        recommended_beer = system.find_match() # find a match
        if recommended_beer:
            self.activate(False) # deactivates the listener
            reply = self.format_reply(recommended_beer) # turn the beer object into a human readable reply
            return reply # return the reply to the user
        else:
            meal_categories = system.get_categories()
            keyboard = self.format_keyboard(meal_categories)
            return {'message': self.dialogs['no_such_meal'] % query, 'keyboard': keyboard}

    def format_reply(self, recommended_beer):
        """Returns a human readable reply. Input should be a beer object."""
        caption = "My advice would be: " + recommended_beer.name
        image_id = str(recommended_beer.imageid) # if recommended_beer.imageid < 9 else str(1)
        try:
            photo = open('media/' + image_id + '.jpg').read()
            photo = StringIO.StringIO(photo).getvalue()
            return {'photo': photo, 'caption': caption}
        except:
            return {'message': caption + ". Sorry I don't have a photo yet!"}

    def user_exists(self, chat_id):
        try:
            User.get(User.chat_id == chat_id)
            return True
        except:
            return False