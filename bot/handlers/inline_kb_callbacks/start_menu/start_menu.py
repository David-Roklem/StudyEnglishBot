from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards.inline_kb import create_kb_exercises_levels
from text_templates.inline_buttons import BUTTONS_START_MENU, CHOOSE_LVL, START_MENU_BUTTONS_TEXT, BUTTONS_STUDENT_LVL

start_menu_router = Router()


@start_menu_router.callback_query(F.data == BUTTONS_START_MENU["Как пользоваться"])
async def process_usage_button(callback: CallbackQuery):
    """
    Описание для меню "Как пользоваться"
    """
    await callback.message.edit_text(START_MENU_BUTTONS_TEXT[callback.data])


@start_menu_router.callback_query(F.data == BUTTONS_START_MENU["Упражнения"])
async def process_excercises_button(callback: CallbackQuery):
    keyboard = create_kb_exercises_levels(2, *BUTTONS_STUDENT_LVL, button_source=BUTTONS_STUDENT_LVL)
    await callback.message.edit_text(CHOOSE_LVL, reply_markup=keyboard)
