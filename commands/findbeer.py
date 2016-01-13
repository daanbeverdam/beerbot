from pybot.command import Command

class FindBeerCommand(Command):

    def reply(self):
        # do something to find beer
        reply = 'Beer found!'
        return {'message': reply}
