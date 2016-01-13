import shelve
import traceback
import StringIO
import urllib


class Command(object):

    def __init__(self, name, dialogs, accepts_none=True, admin_id=0,
                 api_key=0, is_always_listening=False, language='en'):
        self.name = name
        self.dialogs = dialogs
        self.usage = dialogs['usage']
        self.message = None
        self.meta_commands = ['/done', '/cancel', '/results']
        self.data = None
        self.arguments = None
        self.accepts_none_argument = accepts_none
        self.admin = int(admin_id)
        self.api_key = api_key
        self.has_scheduled_event = False
        self.is_always_listening = is_always_listening
        self.default_language = language

    def listen(self, message):
        tokens = message.text.split()
        self.message = message
        self.arguments = self.get_arguments()
        self.data = shelve.open('data/chat_' + str(self.message.chat_id))
        self.collect_user_data(message)
        if message.text.startswith('/') and tokens[0][1:] == self.name:
            if len(tokens) > 1 and tokens[1] == 'help':
                return 'help'
            elif len(tokens) == 1 and self.accepts_none_argument is False:
                return 'ask for input'
            return True
        elif ('@' in message.text and self.message.split('@')[0][1:] ==
                self.name):
            return True
        elif self.is_active() or self.is_always_listening:
            return True
        return False

    def is_active(self):
        try:
            if self.data[self.name + '_active']:
                return True
        except:
            self.data[self.name + '_active'] = False
        return False

    def activate(self, boolean=True):
        if boolean is False:
            self.data[self.name + '_active'] = False
        else:
            self.data[self.name + '_active'] = True

    def collect_user_data(self, message):
        try:
            if str(message.sender_id) not in self.data['chat_users']:
                temp_dict = self.data['chat_users']
                temp_dict[str(message.sender_id)] = message.sender
                self.data['chat_users'] = temp_dict
        except:
            self.data['chat_users'] = {}

    def get_arguments(self):
        if len(self.message.text.split(' ')) > 1:
            return self.message.text.split(' ', 1)[1]

    def get_image(self, image_link):
        return StringIO.StringIO(urllib.urlopen(image_link).read()).getvalue()
