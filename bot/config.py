import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")
COOKIE_FILE = os.getenv("COOKIE_FILE")

SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT", 22))
SSH_USER = os.getenv("SSH_USER")
SSH_REMOTE_PATH = os.getenv("SSH_REMOTE_PATH")
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL")
