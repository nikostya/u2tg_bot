import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")
COOKIE_FILE = os.getenv("COOKIE_FILE")