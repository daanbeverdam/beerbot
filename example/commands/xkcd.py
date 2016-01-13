from pybot.command import Command
import json
import urllib
import random


class XKCDCommand(Command):

    def reply(self):
        url = 'http://xkcd.com/info.0.json'
        content = json.loads(urllib.urlopen(url).read())
        newest_comic = content['num']
        if self.new_comic_exists(newest_comic):
            n = str(random.choice(range(1, newest_comic)))
            url = 'http://dynamic.xkcd.com/api-0/jsonp/comic/' + n
            content = json.loads(urllib.urlopen(url).read())
            image_link = content['img']
            title = 'Random xkcd: "%s"' % content['title']
        else:
            image_link = content['img']
            title = 'Newest xkcd: "%s"' % content['title']
        xkcd_image = self.get_image(image_link)
        return {'photo': xkcd_image, 'caption': title}

    def new_comic_exists(self, newest_comic):
        try:
            if newest_comic == self.data['newest_xkcd']:
                self.data['newest_xkcd'] = newest_comic
                return False
            return True
        except:
            self.data['newest_xkcd'] = 0
