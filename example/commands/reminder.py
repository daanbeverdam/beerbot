from pybot.command import Command
from datetime import datetime
from datetime import timedelta
import shelve


class ReminderCommand(Command):

    def reply(self):
        tokens = self.arguments.split()
        reminder = self.analyze(tokens)
        scheduled_events = shelve.open('scheduled_events')
        self.message.chat_id = str(self.message.chat_id)
        try:
            l = scheduled_events[self.message.chat_id]
            l.append(reminder)
            scheduled_events[self.message.chat_id] = l
        except:
            scheduled_events[self.message.chat_id] = [reminder]
        scheduled_events.close()
        return {'message': self.dialogs['reminder_saved'] % (reminder['text'], str(reminder['date']) + ' ' + str(reminder['time']))}

    def analyze(self, tokens):
        reminder = {}
        date = None
        time = None
        tokens_copy = tokens
        current = datetime.now()
        for token in tokens:
            if '-' in token:
                print 'date stored'
                date = token.split('-')
                day = int(date[0])
                month = int(date[1])
                if len(date) > 2:
                    year = int(date[2])
                else:
                    year = current.year
                reminder['date'] = (year, month, day)
            elif ':' in token:
                print 'time stored'
                time = token.split(':')
                hour = int(time[0])
                minute = int(time[1])
                reminder['time'] = (hour, minute)
            elif 'tomorrow' in token or 'morgen' in token:
                delta = timedelta(days=1)
                new = current + delta
                reminder['date'] = (new.year, new.month, new.day)
            if date and time:
                tokens.remove(':'.join(time))
                tokens.remove('-'.join(date))
                break
        if date and not time:
            reminder['time'] = (8, 0)
            tokens.remove('-'.join(date))
        if time and not date:
            if current >= datetime(current.year, current.month, current.day, reminder['time'][0], reminder['time'][1]):
                delta = timedelta(days=1)
                new = current + delta
                reminder['date'] = (new.year, new.month, new.day)
            else:
                reminder['date'] = (current.year, current.month, current.day)
            tokens.remove(':'.join(time))
        reminder['text'] = ' '.join(tokens)
        if reminder['text'] != '':
            return reminder
