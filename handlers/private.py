import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afb59219c0a0428c63084.jpg",
        caption=f"""** 

 ᴛsɢ ᴍᴜsɪᴄ ɪs ᴀɴ sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ ʜᴏsᴛᴇᴅ ᴏɴ ᴘʀɪᴠᴀᴛᴇ  ᴠᴘs  sᴇʀᴠᴇʀ🎸💝

                             ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ = [ᴀᴍᴀɴ ❤️](https://t.me/itzamanrajput)

ᴄʀᴇᴀᴛᴏʀ :- [✨ ᴀᴍᴀɴ ʀᴀᴊᴘᴜᴛ  💜](https://t.me/itzamanrajput)
sᴜᴘᴘᴏʀᴛ :- [✨ ᴛsɢ ɢʀᴏᴜᴘ ❤️🎸](https://t.me/Friends_Chatting_Group3)

ƖƑ ƳƠƲ ӇƛƔЄ ƛƝƳ ƢƲЄƦƳ ƇƠƝƬƛƇƬ ƬƠ ƠƜƝЄƦ = [ᴀᴍᴀɴ  ❤️](https://t.me/itzamanrajput)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/Friends_Chatting_Group3")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7ca878a87eb74e36254c7.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://te.legra.ph/file/7ca878a87eb74e36254c7.jpg")
                ]
            ]
        ),
    )
