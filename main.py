import asyncio
import logging
# from aiogram import Dispatcher
from handlers import handlers
from config import dp, bot


# handlers.register_all_handlers(dp)
# from aiogram import types
# @dp.message()
# async def echo_msg(message: types.Message):
#     await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
