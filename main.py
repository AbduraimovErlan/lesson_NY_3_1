from config import dp, bot, ADMINS
from aiogram.utils import executor
from handlers import client, callback, extra, admin, fsm_anketa, schedule
import logging
from database.bot_db import sql_create

async def on_startup(_):# функция для того чтоб запустить база данных
    await schedule.set_scheduler()
    await bot.send_message(ADMINS[0], "Я родился!")
    sql_create()#импартируем и подключаем база данных сюда в майн

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)

extra.register_handlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)