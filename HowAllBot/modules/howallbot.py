import random 
from HowAllBot import app
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)



@app.on_inline_query()
async def _app(_, inline_query):
    await inline_query.answer(
    results=[
        InlineQueryResultArticle(
        title = "💋 ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
        input_message_content=InputTextMessageContent(
          f"💋 ɪ ᴀᴍ {random.randint(1,100)}% ʜᴏʀɴʏ .",)
        
        description = "ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",        
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sʜᴀʀᴇ ʏᴏᴜʀ ʜᴏʀɴʏɴᴇss! 🔥",switch_inline_query="")]]),
                                                                                                                                                                                                                                                                                                                                                            
     )],
     cache_time=1)
    
    
