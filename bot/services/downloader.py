import yt_dlp
from pathlib import Path
from bot.config import DOWNLOAD_PATH, COOKIE_FILE


def download_youtube(url: str) -> str:

    Path(DOWNLOAD_PATH).mkdir(exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_PATH}/%(title)s_%(id)s_%(height)sp.%(ext)s",
        "format": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "noplaylist": True,
        "merge_output_format": "mp4",
         "trim_file_name": 200,        
    }

    if COOKIE_FILE:
        ydl_opts["cookiefile"] = COOKIE_FILE

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename
