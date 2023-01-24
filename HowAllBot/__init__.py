import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from motor.motor_asyncio import AsyncIOMotorClient


#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
OWNER_ID = Config.OWNER_ID
START_PIC = Config.START_PIC
MONGO_DB = Config.MONGO_DB_URL
SUDOES.append(OWNER_ID)
if not START_PIC:
    START_PIC = "https://graph.org/file/c1c19fee2ac7b458087f7.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#database
mongo = AsyncIOMotorClient(MONGO_DB)
db = mongo.HowAllBot


#client
app = Client(
    "HowAllBot",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    



