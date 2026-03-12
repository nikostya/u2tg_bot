import subprocess
import os

from bot.config import (
    SSH_HOST,
    SSH_PORT,
    SSH_USER,
    SSH_REMOTE_PATH,
    PUBLIC_BASE_URL,
)

def upload_video(local_path: str) -> str:
    filename = os.path.basename(local_path)
    remote_target = f"{SSH_USER}@{SSH_HOST}:{SSH_REMOTE_PATH}/{filename}"
    subprocess.run(
        [
            "scp",
            "-P", str(SSH_PORT),
            "-o", "StrictHostKeyChecking=accept-new",
            local_path,
            remote_target,
        ],
        check=True,
    )

    # ссылка для пользователя
    from urllib.parse import quote
    safe_filename = quote(filename)
    return f"{PUBLIC_BASE_URL}/{safe_filename}"