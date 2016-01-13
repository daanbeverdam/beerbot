from pybot.command import Command
import urllib
import json


class ImageCommand(Command):

    def reply(self):
        query = self.arguments
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
               'v=1.0&q=' + query)
        print url
        response = urllib.urlopen(url)
        results = json.loads(response.read())
        print results
        if len(results['responseData']['results']) == 0:
            return {'message': self.dialogs['no_results'] % query}
        more_results_link = results['responseData']['cursor']['moreResultsUrl']
        first_result = results['responseData']['results'][0]
        image_link = first_result['unescapedUrl']
        print image_link
        image = self.get_image(image_link)
        caption = '"%s"' % first_result['contentNoFormatting']
        # caption += self.dialogs['more'] + more_results_link
        return {'photo': image, 'caption': caption}
