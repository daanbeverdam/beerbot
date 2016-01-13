class Message(object):

    def __init__(self, message):
        self.id = message.get('message_id')
        self.date = message.get('date')
        self.text = message.get('text')
        self.sender = message.get('from')
        self.first_name_sender = self.sender['first_name']
        self.sender_id = self.sender['id']
        self.chat = message['chat']
        self.chat_id = self.chat['id']
        self.contains_command = self.check_for_command()
        try:
            self.reply_to_message = message.get('reply_to_message')
            self.reply_to_sender = self.reply_to_message['from']
            self.reply_to_sender_id = self.reply_to_sender['id']
            self.reply_to_sender_first_name = (self.reply_to_sender
                                               ['first_name'])
        except:
            self.reply_to_message = False

    def check_for_command(self):
        if (self.text is not None and self.text.startswith('/') and
                len(self.text) > 1):
            return True
        return False
