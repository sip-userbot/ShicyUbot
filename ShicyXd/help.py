""" Userbot help command for multi client """

from fipper import Client
from fipper.errors import PeerIdInvalid
from fipper.types import *
from random import choice
from time import sleep

from pyShicy import Shicy, CMD_HELP, tgbot
from pyShicy.pyrogram import eod, eor

from . import hndlr, chiy


@Shicy(["inline", "help"])
async def module_help(client: Client, message: Message):
    if tgbot:
        try:
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, "help")
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=chiy.ReplyCheck(message),
            )
        except PeerIdInvalid:
            succ = await client.send_message(tgbot.me.username, "/start")
            if succ:
                results = await client.get_inline_bot_results(tgbot.me.username, "help")
                await message.reply_inline_bot_result(
                    results.query_id,
                    results.results[0].id,
                    reply_to_message_id=chiy.ReplyCheck(message),
                )
            else:
                await eor(message, f"Silahkan mulai <a href='https://t.me/{tgbot.me.username}?start=True'>{tgbot.me.first_name}</a> dan ketik .help lagi")
        except BaseException as e:
            await eor(message, f"<b>ERROR:</b> <code>{e}</code>")
    else:
        args = chiy.get_cmd(message)
        if args:
            if args in CMD_HELP:
                plugs = await chiy.PluginXd(CMD_HELP, args)
                cmd_string = f"<b>PLUGIN:</b> {args.capitalize()}\n<b>HNDLR:</b> <code>{choice(hndlr)}</code>\n\n" + "".join(plugs)
                await eor(message, cmd_string)
            else:
                await eod(message, "**Modul {} Tidak diketahui**, **Silahkan Ketik {}help untuk melihat modul.**".format(args, choice(hndlr)))
        else:
            user = await client.get_me()
            string = ""
            for i in CMD_HELP:
                string += "`" + str(i)
                string += f"`\t\t\t**⍟**\t\t\t"
            xnxx = await eor(message, "🤪")
            sleep(3)
            await xnxx.edit(
                f"**[✧ Shicy Ubot ✧](https://github.com/sip-userbot/ShicyUbot)**\n"
                f"**߷ Plugins** `{len(CMD_HELP)}` **Modules**\n"
                f"**♕︎ Owner:** [{user.first_name}](tg://user?id={user.id})\n\n"
                f"**⍟**   {string}"
                f"\n\n☞  **Support** : @ShicyyXCode\n☞  **Notes** :  `{choice(hndlr)}help gcast` **Untuk Melihat Modules Lainnya**"
            )
