from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from text_templates.inline_buttons import BUTTONS_START_MENU
from text_templates import base_commands
from keyboards.inline_keyboards.inline_kb import create_inline_kb

router = Router()


@router.message(CommandStart())
async def cmd_start_testing_inline_kb(message: Message):
    """
    testing_inline_kb
    """
    keyboard = create_inline_kb(2, **BUTTONS_START_MENU)
    await message.answer(text="Потестим Инлайн клаву", reply_markup=keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=base_commands.help_cmd)
