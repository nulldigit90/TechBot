'''Common command for bots. This one, at random will refuse to blindly
say what the user wants'''

import random

def main(nick, comargs, chan, send):
    lol = random.randrange(1,50)
    if lol > 25 and lol < 35:
        phrase = "How about no. Bruh, %s" % nick
    else:
        phrase = comargs.strip()

    send.put((phrase, chan))
