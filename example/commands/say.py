from pybot.command import Command
import urllib2
import urllib
import StringIO

class SayCommand(Command):

    def reply(self):
        language = self.determine_language()
        text = urllib.quote_plus(self.arguments)
        url = ('http://api.voicerss.org/?key=' + self.api_key + '&src=' +
               text + '&hl=' + language + '&f=48khz_16bit_stereo')
        audio = StringIO.StringIO(urllib.urlopen(url).read()).getvalue()
        return {'document': audio, 'extension': '.mp3', 'file_name': text}

    def determine_language(self):
        if self.arguments[:3] == '~en':
            self.arguments = ' '.join(self.arguments.split()[1:])
            language = 'en-us'
        elif self.arguments[:3] == '~nl':
            self.arguments = ' '.join(self.arguments.split()[1:])
            language = 'nl-nl'
        else:
            language = self.default_language
            if language == 'nl':
                language = 'nl-nl'
            elif language == 'en':
                language = 'en-us'
        return language