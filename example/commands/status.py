from pybot.command import Command


class StatusCommand(Command):

    def reply(self):
        return {'message': self.dialogs['reply']}
