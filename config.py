from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24810254")
    API_HASH = environ.get("API_HASH", "aadb42caec01695fa0a77c09b3e0ef47")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6336256307:AAF8htgL8PTyulhefLKqqxf5pI8k-TS1YSM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7077099034').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
