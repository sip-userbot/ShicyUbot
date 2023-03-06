import time

from fipper import Client, __version__ as fip_ver
from fipper.errors import PeerIdInvalid
from fipper.types import Message
from platform import python_version

from pyShicy import __version__, shicy_ver
from pyShicy import CMD_HELP, HOSTED_ON, adB, tgbot
from pyShicy.decorator import Shicy
from pyShicy.pyrogram import eor


from . import *


@Shicy(["alive", "chiy"])
async def aliveme(client: Client, message: Message):
    if tgbot:
        try:
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, f"alive")
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(message),
            )
        except PeerIdInvalid:
            succ = await client.send_message(tgbot.me.username, "/start")
            if succ:
                results = await client.get_inline_bot_results(tgbot.me.username, f"alive")
                await message.reply_inline_bot_result(
                    results.query_id,
                    results.results[0].id,
                    reply_to_message_id=yins.ReplyCheck(message),
                )
            else:
                await eor(message, f"Silahkan mulai <a href='https://t.me/{tgbot.me.username}?start=True'>{tgbot.me.first_name}</a> dan ketik .help lagi")
        except BaseException as e:
            await eor(message, f"<b>ERROR:</b> <code>{e}</code>")
    else:
        chat_id = message.chat.id
        user = await client.get_me()
        output = (
           f"**Shicy Ubot**\n"
           f"  <b>Status : </b>**𝘗𝘙𝘌𝘔𝘐𝘜𝘔**\n"
           f"   <b>Master :</b> {client.me.mention} \n"
           f"   <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
           f"   <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
           f"   <b>Bot Uptime :</b> <code>{uptime}</code>\n")
        )
        await message.delete()
        try:
            if var.ALIVE_PIC:
                endsw = (".mp4", ".gif")
                if var.ALIVE_PIC.endswith(endsw):
                    await client.send_video(chat_id=chat_id, video=var.ALIVE_PIC, caption=output)
                else:
                    await client.send_photo(chat_id=chat_id, photo=var.ALIVE_PIC, caption=output)
            else:
                await message.reply_text(output)
        except BaseException as xd:
            await message.reply(xd)


CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Chech Your Userbot.",
        }
    )
    }
)
