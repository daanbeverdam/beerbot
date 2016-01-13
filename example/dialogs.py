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

bbq = {'en': {
    'usage': "The command /bbq determines if the weather "
    "circumstances in the Netherlands are suitable for barbecuing.",
    'reply': "On a scale of 1-10, the barbecue weather in the "
    "Netherlands gets an %s."
},
    'nl': {
    'usage': "Het commando /bbq geeft het huidige "
    "barbecueweercijfer voor Nederland.",
    'reply': "Het barbecueweer krijgt vandaag een %s. Oant moarn!"
}
}

calculator = {'en': {
    'usage': "The /calulator command brings up a calculator.",
    'prompt': "Please type your query:",
    'error': "Sorry, your query is invalid."
},
    'nl': {
    'usage': "Het /calculator commando retourneert een rekenmachine.",
    'prompt': "Type je som:",
    'error': "Sorry, je som is ongeldig."
}
}

changes = {'en': {
    'usage': "The command /changes shows the most recent code changes of the "
    "PyBot project. Visit github.com/daanbeverdam/pybot to contribute.",
    'reply': "Most recent code changes to PyBot:",
    'more': "Visit https://github.com/daanbeverdam/pybot/commits/master for "
    "more."
},
    'nl': {
    'usage': "Het commando /changes laat de meest recente wijzigingen zien "
    "van het PyBot project. Ga naar github.com/daanbeverdam/pybot om bij te "
    "dragen.",
    'reply': "Meest recente wijzigingen:",
    'more': "Ga naar https://github.com/daanbeverdam/pybot/commits/master "
    " voor meer."
}
}

dice = {
    'en': {
        'usage': "Throw a die with /dice. Throw multiple dice by "
        "adding a number. For example: /dice 2.",
        'reply': "You threw: %s.",
        'reply_0': "Please throw at least 1 die.",
        'reply_max': "Sorry, the maximum number of dice you can throw "
        "is 10."},
    'nl': {
        'usage': "Gooi een dobbelsteen met /dice. Om meerdere "
        "dobbelstenen voeg je een getal toe. Bijvoorbeeld: "
        "'/dice 2'.",
        'reply': "Je gooide %s.",
        'reply_0': "Gooi ten minste 1 dobbelsteen, alsjeblieft.",
        'reply_max': "Sorry, het maximum aantal dobbelstenen dat je kan "
        "gooien is 10."}}

doge = {'en': {
    'usage': "Create your own doge image with '/doge "
    "[your caption]'. For example: '/doge wow such example'."
},
    'nl': {
    'usage': "Maak je eigen doge plaatje met '/doge [caption]'."
    "Bijvoorbeeld: '/doge wow such example'."
}
}

echo = {'en': {
    'usage': "The simplest command there is: '/echo [text]' returns "
    "your [text]."
},
    'nl': {
    'usage': "Het meest simpele commando dat er is: '/echo [tekst]' "
    "retourneert jouw [tekst]."
}
}

google = {'en': {
    'usage': "Search the internet with Google using '/google "
    "[query]'.",
    'reply_top': "Top %d hits for '%s':\n",
    'reply_bottom': "For more results: %s",
    'no_results': "Sorry, no results found for '%s'."
},
    'nl': {
    'usage': "Doorzoek het internet met Google: '/google "
    "[zoekterm]'.",
    'reply_top': "Top %d hits voor '%s':\n",
    'reply_bottom': "Voor meer resultaten: %s",
    'no_results': "Sorry, geen resultaten gevonden voor '%s'."
}
}

hangman = {'en': {
    'usage': "Play a game of /hangman!",
    'guessed_correct': "Correct guess!\n%s\n%s",
    'guessed_incorrect': "Incorrect guess!\n%s\n%s",
    'game_over': "Sorry, you lost.\nThe correct word is: %s\n "
    "Type /hangman for a new game.",
    'game_won': "You won, congratulations!\nThe word is: %s\n"
    "Type /hangman om opnieuw te spelen.",
    'ended': "The game has been canceled."
},
    'nl': {
    'usage': "Speel een potje galgje met /hangman.",
    'guessed_correct': "Goed geraden!\n%s\n%s",
    'guessed_incorrect': "Probeer een andere letter.\n%s\n%s",
    'game_over': "Sorry, je hebt verloren.\nHet woord was: %s\n"
    "Type /hangman om opnieuw te spelen.",
    'game_won': "Je hebt gewonnen!\nHet woord was: %s\n"
    "Type /hangman om opnieuw te spelen.",
    'ended': u"Spel beëndigd."
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

image = {'en': {
    'usage': "Search for images with '/image [query]'.",
    'more': "\nFor more results: ",
    'no_results': "Sorry, no results found for '%s'."
},
    'nl': {
    'usage': "Zoek naar afbeeldingen met '/image [zoekterm]'.",
    'more': "\nVoor meer resultaten: ",
    'no_results': "Sorry, geen resultaten gevonden voor '%s'."}
}

gif = {'en': {
    'usage': "Search for gifs using '/gif [search query]'. You can ask"
    " for a random gif using '/gif random [optional search query]'.",
    'no_results': "Sorry, no gifs found for query '%s'."
},
    'nl': {
    'usage': "Zoek naar gifs met '/gif [zoekterm]'. Je kunt ook een "
    "willekeurige gif opvragen met '/gif random [optionele zoekterm]'",
    'no_results': "Sorry, geen gifs gevonden voor '%s'.",
    'no_kudos': "Sorry, no kudos are given yet.",
    'shame_on_you': "You can't give kudos to yourself, shame on you!"
}
}

kudos = {'en': {
    'usage': "Give kudos to your friends by replying to their messages with "
    "'+1' or '/kudos [first name]'. Ask for the overview with /kudos.",
    'kudos_given': "%i Kudo for %s. Total kudos: %i.",
    'kudo_overview': "Kudo overview:",
    'not_in_chat': "Sorry, user '%s' is not in this chat."
},
    'nl': {
    'usage': "Geef kudo's aan je vrienden door hun berichten te beantwoorden "
    "met '+1' of '/kudos [voornaam]'. Vraag de resultaten op met /kudos.",
    'kudos_given': "%i Kudo voor %s. Totaal aantal kudo\'s: %i.",
    'kudo_overview': "Kudo overzicht:",
    'not_in_chat': "Sorry, '%s' is geen gebruiker in deze chat.",
    'no_kudos': "Sorry, er zijn nog geen kudo's gegeven.",
    'shame_on_you': "Je kan geen kudo's aan jezelf geven, foei!"
}
}

marnie = {'en': {
    'usage': "The /marnie command returns a random picture of Marnie the dog."
},
    'nl': {
    'usage': "Het /marnie commando retourneert een willekeurige foto van "
    "'Marnie the dog'."
}
}

poll = {
    'en': {
        'usage': "Start a poll! Use the following format: '/poll "
        "[question] *[option 1] *[option 2] *[etc]'. Add '~m' to allow voting "
        "on multiple options. You can always "
        "/cancel a poll or ask for the /results.",
        'store_answer': "Thanks, your answer has been recorded.",
        'results': "The results for '%s':",
        'end_poll': "The poll has ended.",
        'not_owner': "Sorry, you are not the owner of the current poll. "
        "Only %s can /cancel it.",
        'poll_already_active': "Sorry, another poll is already active. "
        "The owner must /cancel the current one first.",
        'votes': "votes",
        'vote': "vote",
        'everybody_voted': "Everybody has voted! %s",
        'done_voting': "Thanks, I'll hide your keyboard now."},
    'nl': {
        'usage': "Start een poll! Gebruik het volgende formaat: "
        "'/poll [vraag] *[optie 1] *[optie 2] *[etc]'. Voeg '~m' toe wanneer "
        "er meerdere antwoorden mogelijk zijn. De resultaten "
        "kunnen opgevraagd worden met /results en de poll kan "
        "geannuleerd worden met /cancel.",
        'store_answer': "Dankjewel, je antwoord is opgeslagen.",
        'results': "De resultaten voor de vraag '%s':",
        'end_poll': u"De poll is beëindigd.",
        'not_owner': "Sorry, je bent niet de eigenaar van de actieve "
        "poll. Alleen %s kan de poll annuleren met /cancel.",
        'poll_already_active': "Sorry, er is al een andere poll actief. "
        "De eigenaar moet de huidige poll eerst annuleren met /cancel.",
        'votes': "stemmen",
        'vote': "stem",
        'everybody_voted': "Iedereen heeft gestemd! %s",
        'done_voting': "Bedankt, de antwoordopties worden nu verborgen."}}

putin = {'en': {
    'usage': "The command /putin returns a random photo of "
    "Vladimir Putin."
},
    'nl': {
    'usage': "Het /putin commando retourneert een willekeurige "
    "foto van Vladimir Putin."
}
}

quote = {'en': {
    'usage': "Save quotes by using '/quote [name]: [quote]'. "
    "You can also ask for a random quote using '/quote [optional "
    "name]'. Request all quotes by adding 'all'.",
    'quote_saved': "Quote saved."
},
    'nl': {
    'usage': "Sla je quotes op met behulp van '/quote [naam]: "
    "[quote]'. Een willekeurige quote is aan te vragen met '/quote "
    "[optionele naam]'. Vraag alle quotes op door 'all' toe te "
    "voegen.",
    'quote_saved': "Quote opgeslagen."
}
}

reminder = {'en': {
    'usage': "Save a reminder! Format: /reminder [dd-mm-yyyy] [hh:mm] "
    "[reminder text].",
    'reminder_saved': "Reminder %s saved! %s"
},
    'nl': {
    'usage': "Vergeetachtig? Maak een herinnering met: /reminder [dd-mm-jjjj] "
    "[uu:mm] [herinnering tekst].",
    'reminder_saved': "Reminder %s saved! %s"
}
}


start = {'en': {
    'usage': "The /start command initializes the bot.",
    'reply': "Bot enabled. Type /help for a list of commands."
},
    'nl': {
    'usage': "Het /start commando initialiseert de bot.",
    'reply': "Bot gestart. Type /help voor een lijst met commando's."
}
}

stats = {'en': {
    'usage': "The /stats command returns statistics of the "
    "chat.",
    'reply': "Total messages sent: %i\n"
    "Total words sent: %i\n\n"
    "Top 3 most used commands:\n"
    "1. %s (%i times)\n2. %s (%i times)\n3. %s (%i times)\n\n"
    "Most active users (number of messages):\n%s",
    'error': "Sorry, not enough data yet. Chat some more!"
},
    'nl': {
    'usage': "Het /stats commando geeft de huidige "
    "gespreksstatistieken.",
    'reply': "Totaal verzonden berichten: %i\n"
    "Totaal verzonden woorden: %i\n\n"
    "Top 3 meest gebruikte commando's:\n"
    "1. %s (%i keer)\n2. %s (%i keer)\n3. %s (%i keer)\n\n"
    "Meest actieve gebruikers (aantal berichten):\n%s",
    'error': "Sorry, nog niet genoeg data. Chat nog wat meer!"
}
}

status = {'en': {
    'usage': "The /status commands lets you know the current status "
    "of the bot.",
    'reply': "PyBot is up and running. Awaiting your commands."
},
    'nl': {
    'usage': "Het /status commando geeft de huidige status weer van "
    "de bot.",
    'reply': "PyBot staat voor je klaar en wacht op je commando."
}
}

users = {'en': {
    'usage': "The /users command returns all users that have been detected.",
    'reply': "I have detected the following users:\n"
},
    'nl': {
    'usage': "Het /users commando retourneert alle gedetecteerde gebruikers.",
    'reply': "Ik heb de volgende gebruikers gedetecteerd:\n"
}
}

weather = {'en': {
    'usage': "Get the actual weather with '/weather [place name]'.",
    'lang': 'en',
    'error': "Sorry, no results found for '%s'.",
    'reply': "It's %s degrees Celsius in %s. Weather description: "
    "%s."
},
    'nl': {
    'usage': "Krijg de actuele weersomstandigheden met '/weather "
    "[plaatsnaam]'.",
    'lang': 'nl',
    'error': "Sorry, geen resultaten gevonden voor '%s'.",
    'reply': "Het is %s graden in %s. Weersomstandigheden: %s."
}
}

wiki = {'en': {
    'usage': "Search wikipedia using '/wiki [query]'. For example: "
    "'/wiki Albert Einstein'.",
    'no_results': "Sorry, no results found for '%s'."
},
    'nl': {
    'usage': "Doorzoek wikipedia met '/wiki [zoekterm]'. "
    "Bijvoorbeeld: '/wiki Albert Einstein'.",
    'no_results': "Sorry, geen resultaten gevonden voor '%s'."
}
}

xkcd = {'en': {
    'usage': "The command /xkcd returns the newest xkcd image."
},
    'nl': {
    'usage': "Het commando /xkcd retourneert de nieuwste xkcd."
}
}

youtube = {'en': {
    'usage': "Search YouTube with '/youtube [query]'. The first "
    "result is then returned.",
    'no_results': "Sorry, no results found for '%s'."
},
    'nl': {
    'usage': "Doorzoek YouTube met '/youtube [zoekterm]'. Het "
    "eerste resultaat wordt gegeven.",
    'no_results': "Sorry, geen resultaten gevonden voor '%s'."
}
}

template = {'en': {
    'usage': ""
},
    'nl': {
    'usage': ""
}
}
