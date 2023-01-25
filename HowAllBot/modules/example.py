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
                thumb_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOun4cLQ5QmfXN9328ZzpwRocl16QoCde6PA&usqp=CAU",
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
                thumb_url = "data:image/jpeg;base64,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",
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
                thumb_url = "https://telegra.ph/file/76d0d9071a9e535234112.jpg",
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
                thumb_url = "https://telegra.ph/file/bda96c9fe01ca189b12e4.jpg",
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
                thumb_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuYuiPvPXi7po4B6HsKRdpWgFLAy3ezoLwUg&usqp=CAU",
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
                thumb_url = "https://telegra.ph/file/e8961adf69cdadab117cb.jpg",
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
                thumb_url = "https://telegra.ph/file/46df8f0e20ce85a54c127.jpg",
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
                thumb_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLe4WYVk6LFRYenU0o1ltCQ5dNxnOoeR6fyg&usqp=CAU",
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
                thumb_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMCNxxpqvhpl78aXt7lSZ8h73r_kFGrdnKAg&usqp=CAU",
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

