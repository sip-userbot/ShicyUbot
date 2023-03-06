from gpytranslate import Translator

from fipper import Client
from fipper.types import Message

from pyShicy import Shicy, CMD_HELP
from pyShicy.pyrogram import eor

from . import *



@Shicy(["tr", "tl", "translate"])
async def translate(client: Client, message: Message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        input_str = (
            message.text.split(None, 1)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        target = input_str or "id"
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await eor(
                message,
                f"<b>ERROR:</b> <code>{str(err)}</code>",
            )
            return
    else:
        input_str = (
            message.text.split(None, 2)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        text = message.text.split(None, 2)[2]
        target = input_str or "id"
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await eor(
                message,
                "<b>ERROR:</b> <code>{}</code>".format(str(err)),
            )
            return
    await eor(
        message,
        f"<i>Diterjemahkan</i>\n<b>Dari Bahasa:</b> <code>{(await trl.detect(text))}</code>\n<b>Ke Bahasa:</b> <code>{target}</code>\n\n<i>{tekstr.text}</i>",
    )


CMD_HELP.update(
    {"translate": (
        "translate",
        {
            "tr <text/reply>": "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa indonesia)",
        }
    )
    }
)