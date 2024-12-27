import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# from handlers import handlers
from config import settings
from routers.commands import base_commands
from keyboards.menu_button import set_menu_button


async def main():
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Регистрируем асинхронную функцию в диспетчере, которая будет выполняться на старте бота
    dp.startup.register(set_menu_button)
    dp.include_router(base_commands.router)

    logging.basicConfig(level=logging.DEBUG)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
