from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from text_templates import base_text_templates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Conversation's entry point
    """
    await message.answer(text=base_text_templates.start_cmd)
    # <b>Выберите, пожалуйста, ваш уровень английского:</b>""", reply_markup=kbl, parse_mode="HTML")


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=base_text_templates.help_cmd)
