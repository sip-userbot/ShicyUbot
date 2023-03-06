import os
import time

from datetime import datetime
from fipper import Client
from fipper.types import *

from config import *

from pyShicy import CMD_HELP, StartTime
from pyShicy.assistant import inline

from . import *


handler = f"{Var.HNDLR[0]} {Var.HNDLR[1]} {Var.HNDLR[2]} {Var.HNDLR[3]} {Var.HNDLR[4]} {Var.HNDLR[5]}"

def help_string():
    text = f"""
<b>Help Module</b>
    <b>Prefixes:</b> <code>{handler}</code>
"""

    return text


def update_string():
    teks = f'''
<b>Tersedia Pembaruan Untuk [{branch}]</b>

<b>•</b> Klik Update Untuk Memperbarui [{branch}]
<b>•</b> Klik Changelog Untuk Melihat Pembaruan
'''
    
    return teks


@inline(pattern="help")
async def inline_result(_, inline_query):
    rslts=[
        (
            InlineQueryResultArticle(
                title="Shicy Ubot!",
                reply_markup=InlineKeyboardMarkup(
                    chiy.HelpXd(0, CMD_HELP, "xd")
                ),
                input_message_content=InputTextMessageContent(help_string()),
            )
        )
    ]
    await inline_query.answer(
        rslts,
        cache_time=0
    )


@inline(pattern="paste", client_only=True)
async def inline_result(_, iq):
    query = iq.query
    ok = query.split("-")[1]
    rslts=[
        (
            InlineQueryResultArticle(
                title="Paste Shicy Ubot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="• SpaceBin •",
                                url=f"https://spaceb.in/{ok}",
                            ),
                            InlineKeyboardButton(
                                text="• Raw •",
                                url=f"https://spaceb.in/api/v1/documents/{ok}/raw",
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent("Pasted to Spacebin 🌌"),
            )
        )
    ]
    await iq.answer(
        rslts,
        cache_time=0
    )


@inline(pattern="alive", client_only=True)
async def inline_result(_: Client, iq):
    alive = await chiy.alive('plugins-tab')
    await iq.answer(
        alive,
        cache_time=0
    )



@inline(pattern="ping", client_only=True)
async def inline_result(_: Client, iq):
    start = datetime.now()
    uptime = await chiy.get_readable_time((time.time() - StartTime))
    time.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    out_ping = (
        f"<b>✧ sʜɪᴄʏ Uʙᴏᴛ ✧</b>\n\n"
        f"<b>✧ Pɪɴɢᴇʀ :</b> <code>{duration}ms</code>\n"
        f"<b>✧ Uᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>"
    )
    ping_result = [
        (
            InlineQueryResultArticle(
                title="Ping Shicy Ubot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="• Help •",
                                callback_data="plugins-tab",
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent(out_ping),
            )
        )
    ]
    await iq.answer(
        ping_result,
        cache_time=0,
    )



@inline(pattern='in_update', client_only=True)
async def inline_update(client, iq):
    query = iq.query
    ok = query.split("-")
    update_results = [
        (
            InlineQueryResultArticle(
                title='Update Shicy Ubot!',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text='• Update •',
                                callback_data='update_now',
                            ),
                            InlineKeyboardButton(
                                text='• Changelog •',
                                callback_data='changelog',
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text='• Close •',
                                callback_data='close',
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent(update_string()),
            )
        )
    ]
    await iq.answer(
        update_results,
        cache_time=0,
    )


@inline(pattern='pmpermit', client_only=True)
async def inline_pmpermit(_, iq):
    query = iq.query
    ids = query.split("_")[1]
    xnxx = await chiy.inline_pmpermit(ids)
    await iq.answer(
        xnxx,
        cache_time=0,
    )
