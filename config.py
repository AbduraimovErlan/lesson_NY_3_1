from aiogram import Bot, Dispatcher, types
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")#токен самого проекта

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage) #диспечер проекта

ADMINS = (744475470, )



