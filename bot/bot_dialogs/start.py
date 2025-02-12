from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Start, Group
from FSMstates import states
from text_templates.inline_buttons import START_MENU_DESCRIPTION, BUTTONS_START_MENU

# TODO rewrite start menu dialog to using switch generator ?
# exercise_levels_switches = generate_switches(BUTTONS_START_MENU)
# start_menu_dialog = Dialog(
#     Window(
#         Const(START_MENU_DESCRIPTION),
#         Row(*exercise_levels_switches),
#         MAIN_MENU_BUTTON,
#         state=states.Exercise.START_MENU,
#     )
# )

start_menu_dialog = Dialog(
    Window(
        Const(START_MENU_DESCRIPTION),
        Group(
            Start(
                text=Const("Как пользоваться"),
                id=BUTTONS_START_MENU["Как пользоваться"],
                state=states.Usage.MAIN,
            ),
            Start(
                text=Const("Упражнения"),
                id=BUTTONS_START_MENU["Упражнения"],
                state=states.Exercise.MAIN,
            ),
            Start(
                text=Const("Книги на английском"),
                id=BUTTONS_START_MENU["Книги на английском"],
                state=states.Books.MAIN,
            ),
            Start(
                text=Const("Рейтинг участников"),
                id=BUTTONS_START_MENU["Рейтинг участников"],
                state=states.Rating.MAIN,
            ),
            Start(
                text=Const("Учить слова"),
                id=BUTTONS_START_MENU["Учить слова"],
                state=states.LearnWords.MAIN,
            ),
            Start(
                text=Const("Напоминания"),
                id=BUTTONS_START_MENU["Напоминания"],
                state=states.Notifications.MAIN,
            ),
            Start(
                text=Const("Обратная связь"),
                id=BUTTONS_START_MENU["Обратная связь"],
                state=states.Feedback.MAIN,
            ),
            width=2,
        ),
        state=states.StartMenu.MAIN,
    ),
)
