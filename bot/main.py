import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import bot_dialogs
from config_data.config import settings
from handlers import base_handlers
from keyboards.menu_button import set_menu_button
from aiogram_dialog import setup_dialogs

logger = logging.getLogger(__name__)


async def main():

    dialogs_to_register = [
        # start menu
        bot_dialogs.usage.usage_dialog,
        bot_dialogs.exercise.exercise.exercise_dialog,
        bot_dialogs.exercise.exercise.exact_exercise_dialog,
        bot_dialogs.start.start_menu_dialog,
        bot_dialogs.books.books_dialog,
        bot_dialogs.rating.rating_dialog,
        bot_dialogs.learn_words.learn_words_dialog,
        bot_dialogs.notifications.notifications_dialog,
        bot_dialogs.feedback.feedback_dialog,
    ]

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s")

    logger.info("Starting bot")

    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.startup.register(set_menu_button)
    dp.include_router(base_handlers.router)
    dp.include_routers(*dialogs_to_register)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
