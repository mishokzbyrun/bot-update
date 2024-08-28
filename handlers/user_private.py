from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
import common.keyboard as kb
import common.functions as fun
from filters.chat_types import ChatTypeFilter
from convert.speech_to_text import sp_to_text
from convert.text_to_speech import text_to_speech
import os
from pydub import AudioSegment
import speech_recognition as sr
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


async def ogg_to_wav(file_path):
    wfn = file_path.replace('.ogg', '.wav')
    segment = AudioSegment.from_file(file_path)
    segment.export(wfn, format='wav')
    return wfn

async def sp_to_text(file_path):
    recognizer = sr.Recognizer()
    audio_file = await ogg_to_wav(file_path)
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return f"Recognized speech: {text}"
        except sr.UnknownValueError:
            return "Speech recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from service; {e}"
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)


@user_private_router.message(Command('voice'))
async def cmd_voice(message: Message):
    await message.answer("Send me a text message:")


@user_private_router.message(F.voice)
async def audio_message(message: Message):
    file_info = await message.bot.get_file(message.voice.file_id)
    downloaded_file = await message.bot.download_file(file_info.file_path)
    ogg_filename = "audio.ogg"
    with open(ogg_filename, 'wb') as f:
        f.write(downloaded_file.read())
    recognized_text = await sp_to_text(ogg_filename)
    await message.answer(recognized_text)
    if os.path.exists(ogg_filename):
        os.remove(ogg_filename)

@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello user", reply_markup= await fun.inline_menu())

@user_private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('I`am your telegram bot and i`ll help you to make choice')

@user_private_router.message(F.text == 'Hello')
async def answer_hello(message: Message):
    await message.reply(f'Hello, my friend {message.from_user.full_name}')

@user_private_router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("Your choice is catalog", show_alert=True)
    await callback.message.edit_text("Select a car: ", reply_markup=await fun.reply_cars())
    
@user_private_router.message(Command("meme"))
async def cmd_meme(message: Message):
    await message.answer("Enter category you want see : ")
    text = message.text
    await message.answer_photo(fun.get_random_meme(text))   

@user_private_router.message(Command("duck"))
async def cmd_duck(message: Message):
    await message.answer_photo(fun.get_random_duck())