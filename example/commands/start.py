from pybot.command import Command


class StartCommand(Command):
    # Every bot should have a start command

    def reply(self):
        return {'message': self.dialogs['reply']}
