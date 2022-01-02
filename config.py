import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN',1956381927))
CHANNEL = int(os.getenv('CHANNEL',-1001680925414))
API_ID = int(os.getenv("API_ID", "7082124"))
API_HASH = os.getenv("API_HASH", "aa31753f777a0a4059b68f0225196dc8")
BOT_USERNAME = os.getenv("BOT_USERNAME", "teleutils_bot")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Cryptonite_club")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "CryptoNite_News")
SOURCE_CODE = os.getenv("SOURCE_CODE", "null")
BOT_TOKEN = os.getenv("BOT_TOKEN", "1915220412:AAGQvPDIhucp0_BTSrXwRUufBwRtfFy_l2A")
SESSION_NAME = os.getenv("SESSION_NAME", "AQBOfitwWiX34AWytq7jJpVAlXU_ZMIRshi9JIxZJCSehYi92U_9ifM8rcyzzzsHIXOct-PVZkNR91lN98-BbyPRgzUE6uBREle4AuSQCxHyEPcljbjTw7rLwltdP0rx3ff4S_C1z8iizeGWKLKYZKJo2mQD77VEGxyrB2XlLucab5PwZaaa88XiwBzbyuGjbopgx-28uPe7Aznm0mwM4aX5SuLmrLvkWVuEImREcTwvD6G6STH6H-WLv4Wqk0ZDrujUDWAg1kDTph5yO7HTSCkk5IuxH9jEFxUpg-i7iAfJ6z1Xewj0s1qPQB7SkHSRDuo8gz_CTWmfDhz30kcILfPQXsoOyAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1450779437").split()))
