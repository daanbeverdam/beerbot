# PyBot

### What is it?
A Python framework for Telegram Bots.

### How do I use it?
In order to use the provided example, please follow the steps below.

#### Obtain API token from BotFather
The first step in running your own bot is getting an API token from Telegram. You do this by starting a Telegram conversation with @BotFather and sending it the '/newbot' command. Then just follow the directions you are given.

#### Installing (Mac OS & Linux)
Some of the commands below need to be run with root privileges. Usually, putting `sudo` in front of the commands should do the trick.

Clone the git into a directory of choice:
```
git clone https://github.com/daanbeverdam/pybot.git
```
Then, open 'config.py' located in the example folder and find the line with `TOKEN =`. Now paste your previously obtained API token, replacing what is already there. It should look something like this:
```python
TOKEN = '123456789:ABCDEFGHIJKLMN_OPQRSTUVWXYZ'
```
You should also fill in the `BOT_NAME` and the `LANG`uage it speaks. Currently supported are English and Dutch. Next, install the framework:
```
python pybot/setup.py install
```
And last, run the following command to start the bot:
```
python pybot/example/main.py
```
If everything is done right, your bot should now be up and running. Test it by starting a conversation and sending it '/status'.

#### Installing (Windows)
PyBot has not been tested on Windows yet.
