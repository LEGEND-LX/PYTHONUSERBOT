from telethon import events
from userbot.utils import admin_cmd
import asyncio


@bot.on(admin_cmd(pattern="undlt"))
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await bot.get_admin_log(event.chat_id,limit=5, search="", edit=False, delete=True)
        for i in a:
          await event.reply(i.original.action.message)
    else:
        await event.edit("You need administrative permissions in order to do this command")
        await asyncio.sleep(3)
        await event.delete()

from . import *


CmdHelp("undlt").add_command(
  'undlt', None, 'You need administrative permissions in order to do this command u can see last 5 message'
).add()
