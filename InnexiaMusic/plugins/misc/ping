import psutil
import time
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from InnexiaMusic import app
from InnexiaMusic.callsmusic.pytgcalls import Music
from InnexiaMusic.utils.decorators.language import language
from InnexiaMusic.misc import _boot_
from InnexiaMusic.utils.formatters import get_readable_time





### Commands
PING_COMMAND = get_command("PING_COMMAND")

# load
async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK



@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Music.ping() 
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(f"""
➽─────────────❥
{MUSIC_BOT_NAME} ɪs ʀᴇᴀᴅʏ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ 🎶
ᴡɪᴛʜ ᴘɪɴɢ ᴏғ: {resp}ms
 ╭⸻⸻⸻╮
 ◆ Uᴘᴛɪᴍᴇ ⊱ {UP}
 ◆ Cᴘᴜ ⊱ {CPU}
 ◆ Rᴀᴍ ⊱ {RAM}
 ◆ Pʏ- Tɢᴄᴀʟʟs Pɪɴɢ ⊱  {pytgping} ms
 ◆ Sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ ⊱ {DISK}
 ╰⸻⸻⸻╯
➽─────────────❥
"""
)
