import os

from fipper.enums import ParseMode
from git import Repo

from pyShicy import Shicy, CMD_HELP, tgbot

from . import *


@Shicy(["update"])
async def updater(client, msg):
    xx = await eor(msg, "<code>Processing...</code>")
    m = await yins.updater()
    repo = Repo.init()
    branch = repo.active_branch
    changelog, tl_chnglog = await yins.gen_chlog(
        repo, f"HEAD..upstream/{branch}"
    )
    if m:
        if changelog:
            if len(changelog) > 4096:
                await xx.edit("<b>Changelog terlalu besar, dikirim sebagai file.</b>")
                file = open("output.txt", "w+")
                file.write(changelog)
                file.close()
                await client.send_document(
                    msg.chat.id,
                    "output.txt",
                    caption=f"**Klik Tombol** `Update` **Untuk Mengupdate Userbot.**",
                    reply_to_message_id=yins.ReplyCheck(msg),
                )
                os.remove("output.txt")
        try:
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, f"in_update-{tl_chnglog}")
            await msg.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(msg),
            )
            await xx.delete()
        except BaseException as e:
            return await eod(msg, f"<b>ERROR:</b> <code>{e}</code>")
    else:
        await xx.edit(
            f'<strong>Bot Lu Udah Versi Terbaru</strong><code> Dengan </code><strong><a href="https://github.com/sip-userbot/ShicyUbot/tree/{branch}">[{branch}]</a></strong>',
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )


CMD_HELP.update(
    {"update": (
        "update",
        {
            "update" : "Gunakan Ini Untuk Mengecek Apakah Userbot Anda Versi Terbaru."
        }
    )
    }
)
