import re
import urllib
from pybot.command import Command


class YouTubeCommand(Command):

    def reply(self):
        if self.arguments == 'help':
            return {'message': self.usage}
        query = self.arguments
        if query is not None:
            query_encoded = urllib.urlencode({"search_query": query})
        html_content = urllib.urlopen("http://www.youtube.com/results?" +
                                      query_encoded)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                    html_content.read())
        if len(search_results) > 0:
            youtube_link = ("http://www.youtube.com/watch?v=" +
                            search_results[0])
            return {'message': "Hier is de eerste hit voor '%s':\n" % query +
                    str(youtube_link), 'preview_disabled': False}
        return {'message': self.dialogs['no_results'] % query}
