import re
import urllib
from pybot.command import Command


class BBQCommand(Command):

    def reply(self):
        if self.arguments == 'help':
            return {'message': self.usage}
        else:
            url = "http://www.barbecueweer.nl"
            grade = (re.search(r'<div class="cijfer[\'"]?([^\'" >]+)',
                     urllib.urlopen(url).read()).group(1))
            reply = self.dialogs['reply'] % grade
            return {'message': reply}
