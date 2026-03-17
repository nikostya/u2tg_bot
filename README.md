# Telegram YouTube Downloader Bot

A lightweight Telegram bot for downloading YouTube videos and returning a direct download link.

Designed for personal use by a small number of users (2–3 people).
The bot downloads videos using `yt-dlp`, uploads them to a remote storage server, and returns a public URL.

---

# Architecture

The project uses a **two-server architecture**:

```
User
  │
  ▼
Telegram
  │
  ▼
Bot server (Orange Pi)
  │
  ├─ yt-dlp downloads video
  │
  └─ SCP uploads file
      ▼
Storage server (Ubuntu)
      │
      ▼
Public HTTP link
```

## Bot Server

Device: Orange Pi 3 LTS
OS: Armbian

Responsibilities:

* run Telegram bot
* receive YouTube links from users
* download videos using `yt-dlp`
* upload files to storage server via `scp`

---

## Storage Server

OS: Ubuntu Server

Responsibilities:

* store downloaded videos
* provide HTTP access to files
* accept uploads via SSH/SCP

Files become publicly available via a base URL after upload.

---

# Project Structure

```
bot/
    main.py
    config.py
    handlers/
    services/

.env.example
requirements.txt
README.md
```

## bot/main.py

Application entry point.

Responsible for:

* initializing the Telegram bot
* registering handlers
* running the event loop

Run with:

```
python -m bot.main
```

---

## bot/config.py

Loads configuration from environment variables (`.env`).

Includes:

* Telegram token
* SSH settings
* storage paths
* public URL

---

## bot/handlers/

Telegram message handlers.

Responsibilities:

* receive YouTube links
* trigger download process
* return final link to user

---

## bot/services/

Service layer.

### download.py

Handles video downloading via `yt-dlp`.

Responsibilities:

* extract video metadata
* select format
* save file locally

---

### upload.py

Handles uploading files to the storage server.

Uses:

```
scp
```

After upload, generates a public URL.

---

# Requirements

Bot server:

```
python >= 3.10
ffmpeg
yt-dlp
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Infrastructure Setup

## 1. Prepare storage server

Create directory for video storage:

```
/var/www/videos
```

Configure a web server (nginx or apache) to expose files:

```
https://example.com/videos/<filename>
```

---

## 2. Configure SSH access

Bot server must connect to storage server via SSH.

Use key-based authentication:

```
ssh-keygen
ssh-copy-id user@storage-server
```

Verify access:

```
ssh user@storage-server
```

---

## 3. Test SCP upload

From bot server:

```
scp test.mp4 user@storage:/var/www/videos
```

---

# Configuration

Copy the template:

```
cp .env.example .env
```

Fill in required values.

---

# Running the Bot

Activate virtual environment:

```
source venv/bin/activate
```

Run:

```
python -m bot.main
```

---

# Running as a systemd Service

Create:

```
/etc/systemd/system/youtube-bot.service
```

```
[Unit]
Description=Telegram YouTube Downloader Bot
After=network.target

[Service]
User=bot
WorkingDirectory=/home/bot/youtube-bot
ExecStart=/home/bot/youtube-bot/venv/bin/python -m bot.main
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```
sudo systemctl daemon-reload
sudo systemctl enable youtube-bot
sudo systemctl start youtube-bot
```

Check status:

```
sudo systemctl status youtube-bot
```

---

# Usage

1. Send a YouTube link to the bot
2. The bot downloads the video
3. Uploads it to the storage server
4. Returns a public download link

---

# Security Notes

Do NOT commit:

* `.env`
* SSH keys
* Telegram bot token
* YouTube cookies

---

# Tech Stack

* Python
* aiogram
* yt-dlp
* SCP
* systemd
