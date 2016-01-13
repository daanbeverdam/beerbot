from commands.start import StartCommand
from commands.help import HelpCommand
from commands.findbeer import FindBeerCommand
import dialogs
# environment variables can be found in the .env file
with open('.env') as f:
    env = f.read().splitlines()
# authorization token:
TOKEN = env[0]
# enter name of the bot here:
BOT_NAME = env[1]
# 'en' for english, 'nl' for dutch:
LANG = env[2]
# chat id of the admin (optional):
ADMIN_CHAT_ID = env[3]
# commands can be removed or added:
COMMAND_LIST = [
                StartCommand('start', dialogs.start[LANG]),
                HelpCommand('help', dialogs.help[LANG]),
                FindBeerCommand('findbeer', dialogs.findbeer[LANG])
               ]