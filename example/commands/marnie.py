import urllib
import json
import random
import re
from HTMLParser import HTMLParser
from pybot.command import Command


class MarnieCommand(Command):

    def reply(self):
        url = ('http://api.tumblr.com/v2/blog/marniethedog.tumblr.com/'
               'posts/photo?&limit=50')
        resp = urllib.urlopen(url).read()
        content = json.loads(resp)
        post_list = content['response']['posts']
        random_post = random.choice(post_list)
        image_url = random_post['photos'][0]['alt_sizes'][0]['url']
        h = HTMLParser()
        caption = h.unescape(random_post['caption'])
        caption = re.sub('<[^<]+?>', '', caption)
        marnie = self.get_image(image_url)
        return {'photo': marnie, 'caption': caption}
