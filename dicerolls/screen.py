import lvgl as lv
from gui.screens.screen import Screen
from gui.common import add_label, add_button_pair , add_button, HOR_RES
from gui.decorators import on_release, cb_with_args

from .const import *

class DiceRollsScreen(Screen):
    def __init__(self, title, message, note=None):
        super().__init__()
        self.title = add_label(title, scr=self, style="title")
        obj = self.title
        if note is not None:
            self.note = add_label(note, scr=self, style="hint")
            self.note.align(self.title, lv.ALIGN.OUT_BOTTOM_MID, 0, 5)
            obj = self.note
        self.page = lv.page(self)
        self.page.set_size(480, 600)
        self.message = add_label(message, scr=self.page)
        self.page.align(obj, lv.ALIGN.OUT_BOTTOM_MID, 0, -10)

        self.pips_1 = add_button("1", on_release(cb_with_args(self.set_value, DICE_ROLLED_1)), scr=self)
        self.pips_1.set_width(130)
        self.pips_1.align(self.page, lv.ALIGN.OUT_LEFT_MID, 20, 20)
        self.pips_1.set_x(100)

        self.pips_2 = add_button("2", on_release(cb_with_args(self.set_value, DICE_ROLLED_2)), scr=self)
        self.pips_2.set_width(130)
        self.pips_2.align(self.page, lv.ALIGN.OUT_RIGHT_MID, 20, 20)
        self.pips_2.set_x(HOR_RES - 230)

        self.pips_3 = add_button("3", on_release(cb_with_args(self.set_value, DICE_ROLLED_3)), scr=self)
        self.pips_3.set_width(130)
        self.pips_3.align(self.page, lv.ALIGN.OUT_LEFT_MID, -20, 110)
        self.pips_3.set_x(100)

        self.pips_4 = add_button(u"4", on_release(cb_with_args(self.set_value, DICE_ROLLED_4)), scr=self)
        self.pips_4.set_width(130)
        self.pips_4.align(self.page, lv.ALIGN.OUT_RIGHT_MID, 20, 110)
        self.pips_4.set_x(HOR_RES - 230)

        self.pips_5 = add_button("5", on_release(cb_with_args(self.set_value, DICE_ROLLED_5)), scr=self)
        self.pips_5.set_width(130)
        self.pips_5.align(self.page, lv.ALIGN.OUT_LEFT_MID, -20, 200)
        self.pips_5.set_x(100)

        self.pips_6 = add_button("6", on_release(cb_with_args(self.set_value, DICE_ROLLED_6)), scr=self)
        self.pips_6.set_width(130)
        self.pips_6.align(self.page, lv.ALIGN.OUT_RIGHT_MID, 20, 200)
        self.pips_6.set_x(HOR_RES - 230)

        (self.close_button, self.again_button) = add_button_pair(
            lv.SYMBOL.LEFT + " Back",
            on_release(cb_with_args(self.set_value, BACK)),
            "TODO: Use this seed",
            on_release(cb_with_args(self.set_value, USE_SEED)),
            scr=self,
        )
