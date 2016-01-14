from pybot.command import Command
from models.system import BeerAdvisor

class FindBeerCommand(Command):

    def reply(self):
        if self.arguments:
            system = BeerAdvisor()
            if system.input_meal(self.arguments):
                recommended_beer = system.find_match()
                return {'message': recommended_beer}
            else:
                return {'message': self.dialogs['no_such_meal']}
        else:
            self.activate() # activates the listener so it can receive input
            return {'message': self.dialogs['specify']}

    def format_reply(self):
        pass

    def get_picture(self):
        pass
