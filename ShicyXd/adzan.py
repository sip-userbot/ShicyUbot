import json
import requests

from pyrogram import Client
from pyrogram.types import Message

from pyShicy import Shicy, CMD_HELP

from . import *


@Shicy(["adzan"], pass_error=True)
async def adzan_shalat(client: Client, message: Message):
    LOKASI = chiy.get_cmd(message)
    if not LOKASI:
        await message.reply("<i>Silahkan Masukkan Nama Kota Anda</i>")
        return True
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await message.reply(f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit  :</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh :</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur  :</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar  :</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib :</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya :</b> <code>{result['items'][0]['isha']}</code>
"""
    await message.reply(catresult)


CMD_HELP.update(
    {"adzan": (
        "adzan",
        {
            "adzan": "Masukkan Nama Kota Untuk Mendapatkan Jadwal Sholat Kota Anda",
        }
    )

    }
)
