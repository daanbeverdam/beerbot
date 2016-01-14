from commands.start import StartCommand
from commands.help import HelpCommand
from commands.findbeer import FindBeerCommand
import dialogs
# Environment variables can be entered in the .env file
# Alternatively, you could just enter the values (as string) in this file below.
with open('.env') as f:
    env = f.read().splitlines()
TOKEN = env[0] # Telegram API authorization token
BOT_NAME = env[1] # name of the bot
LANG = env[2] # 'en' for English, 'nl' for Dutch (not fully supported yet)
ADMIN_CHAT_ID = env[3] # admin chat id for Telegram (optional, won't restrict functionality)
DATABASE = env[4] # database name
USER = env[5] # username for database
PASSWORD = env[6] # password for database
# Commands can be removed or added:
COMMAND_LIST = [
                StartCommand('start', dialogs.start[LANG]),
                HelpCommand('help', dialogs.help[LANG]),
                FindBeerCommand('findbeer', dialogs.findbeer[LANG])
               ]