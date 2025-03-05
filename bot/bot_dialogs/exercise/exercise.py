from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Row, Button, Back, SwitchTo, Group
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from FSMstates import states
from text_templates.inline_buttons import CHOOSE_EXERCISE_CATEGORY, CHOOSE_EXERCISE_TYPE, CHOOSE_LVL
from bot_dialogs.common import MAIN_MENU_BUTTON


async def save_level_data(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["level"] = button.widget_id


async def save_category_data(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["category"] = button.widget_id


levels_window = Window(
    Const(CHOOSE_LVL),
    Row(
        SwitchTo(
            text=Const("A1"),
            id="a1",
            state=states.Exercise.category,
            on_click=save_level_data,
        ),
        SwitchTo(
            text=Const("A2"),
            id="a2",
            state=states.Exercise.category,
            on_click=save_level_data,
        ),
        SwitchTo(
            text=Const("B1"),
            id="b1",
            state=states.Exercise.category,
            on_click=save_level_data,
        ),
        SwitchTo(
            text=Const("B2"),
            id="b2",
            state=states.Exercise.category,
            on_click=save_level_data,
        ),
        SwitchTo(
            text=Const("C1"),
            id="c1",
            state=states.Exercise.category,
            on_click=save_level_data,
        )
    ),
    MAIN_MENU_BUTTON,
    state=states.Exercise.level,
)

categories_window = Window(
    Const(CHOOSE_EXERCISE_CATEGORY),
    Row(
        SwitchTo(
            text=Const("Грамматика"),
            id="grammar",
            state=states.Exercise.type,
            on_click=save_category_data,
        ),
        SwitchTo(
            text=Const("Аудирование"),
            id="listening",
            state=states.Exercise.type,
            on_click=save_category_data,
        ),
        SwitchTo(
            text=Const("Говорение"),
            id="speaking",
            state=states.Exercise.type,
            on_click=save_category_data,
        ),
        SwitchTo(
            text=Const("Переводы"),
            id="translates",
            state=states.Exercise.type,
            on_click=save_category_data,
        ),
        SwitchTo(
            text=Const("Лексика"),
            id="vocabulary",
            state=states.Exercise.type,
            on_click=save_category_data,
        )
    ),
    Back(Const("Назад")),
    MAIN_MENU_BUTTON,
    state=states.Exercise.category,
)


async def to_exercise(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["type"] = button.widget_id
    exercise_data = dialog_manager.dialog_data
    await dialog_manager.start(state=states.ExactExercise.MAIN, data=exercise_data)


types_window = Window(
    Const(CHOOSE_EXERCISE_TYPE),
    Row(
        Button(
            text=Const("Простое настоящее время"),
            id="present_simple",
            on_click=to_exercise,
        ),
        Button(
            text=Const("Артикль 'a'"),
            id="article_a",
            on_click=to_exercise,
        ),
    ),
    Back(Const("Назад")),
    MAIN_MENU_BUTTON,
    state=states.Exercise.type,
)

exercise_dialog = Dialog(
    levels_window,
    categories_window,
    types_window,
)


async def exercise_data_getter(dialog_manager: DialogManager, state: FSMContext, **kwargs):
    """Извлекает данные из БД на основе информации, полученной на этапе пайплайна выбора упражнения"""
    start_data = dialog_manager.start_data
    # start_data передать в функцию-генератор (?), которая будет извлекать данные из БД по мере необходимости
    # т.е. первый вопрос извлекается 100%, а далее только по запросу (по клику юзера на получение след вопроса) 


exact_exercise_dialog = Dialog(
    Window(
        Const("Начнем. Первый вопрос..."),
        Group(
            Button(text=Const("Вариант 1"), id="var_1"),
            Button(text=Const("Вариант 2"), id="var_2"),
            width=2,
        ),
        MAIN_MENU_BUTTON,
        state=states.ExactExercise.MAIN,
    ),
)
