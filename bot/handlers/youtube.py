from aiogram import Router
from aiogram.types import Message, FSInputFile
from bot.services.downloader import download_youtube

router = Router()


@router.message()
async def youtube_handler(message: Message):

    url = message.text

    if "youtube.com" not in url and "youtu.be" not in url:
        return

    await message.answer("Скачиваю...")

    try:
        file_path = download_youtube(url)

        video = FSInputFile(file_path)

        await message.answer_video(video)

    except Exception as e:
        await message.answer(f"Ошибка: {e}")
