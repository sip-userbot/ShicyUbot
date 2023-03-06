from fipper import Client
from fipper.errors import PeerIdInvalid
from fipper.types import Message

from pyShicy import Shicy, CMD_HELP
from pyShicy.pyrogram import eod, eor

from . import *


@Shicy(["whois", "info"])
async def check_user(client: Client, msg: Message):
    xx = await eor(msg, "**Mencari Informasi Pengguna...**")
    try:
        users = msg.text.split(" ", 1)[1]
        try:
            target = await client.get_users(users)
        except PeerIdInvalid:
            return await eod(xx, "**Maaf pengguna tidak ditemukan..**")
        name = target.first_name + " " + target.last_name if target.last_name else target.first_name
        uname = f"@{target.username}" if target.username else "⊗"
        out_str = (
            f"""
**⇒ Informasi Pengguna ⇐**
**Name:** `{name}`
**Username:** {uname}
**User ID:** `{target.id}`
**User Prem:** `{target.is_premium}`
**Profil:** [{name}](tg://user?id={target.id})
"""
        )
        await xx.edit(out_str)
    except BaseException as ex:
        return await eod(xx, ex)


CMD_HELP.update(
    {"info": (
        "info",
        {
            "info <id/username>" : "Dapatkan Informasi Pengguna.",
        }
    )
        
    }
)