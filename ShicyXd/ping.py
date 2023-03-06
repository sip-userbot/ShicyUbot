import time

from datetime import datetime

from fipper import Client
from fipper.types import Message

from pyShicy import CMD_HELP, tgbot
from pyShicy.decorator import Shicy

from . import *


@Shicy(["ping"])
async def pingme(client: Client, message: Message):
    if tgbot:
        try:
            xnxx = await message.reply("<b>♡</b>")
            await xnxx.edit("<b>♡♡<b>")
            await xnxx.edit("<b>♡♡♡</b>")
            await xnxx.edit("<b>♡♡♡♡</b>")
            await xnxx.edit("<b>♡♡♡♡♡</b>")
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, f"ping")
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(message),
            )
            await xnxx.delete()
        except BaseException as e:
            await eod(xnxx, f"<b>ERROR:</b> <code>{e}</code>")


CMD_HELP.update(
    {"ping": (
        "ping",
        {
            "ping": "Check Ping Your Bot.",
        }
    )
    }
)
