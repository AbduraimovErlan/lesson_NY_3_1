from aiogram import types, Dispatcher
from config import bot, dp


async def delete_sticker(message: types.Message):
    await message.delete()

async def bad_words_filter(message: types.Message):
    bad_words = ['html', 'js', 'css', 'жинди', 'дурак']
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"Не матерись, {message.from_user.full_name} сам ты {word}")
            await message.delete()
            # await bot.delete_message(message.chat.id, message.message_id)
            break

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()


    if message.text == "dice":
        a = await message.answer_dice()
        # await bot.send_dice(message.chat.id, emoji="🏀")
        print(a.dice.values)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
    dp.register_message_handler(delete_sticker, content_types=['sticker', 'photo', 'animation'])

# # @dp.message_handler() #эхо и ответ на все сообшение
# async def echo(message: types.Message):
#     if message.text == "python":
#         await message.answer("I love it!")
#     else:
#         await bot.send_message(chat_id=message.from_user.id, text=f"Саллалекум хозяин {message.from_user.full_name}")
#         await message.answer(f"This is an answer method!{message.message_id}")
#         await message.reply("This is a reply method!")
#
#     # print(message.text)
#     # bot.send_message()



