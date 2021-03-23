from app import BaseApp
from gui.screens import Menu
from .screen import DiceRollsScreen
from .rolls import rolls
from .const import *

from binascii import hexlify


class DiceRollsApp(BaseApp):
    """ """
    rolls = []
    prefixes = []
    button = "Dice Rolls"
    async def menu(self, show_screen):
        buttons = [
            (None, "Dice Rolls (D6)"),
            (FLUSH_ROLLS,  "Create new seed"),
            (ADD_ROLL,  "Continue current seed"),
        ]

        menuitem = await show_screen(Menu(buttons, title="Seed creation by rolling dice", last=(255, None)))
        while menuitem != 255:
            if menuitem in PIPS or menuitem in [FLUSH_ROLLS, ADD_ROLL]:
                if menuitem == FLUSH_ROLLS:
                    self.rolls = []
                elif menuitem == ADD_ROLL:
                    pass # continue mix into current seed
                roll = True
                while roll:
                    if menuitem in PIPS:
                        self.rolls.append(str(menuitem))
                    warn_message, words, word_ids, hash = rolls(''.join(self.rolls) )

                    ans_hash = hexlify(hash).decode('utf-8')
                    middle = int(len(ans_hash)/2)
                    hash1 = ans_hash[:middle]
                    hash2 = ans_hash[middle:]

                    if ans_hash == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
                        warn_message = "WARNING: Input is empty. This is a known wallet!" # overwrite low entropy warn message
                    if warn_message:
                        message = "%s\n%s" % (warn_message, words)
                    else:
                        message = words

                    scr = DiceRollsScreen(
                            title="Press 1-6 for each roll to mix in.",
                            note="%s rolls: %s\n-\n%s\n%s" % (len(self.rolls), ''.join(self.rolls), hash1, hash2 ),
                            message ="%s" % (message),
                    )
                    menuitem = await show_screen(scr)
                    if menuitem == USE_SEED:
                        print("TODO: USE SEED!")
                        roll = False
                    elif menuitem == ADD_ROLL:
                        roll = False
                    elif menuitem == BACK:
                        roll = False
                menuitem = await show_screen(Menu(buttons, title="Seed creation by rolling dice", last=(255, None)))
