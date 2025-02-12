from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Start
from FSMstates import states
from text_templates.inline_buttons import START_MENU_DESCRIPTION


start_menu_dialog = Dialog(
    Window(
        Const(START_MENU_DESCRIPTION),
        Start(
            text=Const("Упражнения"),
            id="exercises",
            state=states.Exercise.START_MENU,
        ),
        state=states.StartMenu.START_MENU,
    ),
)
