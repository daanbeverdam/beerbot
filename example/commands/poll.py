from pybot.command import Command
import shelve


class PollCommand(Command):

    def reply(self):
        if not self.is_active():
            return self.new_poll()
        elif self.message.text in self.data['poll_options_dict']:
            return self.store_answer()
        elif self.message.text in self.meta_commands:
            return self.handle_meta()
        elif self.message.text.split(' ', 1)[0][1:] == self.name:
            return {'message': self.dialogs['poll_already_active']}
        return {'message': None}

    def new_poll(self):
        if self.arguments[:2] in ['~m', '~M']:
            self.data['poll_multi'] = True
            self.arguments = self.arguments[2:]
            one_time = False
        else:
            self.data['poll_multi'] = False
            one_time = True
        tokens = self.arguments.split('*')
        question = tokens[0].strip()
        self.data['poll_question'] = question
        options = []
        options_dict = {}
        for option in tokens[1:]:
            options.append(option.strip())
            options_dict[option.strip()] = []
        formatted_options = self.format(question, options)
        self.data['poll_options_dict'] = options_dict
        self.data['poll_participators'] = []
        self.data['poll_starter'] = self.message.sender_id
        self.data['poll_starter_name'] = self.message.first_name_sender
        if question != '':
            self.data['poll_active'] = True
            reply = question + '\n- ' + '\n- '.join(options)
        return {'message': reply, 'keyboard': formatted_options,
                'force_reply': True, 'one_time': one_time}

    def format(self, question, options):
        formatted_options = [['"%s"' % question]]
        temp_options = []
        counter = 1
        for option in options:
            temp_options.append(option.strip())
            if counter % 2 == 0:
                formatted_options.append(temp_options)
                temp_options = []
            counter += 1
        if self.data['poll_multi'] is True:
            temp_options.append('/done')
        if len(temp_options) == 1:
            formatted_options.append(temp_options + [' '])
        elif len(temp_options) == 2:
            formatted_options.append(temp_options)
        return formatted_options

    def store_answer(self):
        participators = self.data['poll_participators']
        if (self.message.sender_id not in participators or
                self.data['poll_multi'] is True and
                self.message.first_name_sender not in self.data
                ['poll_options_dict'][self.message.text]):
            participators.append(self.message.sender_id)
            self.data['poll_participators'] = participators
            option_dict = self.data['poll_options_dict']
            option_dict[self.message.text].append(self.message.
                                                  first_name_sender)
            self.data['poll_options_dict'] = option_dict
            reply = {'message': self.dialogs['store_answer'], 'keyboard': None,
                     'selective': True, 'message_id': self.message.id}
            if self.data['poll_multi'] is True:
                reply = {'message': self.dialogs['store_answer']}
            if (len(participators) == len(self.data['chat_users']) and
                    self.data['poll_multi'] is False):
                reply = {'message': self.dialogs['everybody_voted'] %
                         self.poll_results(), 'keyboard': None}
                self.activate(False)
            return reply
        return {'message': None}

    def handle_meta(self):
        if self.message.text == '/results':
            return {'message': self.poll_results()}
        elif self.message.text == '/done':
            return {'message': self.dialogs['done_voting'], 'keyboard': None,
                    'selective': True, 'message_id': self.message.id}
        return self.end_poll()

    def poll_results(self):
        reply = self.dialogs['results'] % self.data['poll_question']
        for option, voters in self.data['poll_options_dict'].iteritems():
            reply += ('\n- ' + option + ': ' + ', '.join(voters) +
                      ' (%d %s)' % (len(voters), self.dialogs[(
                                    'vote' if len(voters) == 1 else 'votes')]))
        return reply

    def end_poll(self):
        if (self.message.sender_id == self.data['poll_starter'] or
                self.message.sender_id == self.admin):
            self.data['poll_active'] = False
            return {'message': self.dialogs['end_poll'], 'keyboard': None}
        return {'message': self.dialogs['not_owner'] %
                self.data['poll_starter_name']}
