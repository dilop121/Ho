from HowAllBot import app


@app.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Installation",
                input_message_content=InputTextMessageContent(
                    "Here's how to install **Pyrogram**"
                ),
                url="https://docs.pyrogram.org/intro/install",
                description="How to install Pyrogram",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Open website",
                            url="https://docs.pyrogram.org/intro/install"
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

