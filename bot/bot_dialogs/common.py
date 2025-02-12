from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from FSMstates import states

MAIN_MENU_BUTTON = Start(
    text=Const("☰ Main menu"),
    id="__main__",
    state=states.StartMenu.START_MENU,
)


def generate_switches(buttons: dict):
    switches = [
        SwitchTo(
            text=Const(btn_text),
            id=btn_name.lower(),
            state=getattr(states.Exercise, btn_name)
        ) for btn_text, btn_name in buttons.items()
    ]
    return switches
