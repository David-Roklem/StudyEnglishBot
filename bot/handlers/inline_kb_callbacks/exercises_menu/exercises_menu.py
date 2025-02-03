from pprint import pprint
from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from handlers.inline_kb_callbacks.callback_factory import Level, LevelCallbackFactory
from keyboards.inline_keyboards.inline_kb import create_inline_kb, create_inline_kb_levels
from text_templates.inline_buttons import BUTTONS_START_MENU, CHOOSE_LVL, START_MENU_BUTTONS_TEXT, BUTTONS_STUDENT_LVL
from aiogram.filters.callback_data import CallbackData


exercises_menu_router = Router()


@exercises_menu_router.callback_query(LevelCallbackFactory.filter(F.lvl == Level.A1))
async def process_lvl_a1_button(callback: CallbackQuery):
    """
    A1
    """
    # keyboard = create_inline_kb_levels(2, *BUTTONS_STUDENT_LVL, button_source=BUTTONS_STUDENT_LVL)
    # await callback.message.edit_text(CHOOSE_LVL, reply_markup=keyboard)
    await callback.message.edit_text("Заплатка A1")
