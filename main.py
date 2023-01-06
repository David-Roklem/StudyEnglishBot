from aiogram.utils import executor
from handlers import handlers
from config import dp


handlers.register_all_handlers(dp)

async def on_startup(_):
    print("Bot's online! 2translate")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
