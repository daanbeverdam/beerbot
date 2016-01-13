from pybot.command import Command
import re
import urllib


class HangmanCommand(Command):

    def reply(self):
        self.accepts_none = True
        if not self.is_active():
            return self.start()
        elif self.message.text in self.data['hangman_letters']:
            return self.check_letter()
        elif self.message.text in self.meta_commands:
            return self.handle_meta()
        return {'message': None}

    def start(self):
        word = self.get_word()
        while word.isalpha() == False or len(word) > 10:
            word = self.get_word()
        self.data['hangman_word'] = word.upper()
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.data['hangman_letters'] = alphabet
        minus = u'\u2796'
        self.data['displayed_word'] = minus * len(self.data['hangman_word'])
        heart = u'\u2661'
        self.data['hangman_lives'] = heart * 6
        keyboard = self.format_keyboard(alphabet, 3)
        self.activate(True)
        reply = u'Start: %s\n%s' % (self.data['displayed_word'],
                                    self.data['hangman_lives'])
        return {'message': reply, 'keyboard': keyboard}

    def get_word(self):
        url = 'http://www.tulpweb.nl/willekeurigwoord/'
        response = urllib.urlopen(url).read()
        search = re.search(r'willekeurige woord is:</p><h2>'
                           '[\'"]?([^\'" >]+)', urllib.urlopen(url).read())
        word = search.group(1)[:-4]
        return word

    def handle_meta(self):
        if self.message.text == '/cancel':
            self.activate(False)
            return {'message': self.dialogs['ended'], 'keyboard': None}
        return {'message': None}

    def format_keyboard(self, keyboard, rows):
        if len(keyboard) < 18:
            rows = 2
        q, r = divmod(len(keyboard), rows)
        indices = [q * i + min(i, r) for i in xrange(rows + 1)]
        return [keyboard[indices[i]:indices[i + 1]] for i in xrange(rows)]

    def format_displayed_word(self):
        letter = self.message.text
        word = self.data['hangman_word']
        displayed_word = self.data['displayed_word']
        indexes = []
        for i in re.finditer(letter, word):
            indexes.append(i.start())
        for i in range(len(displayed_word)):
            if i in indexes:
                displayed_word = (displayed_word[:i] + letter +
                                  displayed_word[i + 1:])
        self.data['displayed_word'] = displayed_word

    def lose_life(self):
        lives = self.data['hangman_lives']
        self.data['hangman_lives'] = lives[1:]

    def check_letter(self):
        letters = self.data['hangman_letters']
        letters.remove(self.message.text)
        self.data['hangman_letters'] = letters
        keyboard = self.format_keyboard(self.data['hangman_letters'], 3)
        if self.message.text in self.data['hangman_word']:
            self.format_displayed_word()
            if self.data['hangman_word'] == self.data['displayed_word']:
                reply = self.dialogs['game_won'] % self.data['hangman_word']
                keyboard = None
                self.activate(False)
            else:
                reply = (self.dialogs['guessed_correct'] %
                         (self.data['displayed_word'],
                          self.data['hangman_lives']))
        else:
            self.lose_life()
            if self.game_over():
                reply = self.dialogs['game_over'] % self.data['hangman_word']
                keyboard = None
                self.activate(False)
            else:
                reply = (self.dialogs['guessed_incorrect'] % (self.data
                         ['displayed_word'], self.data['hangman_lives']))
        return {'message': reply, 'keyboard': keyboard}

    def game_over(self):
        if len(self.data['hangman_lives']) == 0:
            return True
        return False
