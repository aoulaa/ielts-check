from loader import bot, storage, db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    try:
        db.create_table_users()
    except Exception as err:
        print(err)
    # db.delete_users()
    print(db.select_all_users())
    await on_startup_notify(dp)
    await set_default_commands(dp)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
