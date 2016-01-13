from commands.putin import PutinCommand
from commands.bbq import BBQCommand
from commands.dice import DiceCommand
from commands.doge import DogeCommand
from commands.gif import GifCommand
from commands.echo import EchoCommand
from commands.wiki import WikiCommand
from commands.youtube import YouTubeCommand
from commands.google import GoogleCommand
from commands.poll import PollCommand
from commands.help import HelpCommand
from commands.status import StatusCommand
from commands.weather import WeatherCommand
from commands.quote import QuoteCommand
from commands.stats import StatsCommand
from commands.calculator import CalculatorCommand
from commands.hangman import HangmanCommand
from commands.xkcd import XKCDCommand
from commands.users import UsersCommand
from commands.marnie import MarnieCommand
from commands.image import ImageCommand
from commands.start import StartCommand
from commands.kudos import KudosCommand
from commands.changes import ChangesCommand
from commands.reminder import ReminderCommand
import dialogs

# create a prefs.txt file with your api token or alternatively,
# enter your authorization token here directly:
TOKEN = open('example/prefs.txt', 'r').readlines()[0].strip()
# enter name of the bot here:
BOT_NAME = open('example/prefs.txt', 'r').readlines()[1].strip()
# 'en' for english, 'nl' for dutch:
LANG = open('example/prefs.txt', 'r').readlines()[2].strip()
# chat id of the admin (optional):
ADMIN_CHAT_ID = open('example/prefs.txt', 'r').readlines()[3].strip()
# api key for weather:
WEATHER_API = open('example/prefs.txt', 'r').readlines()[4].strip()
# commands can be removed or added:
COMMAND_LIST = [
                BBQCommand('bbq', dialogs.bbq[LANG]),
                CalculatorCommand('calculator', dialogs.calculator[LANG]),
                ChangesCommand('changes', dialogs.changes[LANG]),
                DiceCommand('dice', dialogs.dice[LANG]),
                DogeCommand('doge', dialogs.doge[LANG], False),
                EchoCommand('echo', dialogs.echo[LANG], False),
                GifCommand('gif', dialogs.gif[LANG], False),
                GoogleCommand('google', dialogs.google[LANG], False),
                HangmanCommand('hangman', dialogs.hangman[LANG]),
                HelpCommand('help', dialogs.help[LANG]),
                ImageCommand('image', dialogs.image[LANG], False),
                KudosCommand('kudos', dialogs.kudos[LANG],
                             is_always_listening=True),
                MarnieCommand('marnie', dialogs.marnie[LANG]),
                PollCommand('poll', dialogs.poll[LANG], False, ADMIN_CHAT_ID),
                PutinCommand('putin', dialogs.putin[LANG]),
                QuoteCommand('quote', dialogs.quote[LANG]),
                ReminderCommand('reminder', dialogs.reminder[LANG]),
                StartCommand('start', dialogs.start[LANG]),
                StatsCommand('stats', dialogs.stats[LANG]),
                StatusCommand('status', dialogs.status[LANG]),
                UsersCommand('users', dialogs.users[LANG]),
                WikiCommand('wiki', dialogs.wiki[LANG], False),
                WeatherCommand('weather', dialogs.weather[LANG], False,
                               api_key=WEATHER_API),
                XKCDCommand('xkcd', dialogs.xkcd[LANG]),
                YouTubeCommand('youtube', dialogs.youtube[LANG], False)
               ]
