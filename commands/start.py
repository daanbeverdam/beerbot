from pybot.command import Command
from models.system import BeerAdvisor


class StartCommand(Command):
    """Start command that start the bots and checks whether or not a
    user is already in the database."""

    def reply(self):
        # check if user is in database
        if self.user_exists(self.message.chat_id):
            return {'message': self.dialogs['reply']}
        else:
            return self.register_user(self.message.chat_id, self.message.first_name_sender)

    def user_exists(self, chat_id):
        system = BeerAdvisor()
        return system.check_database_for(user_chat_id=chat_id)

    def register_user(self, chat_id, name):
        system = BeerAdvisor()
        system.register_user(chat_id, name)
        return {'message': self.dialogs['user_registered']}



