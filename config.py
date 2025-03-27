import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "24413166")) #⚠️optional
API_HASH = getenv("API_HASH", "7d43dfedf3baa98292adb7b3f69cd6bd") #⚠️optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split())) #⚠️ Separate by space
OWNER_ID = int(getenv("OWNER_ID", "7080079152")) 
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://thelastcroneb:Tcroneb/2025@jinwoo.zvygv0t.mongodb.net/?retryWrites=true&w=majority&appName=jinwoo")
BOT_TOKEN = getenv("BOT_TOKEN", "7990396100:AAGr4egvoOLCWfE3wO_Kpsde9kxUZZJ-gdI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/4513f188be254572697e3.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/MrxBroken/BROKENUSERBOT") 
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
