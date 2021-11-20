import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/8fe203de66df070f238bf.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Pratheek](t.me/pratheek06) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @AnimeXWrld_Chat «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://pratheek06"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/AnimeXWrld_Chat"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/pratheek06"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/AnimeXWrld_Chat"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/AnimeXWrld_Chat"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/DamnItsNikhil"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
