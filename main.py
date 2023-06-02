from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



TOKEN = config("TOKEN")#токен самого проекта

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot) #диспечер проекта




@dp.message_handler(commands=['start'])# текстовый ответ на команды старт
async def start_command(message: types.Message):
    await message.answer("Hello World!")

@dp.message_handler(commands=['help']) # возврашать фото на команду
async def start_command(message: types.Message):
     photo = open('media/pexels-photo-8428220.jpeg', 'rb')
     await message.answer_photo(photo=photo, caption="сам разбирайся!")
    # await bot.send_photo(message.from_user.id, photo=photo, caption="сам разбирайся!")


@dp.message_handler(commands=['quiz'])# опросник и его структура
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")# создание кнопки
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")

    markup.add(button_1, button_2)
    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup

    )


@dp.callback_query_handler(text="button_1")# следуюший страница опросника
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько яблок на березу?"
    answer = [
        "12",
        "3",
        "бессконечность",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=30,
    )

@dp.message_handler() #эхо и ответ на все сообшение
async def echo(message: types.Message):
    if message.text == "python":
        await message.answer("I love it!")
    else:
        await bot.send_message(chat_id=message.from_user.id, text=f"Саллалекум хозяин {message.from_user.full_name}")
        await message.answer(f"This is an answer method!{message.message_id}")
        await message.reply("This is a reply method!")

    # print(message.text)
    # bot.send_message()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)