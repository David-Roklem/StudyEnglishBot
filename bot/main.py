import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import settings
from handlers import base_handlers
from keyboards.menu_button import set_menu_button
from aiogram_dialog import setup_dialogs
from bot_dialogs.start import start_menu_dialog
from bot_dialogs.exercise import exercise_levels_dialog

logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s")

    logger.info("Starting bot")

    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.startup.register(set_menu_button)
    dp.include_router(base_handlers.router)
    dp.include_routers(start_menu_dialog, exercise_levels_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
