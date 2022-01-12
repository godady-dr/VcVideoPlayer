import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN',1450779437))
CHANNEL = int(os.getenv('CHANNEL',-1001451057225))
API_ID = int(os.getenv("API_ID", "17345948"))
API_HASH = os.getenv("API_HASH", "ae6edf5c66031300e59ff940a52dfd67")
BOT_USERNAME = os.getenv("BOT_USERNAME", "teleutils_bot")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Cryptonite_club")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "CryptoNite_News")
SOURCE_CODE = os.getenv("SOURCE_CODE", "null")
BOT_TOKEN = os.getenv("BOT_TOKEN", "5004190164:AAGChRIix1fR0ipUH038fT-QYmbiThMT654")
SESSION_NAME = os.getenv("SESSION_NAME", "BQBTYR6Bi06XWRcROHG2apnqh3CKamHDHsMpOzC_Dlpjot1InGrefmdtM3RR8cv_utgTmAJFYFYCzKcxRPoviPctvlKrwzM4p8dgchuzPQN209oOiAYZ9f0gQxffzZgK2mY9xCM8uYr2C7a_xnvnr2qn2leemJ46v6xdmXXwnbQN4ew2Lxj8_xWO4HeQKckUvqXz7hNWzIbVCTIpn25-W2Mm1eRV8RR7cb_Ye6lV4cHwo7X_K72YWHVPPsg8580W6GIVZcSEp0HS7V9E3eDYuiKrM4vmJ1rHSYp68VUoeDLsX6EoWOvolZih12zeOGVVFXEAQpcvpqDV026cneP1XpnSeXGsHwA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "962844567 2037492767 1450779437").split()))
