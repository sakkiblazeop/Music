
from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 Pause 🙄",
            description=f"Pause the current stream on videochat.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 Resume 😋",
            description=f"Resume the current stream On videochat.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 Skip 🙂",
            description=f"skip the Current streaming song to next track.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 Stop 🥺",
            description="Stops the music streaming and assistant leaves vc.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 Suffle 🥴",
            description="suffle the songs in current playlist.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 Loop 🥱",
            description="loop the current playing song in same track.",
            thumb_url="https://te.legra.ph/file/84ad5652688b46626164e.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
