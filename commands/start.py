from pybot.command import Command
from models.system import BeerAdvisor
from models.user import User


class StartCommand(Command):
    """Start command that start the bots and checks whether or not a
    user is already in the database."""

    def reply(self):
        if self.user_exists(self.message.chat_id) and not self.is_active():
            return {'message': self.dialogs['reply']}
        if not self.user_exists(self.message.chat_id) and self.is_active():
            return self.register_preferences()
        else: # New here?
            self.activate()
            self.data['register_phase'] = 0
            return self.create_user(self.message.chat_id, self.message.first_name_sender)

    def user_exists(self, chat_id):
        system = BeerAdvisor()
        return system.check_database_for(user_chat_id=chat_id)

    def create_user(self, chat_id, name):
        self.data['new_user'] = User(chat_id=chat_id, name=name) # create new user object
        # TODO: remove hardcoded dialogs
        return {'message': self.dialogs['new_user'], 'keyboard': [["Okay, let's do this!"]]}

    def register_preferences(self):
        self.data['register_phase'] += 1
        likert_scale = self.format_keyboard(range(1, 6), 5)
        percentages = [['<5%', '5%-8%', '>8%']]
        colors = [['light','dark']]

        try:
            if self.data['register_phase'] == 1:
                return {'message': self.dialogs['color'], 'keyboard': colors}

            elif self.data['register_phase'] == 2:
                user = self.data['new_user']
                user.color = self.message.text
                self.data['new_user'] = user
                return {'message': self.dialogs['bitterness'], 'keyboard': likert_scale}

            elif self.data['register_phase'] == 3:
                user = self.data['new_user']
                user.bitterness = int(self.message.text)
                self.data['new_user'] = user
                return {'message': self.dialogs['sweetness'], 'keyboard': likert_scale}

            elif self.data['register_phase'] == 4:
                user = self.data['new_user']
                user.sweetness = int(self.message.text)
                self.data['new_user'] = user
                return {'message': self.dialogs['alcohol'], 'keyboard': percentages}

            elif self.data['register_phase'] == 5:
                user = self.data['new_user']
                user.percentage = self.message.text
                self.data['new_user'] = user
                self.data['new_user'].save() # save user to database
                self.activate(False) # deactivate the listener
                return {'message': self.dialogs['user_registered'], 'keyboard': None}
        except:
            self.data['register_phase'] == 0
            self.activate(False)
            return {'message': self.dialogs['whoops!'], 'keyboard': None}