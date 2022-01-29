from dotenv import load_dotenv
import os

load_dotenv()

ANGEL_BOT_TOKEN = os.getenv("ANGEL_BOT_TOKEN")
PLAYERS_FILENAME = os.getenv("PLAYERS_FILENAME")
CHAT_ID_JSON = os.getenv("CHAT_ID_JSON")
ANGEL_ALIAS = os.getenv("ANGEL_ALIAS")
MORTAL_ALIAS = os.getenv("MORTAL_ALIAS")