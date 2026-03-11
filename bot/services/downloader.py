import yt_dlp
from pathlib import Path
from bot.config import DOWNLOAD_PATH, COOKIE_FILE


def download_youtube(url: str) -> str:

    Path(DOWNLOAD_PATH).mkdir(exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_PATH}/%(title)s.%(ext)s",
        "format": "mp4",
        "noplaylist": True,        
    }

    if COOKIE_FILE:
        ydl_opts["cookiefile"] = COOKIE_FILE

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename
