from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from FSMstates import states
from text_templates import base_commands

router = Router()


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.StartMenu.MAIN, mode=StartMode.RESET_STACK)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=base_commands.help_cmd)
