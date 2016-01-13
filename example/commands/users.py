from pybot.command import Command


class UsersCommand(Command):

    def reply(self):
        reply = self.dialogs['reply']
        dictionary = self.data['chat_users']
        for user in dictionary:
            try:
                reply += "%s %s (%s)\n" % (dictionary[user]['first_name'],
                                           dictionary[user]['last_name'],
                                           dictionary[user]['id'])
            except:
                reply += "%s (%s)\n" % (dictionary[user]['first_name'],
                                        dictionary[user]['id'])
        return {'message': reply}
