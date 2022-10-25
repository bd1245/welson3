import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنج"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("جاري حساب سرعه البنج ⚡️ ")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>-›  بنج</b> `{delta_ping * 1000:.3f} ms` \n<b>-›  الوقت</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**-يتم الان تحديث البوت ع سورس ويلسون ⚡️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر","اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>منور يزميلي  🥇 {m.from_user.mention}!

🛠 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬

✛┈┉━｢ 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬 ｣━┅┈✛

👈 | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}شغل او تشغيل + اسم الاغنيه + او الرابط من يوتيوب` ]

👈 | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنيه + او الرابط من اليوتيوب` ]

✛┈┉━｢ 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬 ｣━┅┈✛

👈 | لأيقاف الصوت او الفيديو مؤقتآ  ⇦ [ `{HNDLR}اسكت` ] 

👈 | لأعاده تشغيل الصوت ⇦  [ `{HNDLR}اسكت_كمل` ]

👈 | لأيقاف الصوت  ⇦ [ `{HNDLR}اسكت` ] 

✛┈┉━｢ 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬 ｣━┅┈✛

👈 | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تحميل + اسم الاغنيه او الرابط` ]

👈 | لتحميل فيديو  ⇦  [ `{HNDLR}تحميل_فيديو + اسم الاغنيه او الرابط` ]

✛┈┉━｢ 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬 ｣━┅┈✛

👈 | لأعاده تشغيل السورس  ⇦  [ `{HNDLR}ريستارت` ]

✛┈┉━｢ 𝑾𝑬𝑳𝑺𝑶𝑵 𝑺𝑶𝑼𝑹𝑪𝑬 ｣━┅┈✛

 مطور سورس ويلسون  : @WEIS0N 

قناة السورس:  @kyany_el5as"""
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))

async def repo(client, m: Message):

    await m.delete()

    REPO = f"""

<b>👋  اهلا {m.from_user.mention}!

- للمطور : @WELS0N 

@kyany_el5as 

"""

    await m.reply(REPO, disable_web_page_preview=True)
