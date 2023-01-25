import random 
from HowAllBot import app
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)



@app.on_inline_query()
async def _app(_, inlinequery):
    await inlinequery.answer(
    results=[
        InlineQueryResultArticle(
        title = "💋 ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
        description = "ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
        input_message_content=InputTextMessageContent
          (f"💋 I ᴀᴍ {random.randint(1,100)}% ʜᴏʀɴʏ .",)
        ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Share your hornyness! 🔥",switch_inline_query="")]])
                                                                                                                                                                                                                                                                                                                                                            
     ],
     cache_time=1)
    
    
