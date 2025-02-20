from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from FSMstates import states
from text_templates.inline_buttons import START_MENU_BUTTONS_TEXT
from bot_dialogs.common import MAIN_MENU_BUTTON

books_dialog = Dialog(
    Window(
        Const(START_MENU_BUTTONS_TEXT["books"]),
        MAIN_MENU_BUTTON,
        state=states.Book.MAIN,
    )
)
