import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from middlewares.session import DbSessionMiddleware
from middlewares.track_all_users import TrackAllUsersMiddleware
import bot_dialogs
from config_data.config import settings
from handlers import base_handlers
from keyboards.menu_button import set_menu_button
from aiogram_dialog import setup_dialogs

logger = logging.getLogger(__name__)


async def main():

    engine = create_async_engine(url=str(settings.DB_URL))

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

    # Подключение мидлварей
    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    dp.update.outer_middleware(DbSessionMiddleware(Sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    dp.startup.register(set_menu_button)
    dp.include_router(base_handlers.router)
    dp.include_routers(*dialogs_to_register)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
