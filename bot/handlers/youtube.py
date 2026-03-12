from aiogram import Router
from aiogram.types import Message, FSInputFile
from bot.services.downloader import download_youtube
from bot.services.upload_service import upload_video
import os

router = Router()


@router.message()
async def youtube_handler(message: Message):

    url = message.text

    if "youtube.com" not in url and "youtu.be" not in url:
        return

    await message.answer("Скачиваю...")

    try:
        file_path = download_youtube(url)

        await message.answer("Загружаю на сервер...")  # потом добавить размер файла

        link = upload_video(file_path)
        os.remove(file_path)

        await message.answer(
        f'<a href="{link}">Скачать видео</a>',
        parse_mode="HTML"
        )

        

    except Exception as e:
        await message.answer(f"Ошибка: {e}")
