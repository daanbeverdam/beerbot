from pybot.command import Command


class StartCommand(Command):
    """Start command that start the bots and checks whether or not a
    user is already in the database."""

    def reply(self):
        # check if user is in database
        return {'message': self.dialogs['reply']}
