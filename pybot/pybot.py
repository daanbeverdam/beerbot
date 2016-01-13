from message import Message
from multipart import post_multipart
import time
import json
import urllib
import urllib2
import shelve
import traceback
import os
from datetime import datetime


class PyBot(object):

    def __init__(self, name, token, dialogs, commands):
        self.name = name
        self.token = token
        self.base_url = 'https://api.telegram.org/bot' + self.token + '/'
        self.dialogs = dialogs
        self.commands = commands
        self.reserved_names = ['cancel', 'results', 'done']
        self.command_names = ([command.name for command in self.commands] +
                              self.reserved_names)
        self.is_waiting_for_input = False

    def check_dirs(self):
        if not os.path.exists('data'):
            os.makedirs('data')
            print "Data folder created"

    def run(self):
        self.check_dirs()
        print "Bot started"
        while True:
            try:
                self.check_for_updates()
                self.check_for_scheduled_events()
            except KeyboardInterrupt:
                print " Bot stopped"
                break
            except:
                self.log(error=traceback.format_exc())

    def check_for_updates(self):
        self.main_data = shelve.open('main_data')
        try:
            offset = self.main_data['offset']
        except:
            offset = 0
        response = urllib2.urlopen(self.base_url + 'getUpdates',
                                   urllib.urlencode({
                                    'timeout': 30,
                                    'limit': 100,
                                    'offset': offset,
                                    })).read()
        body = json.loads(response)
        if body['ok'] and body['result'] != []:
            self.main_data['offset'] = body['result'][-1]['update_id'] + 1
            self.main_data.close()
            for result in body['result']:
                message = Message(result['message'])
                self.handle_message(message)
                self.handle_command(message)
                self.log(json_entry=result)
        elif body['ok'] == False:
            self.log('Invalid response!')

    def check_for_scheduled_events(self):
        scheduled_events = shelve.open('scheduled_events')
        current = datetime.now()
        for chat_id in scheduled_events:
            if scheduled_events[chat_id]:
                for event in list(scheduled_events[chat_id]):
                    print event
                    if ((current.year, current.month, current.day) == event['date']
                            and (current.hour, current.minute) == event['time']):
                        self.reply(chat_id, event['text'])
                        scheduled_events[chat_id] = scheduled_events[chat_id].remove(event)
        scheduled_events.close()

    def handle_message(self, message):
        self.log(message.first_name_sender + ' sent "' + message.text +
                 '" in chat ' + str(message.chat_id) + '.')

    def handle_command(self, message):
        if self.is_waiting_for_input and (self.is_waiting_for_input['from'] ==
                                          message.sender_id):
            if message.text == '/cancel':
                self.reply(message.chat_id, self.dialogs['operation_canceled'])
            else:
                self.is_waiting_for_input['command'].arguments = message.text
                self.handle_reply(self.is_waiting_for_input['command'],
                                  message)
            self.is_waiting_for_input = False
        else:
            for command in self.commands:
                if command.listen(message) == 'help':
                    reply = self.reply(message.chat_id, command.usage)
                elif command.listen(message) == 'ask for input':
                    self.is_waiting_for_input = {'command': command,
                                                 'from': message.sender_id}
                    self.reply(message.chat_id,
                               self.dialogs['input'] % command.name)
                elif command.listen(message):
                    self.handle_reply(command, message)
            if (message.contains_command and message.text.split()[0][1:]
                    not in self.command_names):
                self.reply(message.chat_id, self.dialogs['no_such_command'])

    def handle_reply(self, command, message):
        try:
            reply = command.reply()
            if 'keyboard' in reply:
                self.reply_markup(message.chat_id, **reply)
            else:
                self.reply(message.chat_id, **reply)
        except:
            self.log(error=traceback.format_exc())
            self.reply(message.chat_id,
                       self.dialogs['command_failed'] % command.name)

    def log(self, entry=None, json_entry=None, error=None):
        if entry:
            print entry.encode('utf-8').replace('\n', ' ')
            with open('readable.log', 'a') as log:
                log.write(entry.encode('utf-8').replace('\n', ' ') + '\n')
        elif json_entry:
            with open('json.log', 'a') as log:
                log.write(json.dumps(json_entry))
                log.write(',\n')
        elif error:
            print error
            with open('error.log', 'a') as log:
                log.write(str(error))
                log.write('\n')

    def reply(self, chat_id, message=None, photo=None, document=None, gif=None,
              location=None, preview_disabled=True, caption=None):
        if message:
            response = urllib2.urlopen(self.base_url + 'sendMessage',
                                       urllib.urlencode({
                                        'chat_id': str(chat_id),
                                        'text': message.encode('utf-8'),
                                        'disable_web_page_preview':
                                        str(preview_disabled)
                                        })).read()
            self.log('Bot sent reply "' + message + '" to ' +
                     str(chat_id) + '.')
        elif photo:
            self.send_action(chat_id, 'upload_photo')
            parameters = [('chat_id', str(chat_id))]
            if caption:
                parameters.append(('caption', caption.encode('utf-8')))
            response = post_multipart(self.base_url + 'sendPhoto', parameters,
                                      [('photo', 'photo.jpg', photo)])
            self.log('Bot sent photo to ' + str(chat_id) + '.')
        elif gif or document:
            file_name = 'image.gif' if gif else 'document.file'
            self.send_action(chat_id, 'upload_document')
            response = post_multipart(self.base_url + 'sendDocument',
                                      [('chat_id', str(chat_id))],
                                      [('document', (file_name),
                                       (gif if gif else document))])
            self.log('Bot sent document to ' + str(chat_id) + '.')
        elif location:
            response = urllib2.urlopen(self.base_url + 'sendLocation',
                                       urllib.urlencode({
                                        'chat_id': str(chat_id),
                                        'latitude': location[0],
                                        'longitude': location[1]
                                        })).read()
            self.log('Bot sent location to ' + str(chat_id) + '.')

    def reply_markup(self, chat_id, message, keyboard=None, selective=False,
                     force_reply=False, message_id=None, resize=True,
                     one_time=True, disable_preview=True):
        if keyboard:
            reply_markup = ({
                'keyboard': keyboard,
                'resize_keyboard': resize,
                'one_time_keyboard': one_time,
                'selective': selective
            })
        else:
            reply_markup = ({
                'hide_keyboard': True,
                'selective': selective
            })
        reply_markup = json.dumps(reply_markup)
        params = urllib.urlencode({
              'chat_id': str(chat_id),
              'text': message.encode('utf-8'),
              'reply_markup': reply_markup,
              'force_reply': force_reply,
              'disable_web_page_preview': disable_preview,
              'reply_to_message_id': str(message_id)
        })
        response = urllib2.urlopen(self.base_url + 'sendMessage',
                                   params).read()
        self.log('Bot sent markup: ' + '"' + message + '" ' + str(keyboard) +
                 ' to ' + str(chat_id) + '.')

    def send_action(self, chat_id, action):
        act = urllib2.urlopen(self.base_url + 'sendChatAction',
                              urllib.urlencode({
                               'chat_id': str(chat_id),
                               'action': str(action)
                               })).read()
        self.log('Bot sent action "' + action + '" to ' + str(chat_id) + '.')
