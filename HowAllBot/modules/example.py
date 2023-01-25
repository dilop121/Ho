import random 
from HowAllBot import app
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)


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
                            switch_inline_query=""
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="Usage",
                input_message_content=InputTextMessageContent(
                    "Here's how to use **Pyrogram**"
                ),
                url="https://docs.pyrogram.org/start/invoking",
                description="How to use Pyrogram",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Open website",
                            url="https://docs.pyrogram.org/start/invoking"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )

