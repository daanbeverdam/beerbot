from pybot.pybot import PyBot
import config
import dialogs

if __name__ == "__main__":
    bot = PyBot(config.BOT_NAME, config.TOKEN, dialogs.bot[config.LANG],
                config.COMMAND_LIST)
    bot.run()
