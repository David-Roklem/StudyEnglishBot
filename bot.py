from aiogram.utils import executor
from config import dp
from handlers import handlers


# client_easy.register_handlers_client(dp)
# admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)


async def on_startup(_):
    print("2translate has started!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
