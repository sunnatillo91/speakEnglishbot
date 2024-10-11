import asyncio
import logging
import sys
from os import getenv
from oxfordLookUp import getDefinitions
from googletrans import Translator

translator = Translator()

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

# wikipedia.set_lang('uz')

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7466032534:AAFpWAzQiipegNSoWudnsvxv5df2OaK9kq0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(Command(commands='start'))
async def start(message: types.Message):
    await message.answer("Speak english Botiga Xush Kelibsiz!")

@dp.message(Command(commands='help'))
async def help(message: types.Message):
    await message.answer("Ushbu bot ingliz tilini o'rganishda qulay yordamchi bo'ladi:)")

@dp.message()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        # await message.reply(translator.translate(message.text, dest).text)  bu reply ko'rinishida qaytaradi
        await message.answer(translator.translate(message.text, dest).text) # bu javob ko'rinishida qaytaradi
    else:
        word_id = translator.translate(message.text, dest='en').text
        
    
    lookup = getDefinitions(word_id)
    if lookup:
        await message.reply(f"Word: {word_id} \n{lookup['definitions']}")
        if lookup.get('audio'):
            await message.reply_audio(lookup['audio'])
    else:
        await message.reply("Bunday so'z topilmadi")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())