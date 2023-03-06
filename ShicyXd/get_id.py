from fipper import Client
from fipper.enums.chat_type import ChatType
from fipper.errors import PeerIdInvalid
from fipper.types import Message

from pyShicy import Shicy, CMD_HELP
from pyShicy.pyrogram import eod, eor

from . import *


@Shicy(['id', 'get_id'])
async def get_id(client: Client, msg: Message):
    usr_text = ''
    xxx = await eor(msg, '**Processing...**')
    reply = msg.reply_to_message
    chats = msg.chat.id
    cmd = chiy.get_cmd(msg)
    if reply:
        if reply.from_user:
            mention = reply.from_user.mention
            ids = reply.from_user.id
            usr_text += f'**User:** {mention}\n'
            usr_text += f'**ID:** {ids}\n\n'
        else:
            mention = reply.forward_from.mention
            ids = reply.forward_from.id
            usr_text += f'**User:** {mention}\n'
            usr_text += f'**ID:** {ids}\n\n'
        usr_text += f'**Get ID By {client.me.username}'
        await xxx.edit(usr_text)
    elif cmd:
        try:
            user = await client.get_users(cmd)
        except PeerIdInvalid:
            await eod(xxx, 'Maaf saya tidak bisa menemukan pengguna...')
        mention = user.mention
        ids = user.id
        usr_text += f'**User:** {mention}\n'
        usr_text += f'**ID:** {ids}\n\n'
        usr_text += f'**Get ID By {client.me.username}'
        await xxx.edit(usr_text)
    else:
        await xxx.edit(f'**ID:** {chats}')


CMD_HELP.update(
    {'get_id': (
        'get_id',
        {
            'id <reply/id>' : 'Berikan id atau balas ke pesan pengguna untuk mendapatkan id.\n\nKetik .id untuk mendapatkan id chat saat ini.'
        }
    )
    }
)
