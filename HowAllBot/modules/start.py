from HowAllBot import app,START_PIC,OWNER_ID
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

buttons = InlineKeyboardMarkup([[InlineKeyboardButton("sʜᴀʀᴇ ᴀɴʏ ᴛʜɪɴɢ ✌️",switch_inline_query="")]])
START_TEXT = """
ʜᴇʏ ᴀᴍ ɪᴜsᴛ ᴀ ғᴜɴ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ {}.
ᴛᴏ ᴜsᴇ ᴍᴇ ɪᴜsᴛ ᴛʏᴘᴇ @{} ɪɴᴛᴏ ʏᴏᴜʀ ᴛᴇxᴛ ʙᴏx ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴᴇ ᴏғ ᴛʜᴇ ʀᴇsᴜʟᴛs ᴏʀ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴀᴛᴛᴀᴄʜᴇᴅ ᴛᴏ ᴛʜɪs ᴍᴇssᴀɢᴇ (sʜᴀʀᴇ ᴀɴʏ ᴛʜɪɴɢ).
"""


@app.on_message(filters.command("start"))
async def _start(_, message):
    BOT = (await _.get_me()).username    
    USER = (await _.get_users(OWNER_ID)).mention 
    await message.reply_photo(
    photo =  START_PIC,
    caption = START_TEXT.format(USER,BOT),
    reply_markup = buttons)
