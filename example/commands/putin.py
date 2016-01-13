import urllib, urllib2
import json
import StringIO
import random
from pybot.command import Command


class PutinCommand(Command):

    def reply(self):
        if self.arguments == 'help':
            return {'message': self.usage}
        url = "http://api.tumblr.com/v2/blog/vladimirputindoingthings.tumblr.com/posts/text?&limit=50"
        resp = urllib2.urlopen(url).read()
        content = json.loads(resp)
        post_list = content['response'].get("posts")
        random_post_body = random.choice(post_list).get('body')
        photo_url = random_post_body.split('src=')[1].split('/>')[0].strip('"')
        photo = StringIO.StringIO(urllib.urlopen(photo_url).read()).getvalue()
        return {'photo': photo}
