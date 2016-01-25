from pybot.command import Command
from models.system import BeerAdvisor
from models.user import User


class DeleteMeCommand(Command):
    """Deletes an user from the database."""
    def reply(self):
        if self.is_active() and self.message.text == 'Yes':
            self.activate(False)
            try:
                User.get(User.chat_id == self.message.chat_id).delete_instance()
                return {'message': self.dialogs['reply'], 'keyboard': None}
            except:
                return {'message': "You're already deleted!", 'keyboard': None}
        if self.is_active() and self.message.text == 'No':
            self.activate(False)
            return {'message': "Ok, I won't delete you.", 'keyboard': None}
        else:
            self.activate()
            return {'message': "Are you sure?", 'keyboard': [['Yes', 'No']]}