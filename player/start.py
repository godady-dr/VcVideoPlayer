from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from plugins.tr import TGPK_TEXT, VSONG_TEXT, PASTE_TEXT, INFO_TEXT, STREAM_TEXT, START_TEXT, HELP_TEXT
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❔ Help & Command ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("Channel 📢", url=f"https://t.me/{UPDATES_CHANNEL}",
                InlineKeyboardButton("Support 👥", url=f"https://t.me/{SUPPORT_GROUP}"),
            ],
            [
                InlineKeyboardButton("Dev🧑‍💻", url=f"https://t.me/coder_debojit"),
                InlineKeyboardButton("Dev Support 📞", url=f"https://t.me/debojit_chat"),
            ],
            [
               InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
      m=await message.reply_photo(
                                  photo="https://telegra.ph/file/b85d375e9e6cb3cb07896.jpg", 
                                  caption=START_TEXT.format(message.from_user.first_name, message.from_user.id),
                                  reply_markup=reply_markup
      )      
   else:
      await message.reply(f"**👋 Hey ᴄʀʏᴘᴛᴏɴɪᴛᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍᴇʀ is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Sᴛʀᴇᴀᴍ", callback_data="stream"),
                InlineKeyboardButton ("Iɴfo", callback_data="info"),
            ],
            [
                InlineKeyboardButton("Vɪᴅᴇᴏ Sᴏɴɢ", callback_data="vsong"),
                InlineKeyboardButton ("Pᴀsᴛᴇ", callback_data="paste"),
            ],
            [
               InlineKeyboardButton("Tᴇʟᴇ ✮ ɢʀᴀᴘʜ", callback_data="tgph"),
            ],
            [
               InlineKeyboardButton("╰✰ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
               InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
               InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ ✰╮", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="tgph":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                TGPK_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="stream":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                STREAM_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="paste":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                PASTE_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="vsong":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                VSONG_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="info":
        buttons = [
            [
                InlineKeyboardButton ("╰✰ Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ ✰╮", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                INFO_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("❔ Help & Command ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("Channel 📢", url=f"https://t.me/{UPDATES_CHANNEL}",
                InlineKeyboardButton("Support 👥", url=f"https://t.me/{SUPPORT_GROUP}"),
            ],
            [
                InlineKeyboardButton("Dev🧑‍💻", url=f"https://t.me/coder_debojit"),
                InlineKeyboardButton("Dev Support 📞", url=f"https://t.me/debojit_chat"),
            ],
            [
               InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
