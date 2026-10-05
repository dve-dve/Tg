#---------- © sᴛᴀʟᴋᴇʀ@hehe_stalker
#---------- ᴘʀᴏJᴇᴄᴛ - ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ sᴇʟʟɪɴɢ ʙᴏᴛ
#-------------------------------------------------------
import os
from dotenv import load_dotenv

load_dotenv()

def _getenv(name: str, default: str | None = None, required: bool = False) -> str:
    val = os.getenv(name, default)
    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required env var: {name}")
    return val
    
MUST_JOIN_CHANNEL = "-1004199515021"
BOT_TOKEN = _getenv("8830257783:AAHMaJww6ekNmWTUaZcH_5gNlU8y6vIx5UA", required=True)
ADMIN_IDS = [int(i) for i in _getenv("ADMIN_IDS", "", required=True).replace(" ", "").split(",") if i]
API_ID = "31724382"
API_HASH = "cdaa5c6f43ec7eccbe7142d25e6e1c67"

DATABASE_URL = "mongodb+srv://OtpWala:PapaiPaul13@otpwala.gjxwbr3.mongodb.net/?appName=OtpWala"

DEFAULT_CURRENCY = _getenv("DEFAULT_CURRENCY", "₹")
MIN_BALANCE_REQUIRED = float(_getenv("MIN_BALANCE_REQUIRED", "0"))