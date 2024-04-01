import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app  
from AnonXMusic.core.userbot import Userbot
from AnonXMusic.utils.database import delete_served_chat
from AnonXMusic.utils.database import get_assistant



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** {message.chat.id}"
                
             ]))
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
