from PhoenixSystem import (
    System,
    system_cmd,
    make_collections,
    PHOENIX,
    REDLIONS,
    PHOENIX_LOGS,
)
from PhoenixSystem.strings import on_string
import logging
import importlib
import asyncio
import time

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

from PhoenixSystem.plugins import to_load

HELP = {}
IMPORTED = {}
FAILED_TO_LOAD = {}

for load in to_load:
    try:
        imported = importlib.import_module("PhoenixSystem.plugins." + load)
        if not hasattr(imported, "__plugin_name__"):
            imported.__plugin_name__ = imported.__name__

        if not imported.__plugin_name__.lower() in IMPORTED:
            IMPORTED[imported.__plugin_name__.lower()] = imported

        if hasattr(imported, "help_plus") and imported.help_plus:
            HELP[imported.__plugin_name__.lower()] = imported
    except Exception as e:
        print(f"Error while loading plugin: {load}")
        print("------------------------------------")
        print(e)
        FAILED_TO_LOAD[load] = e
        print("------------------------------------")


@System.on(system_cmd(pattern=r"osinfo", allow_redlion=True))
async def status(event):
    msg = await event.client.send_file(event.chat_id, file="https://telegra.ph/file/325d571e977aff9ae5f4d.mp4", caption="Connecting to Phoenix Systems", reply_to=event)
    time.sleep(1)
    await msg.edit("Initialising ■□□□□□")
    time.sleep(1)
    await msg.edit("Initialising ■■□□□□")
    time.sleep(1)
    await msg.edit("Initialising ■■■□□□")
    time.sleep(1)
    await msg.edit("Initialising ■■■■□□")
    time.sleep(1)
    await msg.edit("Initialising ■■■■■□")
    time.sleep(1)
    await msg.edit("Initialising ■■■■■■")
    time.sleep(1)
    await msg.edit("🔰🔰VERIFIED🔰🔰")
    time.sleep(2)
    sender = await event.get_sender()
    user_status = "Phoenix" if sender.id in PHOENIX else "Redlion"
    time.sleep(1)
    await msg.edit(on_string.format(Redlion=user_status, name=sender.first_name))


@System.on(system_cmd(pattern="Phoenix stats"))
async def stats(event):
    msg = f"Processed {System.processed} messages since last restart."
    msg += f"\n{len(REDLIONS)} Redlions & {len(PHOENIX)} Phoenix"
    g = 0
    async for d in event.client.iter_dialogs(limit=None):
        if d.is_channel and not d.entity.broadcast:
            g += 1
        elif d.is_group:
            g += 1
    msg += f"\nModerating {g} Groups"
    await event.reply(msg)


@System.on(system_cmd(pattern=r"help", allow_slash=False, allow_Phoenix=True, allow_redlion=True))
async def send_help(event):
    try:
        help_for = event.text.split(" ", 1)[1].lower()
    except IndexError:
        msg = "List of plugins with help text:\n"
        for x in HELP.keys():
            msg += f"`{x.capitalize()}`\n"
        await event.reply(msg)
        return
    if help_for in HELP:
        await event.reply(HELP[help_for].help_plus)
    else:
        return


async def main():
    try:
        await make_collections()
        me = await System.bot.get_me()
        System.bot.id = me.id
    except Exception as e:
        FAILED_TO_LOAD["main"] = e
    await System.start()
    await System.catch_up()
    if FAILED_TO_LOAD:
        msg = "Few plugins failed to load:"
        for plugin in FAILED_TO_LOAD:
            msg += f"\n**{plugin}**\n\n`{FAILED_TO_LOAD[plugin]}`"
        await System.send_message(PHOENIX_LOGS, msg)
    else:
        await System.send_message(PHOENIX_LOGS, "I'm up!")
    await System.run_until_disconnected()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main()) 