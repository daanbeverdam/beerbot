from pybot.command import Command
import json
import urllib


class WeatherCommand(Command):

    def reply(self):
        query = self.arguments
        url = ('http://api.openweathermap.org/data/2.5/weather?q=' + query +
               '&units=metric&lang=' + self.dialogs['lang'] + '&appid=' +
               self.api_key)
        results = json.loads(urllib.urlopen(url).read())
        try:
            place = str(results['name'])
            temp = str(results['main']['temp'])
            description = str(results['weather'][0]['description'])
            reply = self.dialogs['reply'] % (temp, place, description)
        except:
            reply = self.dialogs['error'] % query
        return {'message': reply}
