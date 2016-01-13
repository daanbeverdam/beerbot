import StringIO
import urllib
from pybot.command import Command


class DogeCommand(Command):

    def reply(self):
        if self.arguments == 'help':
            return {'message': self.usage}
        caption = self.arguments
        image_url = ('http://dogr.io/' + '/'.join(map(str, caption.split())) +
                     '.png?split=false')
        doge_image = (StringIO.StringIO(urllib.urlopen(image_url)
                      .read()).getvalue())
        return {'photo': doge_image}
