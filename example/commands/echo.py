from pybot.command import Command


class EchoCommand(Command):

    def reply(self):
        if self.arguments.lower() == 'help':
            return {'message': self.usage}
        return {'message': self.arguments}
