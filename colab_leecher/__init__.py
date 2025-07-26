# __init__.py

# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging
import json
import os
from uvloop import install
from pyrogram import Client

# Setup better performance with uvloop
install()

# Load credentials from JSON file (if exists), else from environment variables
if os.path.exists("credentials.json"):
    with open("credentials.json", "r") as f:
        credentials = json.load(f)
        API_ID = credentials["API_ID"]
        API_HASH = credentials["API_HASH"]
        BOT_TOKEN = credentials["BOT_TOKEN"]
        OWNER = credentials["USER_ID"]
        DUMP_ID = credentials["DUMP_ID"]
else:
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    OWNER = int(os.environ.get("USER_ID", 0))
    DUMP_ID = int(os.environ.get("DUMP_ID", 0))

# Initialize logging
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    level=logging.INFO
)

# Initialize Pyrogram Client
colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
