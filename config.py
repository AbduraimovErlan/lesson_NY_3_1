from aiogram import Bot, Dispatcher, types
from decouple import config


TOKEN = config("TOKEN")#токен самого проекта

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot) #диспечер проекта

ADMINS = (744475470, )

