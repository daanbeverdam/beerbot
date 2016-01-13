from pybot.command import Command
from xml.dom.minidom import parse
import urllib


class ChangesCommand(Command):

    def reply(self):
        feed = 'https://github.com/daanbeverdam/pybot/commits/master.atom'
        xml = parse(urllib.urlopen(feed))
        reply = self.dialogs['reply']
        for node in xml.getElementsByTagName('title')[1:6]:
            reply += '\n- ' + node.firstChild.nodeValue.strip()
        # reply += '\n' + self.dialogs['more']
        return {'message': reply}
