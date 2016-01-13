from pybot.command import Command
import re
import json
import collections


class StatsCommand(Command):

    def reply(self):
        log = '[%s]' % str(open('json.log', 'r').read())[:-2]
        log = json.loads(log)
        try:
            reply = self.scan_entries(log)
            return {'message': reply}
        except:
            return {'message': self.dialogs['error']}

    def scan_entries(self, log):
        relevant_entries = []
        for entry in log:
            chat_id = entry['message']['chat']['id']
            if chat_id == self.message.chat_id:
                relevant_entries.append(entry['message'])
        return self.calculate_statistics(relevant_entries)

    def calculate_statistics(self, entries):
        stat_dict = {}
        all_words = ''
        all_commands = ''
        for message in entries:
            text = message.get('text')
            if text is not None:
                if not text.startswith('/'):
                    all_words += ' ' + text.lower()
                elif text.startswith('/'):
                    all_commands += ' ' + text.split(' ')[0]
            first_name_sender = message['from']['first_name']
            stat_dict.setdefault(first_name_sender, []).append(text)
        total_words = len(all_words.split(' '))
        words = collections.Counter(re.findall(r'\w+', all_words))
        commands = collections.Counter(re.findall(r'/\w+', all_commands))
        most_active_users = []
        for user in stat_dict.keys():
            most_active_users.append((user, stat_dict[user]))
        most_active_users.sort(key=lambda tup: len(tup[1]), reverse=True)
        total_messages = len(entries)
        most_used_commands = commands.most_common(3)
        most_used_words = words.most_common(3)
        return self.format_statistics(total_messages, total_words,
                                      most_used_commands, most_active_users)

    def format_statistics(self, total_messages, total_words,
                          most_used_commands, most_active_users):
        temp_string = ""
        counter = 1
        for entry in most_active_users:
            temp_string += "%i. %s (%i)\n" % (counter, entry[0], len(entry[1]))
            counter += 1
        most_active_users = temp_string
        return self.dialogs['reply'] % (total_messages, total_words,
                                        most_used_commands[0][0],
                                        most_used_commands[0][1],
                                        most_used_commands[1][0],
                                        most_used_commands[1][1],
                                        most_used_commands[2][0],
                                        most_used_commands[2][1],
                                        most_active_users)
