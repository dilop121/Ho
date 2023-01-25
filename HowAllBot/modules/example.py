import random 
from HowAllBot import app
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
GUY_ABOVE = [
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ʜɪɢʜ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɢᴏɴɴᴀ ᴍᴀᴋᴇ ᴍᴇ ᴛᴇᴀ ᴡɪᴛʜ ʟᴇᴍᴏɴ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴍᴜsᴛ ғᴜᴄᴋ ᴛʜᴇ ɢᴜʏ ʙᴇʟᴏᴡ🔥",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴅᴏᴇsɴ'ᴛ ᴡᴇᴀʀ ᴘᴀɴᴛɪᴇs",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡᴀɴᴛs ᴛᴏ ʜᴀᴠᴇ ᴀ ʙɪɢɢᴇʀ ᴅɪᴄᴋ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ᴀ ᴘᴇᴅᴏᴘʜɪʟᴇ…",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ʜᴀs ᴀ ᴠᴇʀʏ ʙᴇᴀᴜᴛɪғᴜʟ sᴏᴜʟ sᴏ ɪ ᴄᴀɴ ғᴀʟʟ ɪɴ ʟᴏᴠᴇ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡᴀɴᴛs ᴍᴇ…",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ᴀ ʟᴇsʙɪᴀɴ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡɪʟʟ ʙᴇᴄᴏᴍᴇ ᴀ ʙᴀʀʙᴇᴄᴜᴇ ɪɴ ᴀ ᴍɪɴᴜᴛᴇ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ᴀ ʟᴏᴠᴇsɪᴄᴋ ғᴏᴏʟ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴅʀᴇᴀᴍs sᴏᴍᴇᴏɴᴇ ɢᴀᴠᴇ ʜɪᴍ ʜᴇᴀᴅ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ᴜɴᴅᴇʀ ᴀɴᴇsᴛʜᴇsɪᴀ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡɪʟʟ ʙᴇ ᴄᴜᴅᴅʟɪɴɢ ᴀᴡᴀʏ ᴡɪᴛʜ ᴍᴇ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴅʀᴇᴀᴍs ᴏғ sᴀᴜsᴀɢᴇs",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ʏᴏᴜ'ʀᴇ sᴜᴄʜ ᴀ sᴜᴄᴋᴇʀ.",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ɪᴇʀᴋɪɴɢ ᴏғғ ʀɪɢʜᴛ ɴᴏᴡ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ Mᴏᴀɴs sᴏ sᴡᴇᴇᴛ ᴡʜɪʟᴇ ғᴜᴄᴋᴇᴅ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡɪʟʟ ᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴘʟᴀᴄᴇ ᴛᴏᴍᴏʀʀᴏᴡ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ʜᴀs ʙᴜʀɴᴛ ᴏᴜᴛ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴇᴀᴛs ᴘᴏᴏᴘ 💩",
   "ɢᴜʏ ᴀʙᴏᴠᴇ  ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴛ 🐱✨ ᴍᴇᴏᴡ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴡɪʟʟ ʀᴀᴘᴇ ᴛʜᴇ ɢᴜʏ ʙᴇʟᴏᴡ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs ᴀ sʜɪᴛ ᴇᴀᴛᴇʀ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ғᴜᴄᴋᴇᴅ ᴀ ᴘɪɢ ᴏɴ Nᴇᴡ Yᴇᴀʀ's ᴇᴠᴇ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ᴍᴜsᴛ ᴋɪss ᴍᴇ💋",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ʟᴏᴠᴇs ᴛᴏ ʜᴜɢ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ɪs sᴇᴄʀᴇᴛʟʏ ɪᴇᴀʟᴏᴜs ᴏғ ᴍᴇ",
   "ɢᴜʏ ᴀʙᴏᴠᴇ ʜᴀs ɢᴏɴᴇ ғᴜᴄᴋɪɴɢ ᴄʀᴀᴢʏ",
   
  ]


NARUTO = ["ᴋᴜɴɪʜɪsᴀ","ʙᴀᴋɪ","sᴀsᴜᴋᴇ","ᴍɪɢʜᴛ ɢᴜʏ","ʟᴇᴇ","ɴᴀʀᴜᴛᴏ","ʜɪɴᴀᴛᴀ","sᴀᴋᴜʀᴀ","ɪɴᴏ","ᴋᴀᴋᴀsʜɪ","ᴍᴀᴅᴀʀᴀ","ʜᴀsʜɪʀᴀᴍᴀ","ᴛᴏʙɪʀᴀᴍᴀ","Iᴛᴀᴄʜɪ","ᴋɪʟʟᴇʀ ʙᴇᴇ","ᴢᴏʀᴏ 🛐","ᴍɪɴᴀᴛᴏ","ᴛsᴜɴᴀᴅᴇ","jɪʀᴀɪʏᴀ","ɴᴀɢᴀᴛᴏ","ɢᴀʀᴀᴀ","ᴘᴀɪɴ"]

AOT = ["ᴇʀᴇɴ ʏᴇᴀɢᴇʀ","Lᴇᴠɪ Aᴄᴋᴇʀᴍᴀɴ","ᴍɪᴋᴀsᴀ ᴀᴄᴋᴇʀᴍᴀɴ","ᴀʀᴍɪɴ","Eʀᴡɪɴ sᴍɪᴛʜ","ᴘɪᴇᴄᴋ","sʜᴀsʜᴀ","Jᴇᴀɴ","ᴀɴɴɪᴇ","ʀᴇɪɴᴇʀ","ᴀɴɴɪᴇ","ᴢᴇᴀᴋ","ʜᴀɴɪɪ ᴢᴏᴇ"]

ASS = ["ʜᴜɢᴇ","sᴍᴀʟʟ","ᴍᴇᴅɪᴜᴍ","ʟᴀʀɢᴇ"]

@app.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="💋 ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
                input_message_content=InputTextMessageContent(
                    f"💋 ɪ ᴀᴍ {random.randint(1,100)}% ʜᴏʀɴʏ ."
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "sʜᴀʀᴇ ʏᴏᴜʀ ʜᴏʀɴʏɴᴇss! 🔥",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🎈 ɢᴜʏ ᴀʙᴏᴠᴇ",
                input_message_content=InputTextMessageContent(
                    random.choice(GUY_ABOVE)
                ),
                thumb_url = "https://graph.org/file/ca51f7cd49e9e99db9db4.jpg",
                description="sᴇᴇ ᴡʜᴏ ᴀɴᴅ ʜᴏᴡ ᴛʜᴇ ɢᴜʏ ɪs ᴀʙᴏᴠᴇ ʏᴏᴜ.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ғɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ʀᴇsᴜʟᴛ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🔥 ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ғʀᴏᴍ ɴᴀʀᴜᴛᴏ",
                input_message_content=InputTextMessageContent(
                    f"🤩 ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ɴᴀʀᴜᴛᴏ ɪ ᴀᴍ :\n\n ⭐ **{random.choice(NARUTO)}** ⭐"
                ),
                thumb_url = "https://telegra.ph/file/6e9f3d55445344d83e34b.jpg",

                description="ғɪɴᴅ ᴏᴜᴛ ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ɴᴀʀᴜᴛᴏ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ғɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ʀᴇsᴜʟᴛ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🥺 ʜᴏᴡ ᴄᴜᴛᴇ ᴀʀᴇ ʏᴏᴜ",
                input_message_content=InputTextMessageContent(
                    f"💝 I ᴀᴍ {random.randint(1,100)}% ᴄᴜᴛᴇ."
                ),
                thumb_url = "https://graph.org/file/3c91402bbcd58d5f9254f.jpg",
                description="ғɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ᴄᴜᴛᴇɴᴇss",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "✨ sʜᴀʀᴇ ʏᴏᴜʀ ᴄᴜᴛᴇɴᴇss",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🏳‍🌈 ʜᴏᴡ ɢᴀʏ ᴀʀᴇ ʏᴏᴜ",
                input_message_content=InputTextMessageContent(
                    f"🏳‍🌈 I ᴀᴍ {random.randint(1,100)}% ɢᴀʏ."
                ),
                thumb_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7XBqdcAQasd4WLnb0OaQe7GP-iVUjXlNnxg&usqp=CAU", 
                description="ғɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢᴀʏɴᴇss",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "sʜᴀʀᴇ ʏᴏᴜʀ ɢᴀʏɴᴇss ʟᴏʟ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🍆 ᴡʜᴀᴛ's ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                input_message_content=InputTextMessageContent(
                    f"🍆 ᴍʏ ᴄᴏᴄᴋ sɪᴢᴇ ɪs {random.randint(1,100)}ᴄᴍ!"
                ),
                
                description="sᴇɴᴅ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴏᴄᴋ sɪᴢᴇ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🔰 ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ғʀᴏᴍ ᴀᴛᴛᴀᴄᴋ ᴏɴ ᴛɪᴛᴀɴ",
                input_message_content=InputTextMessageContent(
                    f"🔰 ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴀᴛᴛᴀᴄᴋ ᴏɴ ᴛɪᴛᴀɴ ɪ ᴀᴍ :\n\n ⭐ **{random.choice(AOT)}** ⭐"
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴀᴛᴛᴀᴄᴋ ᴏɴ ᴛɪᴛᴀɴ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ʀᴇsᴜʟᴛs",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🫂 ʜᴏᴡ ᴍᴜᴄʜ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʜᴜɢ ᴏᴛʜᴇʀ.",
                input_message_content=InputTextMessageContent(
                    f"🫂 I ᴡᴀɴᴛ ᴛᴏ ʜᴜɢ ʏᴏᴜ {random.randint(1,100)}%!"
                ),
                
                description="ғɪɴᴇ ᴏᴜᴛ ʜᴏᴡ ᴍᴜᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʜᴜɢ ᴏᴛʜᴇʀ ᴘᴇʀsᴏɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🍑 ᴡʜᴀᴛ's ʏᴏᴜʀ ᴀss sɪᴢᴇ",
                input_message_content=InputTextMessageContent(
                    f"🍑 ᴍʏ ᴀss ɪs {random.choice(ASS)}"
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ᴛʜᴇ sɪᴢᴇ ᴏғ ʏᴏᴜʀ ᴀss",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🙂 ʜᴏᴡ ʜᴀᴘᴘʏ ᴀʀᴇ ʏᴏᴜ",
                input_message_content=InputTextMessageContent(
                    f"🙂 ɪ ᴀᴍ {random.randint(1,100)}% ʜᴀᴘᴘʏ."
                ),
                
                description="ᴡʜᴀᴛ's ʏᴏᴜʀ ʜᴀᴘᴘɪɴᴇss ʟᴇᴠᴇʟ!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="😚 ʜᴏᴡ sɪᴍᴘ ᴀʀᴇ ʏᴏᴜ",
                input_message_content=InputTextMessageContent(
                    f"😚 ɪ ᴀᴍ {random.randint(1,100)}% sɪᴍᴘ."
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ sɪᴍᴘ ᴀʀᴇ ʏᴏᴜ",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="😌 ᴡʜᴀᴛ's ʏᴏᴜʀ ʙᴏᴏʙs sɪᴢᴇ",
                input_message_content=InputTextMessageContent(
                    f"🍒 ᴍʏ ʙᴏᴏʙs sɪᴢᴇ ɪs {random.randint(1,100)}!"
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ᴛʜᴇ sɪᴢᴇ ᴏғ ʏᴏᴜʀ ʙᴏᴏʙs",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="🧠 ʜᴏᴡ ɪǫ ᴀʀᴇ ʏᴏᴜ",
                input_message_content=InputTextMessageContent(
                    f"🧠 I ᴀᴍ {random.randint(1,150)} ɪǫ!"
                ),
                
                description="ғɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ɪq",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ sɪᴢᴇ",
                            switch_inline_query_current_chat=""
                        )]
                    ]
                )
            ),
        ],
        cache_time=1
    )

