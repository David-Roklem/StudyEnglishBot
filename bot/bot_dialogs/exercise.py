from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Const, Format
from FSMstates import states
from text_templates.inline_buttons import START_MENU_BUTTONS_TEXT, BUTTONS_STUDENT_LVL
from bot_dialogs.common import MAIN_MENU_BUTTON, generate_switches


exercise_levels_switches = generate_switches(BUTTONS_STUDENT_LVL)
exercise_levels_dialog = Dialog(
    Window(
        Const(START_MENU_BUTTONS_TEXT["exercises"]),
        Row(*exercise_levels_switches),
        MAIN_MENU_BUTTON,
        state=states.Exercise.MAIN,
    )
)


# exercise_category_window = Window(
#     Const(CHOOSE_EXERCISE_CATEGORY),
#     Row("Грамматика"),
#     LAYOUTS_MAIN_MENU_BUTTON,
#     state=states.Layouts.ROW,
# )
