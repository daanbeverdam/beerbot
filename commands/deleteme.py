from pybot.command import Command
from models.system import BeerAdvisor
from models.user import User


class DeleteMeCommand(Command):
    """Something here"""

    def reply(self):
        User.get(User.chat_id == self.message.chat_id).delete_instance()
        return {'message': self.dialogs['reply']}