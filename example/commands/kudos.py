from pybot.command import Command
import operator


class KudosCommand(Command):

    def reply(self):
        if self.message.text.split()[0][1:] == self.name:
            if self.arguments is None:
                return self.kudos_overview()
            elif self.arguments.title() in [i['first_name'] for i in
                                            self.data['chat_users'].values()]:
                return self.give_kudos(self.arguments)
            return {'message': self.dialogs['not_in_chat'] % self.arguments}
        elif self.message.text[:2] == '+1':
            return self.give_kudos()
        elif self.message.text[:2] == '-1':
            return self.give_kudos(substract=True)
        else:
            return {'message': None}

    def kudos_overview(self):
        try:
            kudo_dict = sorted(self.data['kudo_dict'].items(),
                               key=operator.itemgetter(1), reverse=True)
        except:
            return{'message': self.dialogs['no_kudos']}
        reply = self.dialogs['kudo_overview']
        for entry in kudo_dict:
            reply += "\n%s: %i" % (entry[0], entry[1])
        return {'message': reply}

    def give_kudos(self, name=None, substract=False):
        if substract is True:
            number_of_kudos = -1
        else:
            number_of_kudos = 1
        try:
            kudo_dict = self.data['kudo_dict']
        except:
            self.data['kudo_dict'] = {}
            kudo_dict = self.data['kudo_dict']
        if name is None:
            try:
                name = self.message.reply_to_sender_first_name
            except:
                return {'message': None}
        name = name.title()
        if self.message.first_name_sender == name:
            return {'message': self.dialogs['shame_on_you']}
        try:
            current_kudos = kudo_dict[name]
            new_kudos = current_kudos + number_of_kudos
            kudo_dict[name] = new_kudos
        except:
            kudo_dict[name] = number_of_kudos
        self.data['kudo_dict'] = kudo_dict
        return {'message': self.dialogs['kudos_given'] %
                (number_of_kudos, name, self.data['kudo_dict'][name])}
