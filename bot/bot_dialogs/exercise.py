from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Button,
    Column,
    Group,
    Row,
    Select,
    SwitchTo,
)
from aiogram_dialog.widgets.text import Const, Format
from FSMstates import states
from text_templates.inline_buttons import (
    CHOOSE_LVL,
    BUTTONS_STUDENT_LVL,
)
from bot_dialogs.common import MAIN_MENU_BUTTON, generate_switches


exercise_levels_switches = generate_switches(BUTTONS_STUDENT_LVL)
exercise_levels_dialog = Dialog(
    Window(
        Const(CHOOSE_LVL),
        Row(*exercise_levels_switches),
        MAIN_MENU_BUTTON,
        state=states.Exercise.START_MENU,
    )
)

# exercise_category_window = Window(
#     Const(CHOOSE_EXERCISE_CATEGORY),
#     Row("Грамматика"),
#     LAYOUTS_MAIN_MENU_BUTTON,
#     state=states.Layouts.ROW,
# )
