# This Python file uses the following encoding: utf-8

bot = {'en': {
    'command_failed': "Sorry, something went wrong. "
    "Need help? Type: '/%s help'.",
    'no_such_command': "Sorry, I'm not familiar with that command.",
    'input': "Please type your input for the /%s command:",
    'operation_canceled': "Operation canceled."
},
    'nl': {
    'command_failed': "Sorry, er ging iets mis. "
    "Hulp nodig? Type: '/%s help'",
    'no_such_command': "Sorry, dat commando ken ik niet.",
    'input': "Type alsjeblieft je invoer voor het commando /%s:",
    'operation_canceled': "Geannuleerd."
}
}

help = {'en': {
    'usage': "Help-ception! Please try /help for a list of "
    "commands.",
    'reply': "Here is a list of all available commands:"
},
    'nl': {
    'usage': "Help-ception! Probeer /help voor een lijst met alle "
    "beschikbare commando's.",
    'reply': "Hier is een lijst met alle beschikbare commando's:"
}
}

deleteme = {'en': {
    'usage': "Delete all your records in the database.",
    'reply': "All your records are deleted! Who are you again?"
}
}

findbeer = {'en': {
    'usage': "Find the best beer to go with your meal.",
    'specify': "Please choose your mealtype from the list below, or type "
    "in a more specific meal.",
    'no_such_meal': "Sorry, I can't find '%s' in the database. "
    "Please try another meal or select the mealtype below that corresponds "
    "the most to your meal."
}}

start = {'en': {
    'usage': "The /start command initializes the bot.",
    'new_user': "Hi there, welcome! I don't know you yet. Please "
    "help me get to know you by telling me your preferences, okay?",
    'color': "Do you prefer dark beers or light beers?",
    'bitterness': "On a scale from 1-5, how bitter do you like your beers?",
    'sweetness': "On a scale from 1-5, how sweet do you like your beers?",
    'alcohol': "How strong do you like your beers?",
    'user_registered': "Thanks, I'm all set! Use /findbeer to get beer "
    "reccomendations or use /deleteme to remove yourself from the database.",
    'whoops!': "Whoops! You did something wrong, please tap /start again.",
    'reply': "Your preferences are stored. Let me find some beers for you! "
    "Tap /findbeer to begin."
}}