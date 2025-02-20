from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from FSMstates import states
from text_templates.inline_buttons import BUTTONS_STUDENT_LVL

MAIN_MENU_BUTTON = Start(
    text=Const("☰ Main menu"),
    id="__main__",
    state=states.StartMenu.MAIN,
)


# def generate_switches(buttons: dict, on_click: callable = None):
#     switches = [
#         SwitchTo(
#             text=Const(btn_text),
#             id=btn_name.lower(),
#             state=getattr(states.Levels, btn_name),
#             on_click=on_click,
#         ) for btn_text, btn_name in buttons.items()
#     ]
#     return switches


# print(generate_switches(BUTTONS_STUDENT_LVL))
