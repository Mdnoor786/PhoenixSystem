from telethon.utils import resolve_invite_link
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from PhoenixSystem.plugins.Mongo_DB.tree import add_Phoenix, add_redlions, get_data
from PhoenixSystem import REDLIONS, PHOENIX, SHASA, session
from PhoenixSystem import System, system_cmd
from PhoenixSystem import PHOENIX_LOGS

from datetime import datetime
from urllib.parse import urlparse, urlunparse
import heroku3
import os
import re
import json

try:
    from PhoenixSystem import HEROKU_API_KEY, HEROKU_APP_NAME

    heroku_conn = heroku3.from_key(HEROKU_API_KEY)
    app = heroku_conn.app(HEROKU_APP_NAME)
    config = app.config()
    HEROKU = True
except BaseException:
    HEROKU = False

json_file = os.path.join(os.getcwd(), "PhoenixSystem/elevated_users.json")


@System.on(system_cmd(pattern=r"addenf", allow_Phoenix=True))
async def addenf(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        if replied:
            u_id = replied.sender.id
        else:
            return
    else:
        u_id = event.text.split(" ", 2)[1]
        try:
            u_id = (await System.get_entity(u_id)).id
        except BaseException:
            await event.reply(
                "I haven't interacted with that user! Meh, Will add them anyway"
            )
    if u_id in REDLIONS:
        await System.send_message(event.chat_id, "That person is already Redlion!")
        return
    if HEROKU:
        config["REDLIONS"] = os.environ.get("REDLIONS") + " " + str(u_id)
    else:
        with open(json_file, "r") as file:
            data = json.load(file)
        data["REDLIONS"].append(u_id)
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        await System.send_message(event.chat_id, "Added to redlions, Restarting...")
        if not event.from_id.user_id in SHASA:
            await add_redlions(event.from_id.user_id, u_id)
        await System.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    if not event.from_id.user_id in SHASA:
        await add_redlions(event.from_id.user_id, u_id)
    await System.send_message(
        event.chat_id, f"Added [{u_id}](tg://user?id={u_id}) to Redlions"
    )


@System.on(system_cmd(pattern=r"rmenf", allow_Phoenix=True))
async def rmenf(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        u_id = replied.sender.id
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Invalid ID/Username!")
    u_id = int(u_id)
    if u_id not in REDLIONS:
        await System.send_message(event.chat_id, "Is that person even a Redlion?")
        return
    if HEROKU:
        str(u_id)
        ENF = os.environ.get("REDLIONS")
        if ENF.endswith(u_id):
            config["REDLIONS"] = ENF.strip(" " + str(u_id))
        elif ENF.startswith(u_id):
            config["REDLIONS"] = ENF.strip(str(u_id) + " ")
        else:
            config["REDLIONS"] = ENF.strip(" " + str(u_id) + " ")
    else:
        with open(json_file, "r") as file:
            data = json.load(file)
        data["REDLIONS"].remove(u_id)
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        await System.send_message(
            event.chat_id, "Removed from redlions, Restarting..."
        )
        await System.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    await System.send_message(
        event.chat_id, f"Removed [{u_id}](tg://user?id={u_id}) from Redlions"
    )


@System.on(system_cmd(pattern=r"redlions", allow_Phoenix=True))
async def listuser(event) -> None:
    msg = "Redlions:\n"
    for z in REDLIONS:
        try:
            user = await System.get_entity(z)
            msg += f"•[{user.first_name}](tg://user?id={user.id}) | {z}\n"
        except BaseException:
            msg += f"•{z}\n"
    await System.send_message(event.chat_id, msg)


@System.on(system_cmd(pattern=r"join", allow_Phoenix=True, allow_redlion=True))
async def join(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    private = re.match(
        r"(https?://)?(www\.)?t(elegram)?\.(dog|me|org)/joinchat/(.*)", link
    )
    if private:
        await System(ImportChatInviteRequest(private.group(5)))
        await System.send_message(event.chat_id, "Joined chat!")
        await System.send_message(
            PHOENIX_LOGS,
            f"{(await event.get_sender()).first_name} made Phoenix join {private.group(5)}",
        )
    else:
        await System(JoinChannelRequest(link))
        await System.send_message(event.chat_id, "Joined chat!")
        await System.send_message(
            PHOENIX_LOGS,
            f"{(await event.get_sender()).first_name} made Phoenix join {link}",
        )


@System.on(system_cmd(pattern=r"addins"))
async def addins(event) -> None:
    if event.reply:
        replied = await event.get_reply_message()
        if replied:
            u_id = replied.sender.id
        else:
            return
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Ivalid ID/Username!")
        return
    if u_id in PHOENIX:
        await System.send_message(event.chat_id, "That person is already an Phoenix!")
        return
    if HEROKU:
        config["PHOENIX"] = os.environ.get("PHOENIX") + " " + str(u_id)
    else:
        with open(json_file, "r") as file:
            data = json.load(file)
        data["PHOENIX"].append(u_id)
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        await System.send_message(event.chat_id, "Added to Phoenix, Restarting...")
        await add_Phoenix(event.from_id.user_id, u_id)
        await System.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    await add_Phoenix(event.from_id.user_id, u_id)
    await System.send_message(
        event.chat_id, f"Added [{u_id}](tg://user?id={u_id}) to PHOENIX"
    )


@System.on(system_cmd(pattern=r"rmins"))
async def rmins(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        u_id = replied.sender.id
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Ivalid ID/Username!")
    if u_id not in PHOENIX:
        await System.send_message(event.chat_id, "Is that person even an Phoenix?")
        return
    u_id = str(u_id)
    if HEROKU:
        ENF = os.environ.get("PHOENIX")
        if ENF.endswith(u_id):
            config["PHOENIX"] = ENF.strip(" " + str(u_id))
        elif ENF.startswith(u_id):
            config["PHOENIX"] = ENF.strip(str(u_id) + " ")
        else:
            config["PHOENIX"] = ENF.strip(" " + str(u_id) + " ")
    else:
        with open(json_file, "r") as file:
            data = json.load(file)
        data["PHOENIX"].remove(u_id)
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        await System.send_message(
            event.chat_id, "Removed from Phoenix, Restarting..."
        )
        await System.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    await System.send_message(
        event.chat_id,
        f"Removed Phoenix status of [{u_id}](tg://user?id={u_id}), Now that user is a mere redlions.",
    )


@System.on(system_cmd(pattern=r"info ", allow_Phoenix=True))
async def info(event) -> None:
    data = (await get_data())["standalone"]
    if not event.text.split(" ", 1)[1] in data.keys():
        return
    u = event.text.split(" ", 1)[1]
    msg = f"User: {u}\n"
    msg += f"Added by: {data[u]['addedby']}\n"
    msg += f"Timestamp: {datetime.fromtimestamp(data[u]['timestamp']).strftime('%d/%m/%Y - %H:%M:%S')}(`{data[u]['timestamp']}`)"
    await event.reply(msg)


@System.on(system_cmd(pattern=r"Phoenix", allow_Phoenix=True))
async def listuserI(event) -> None:
    msg = "Phoenix:\n"
    for z in PHOENIX:
        try:
            user = await System.get_entity(z)
            msg += f"•[{user.first_name}](tg://user?id={user.id}) | {z}\n"
        except BaseException:
            msg += f"•{z}\n"
    await System.send_message(event.chat_id, msg)


@System.on(system_cmd(pattern=r"resolve", allow_Phoenix=True))
async def resolve(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    match = re.match(
        r"(https?://)?(www\.)?t(elegram)?\.(dog|me|org)/joinchat/(.*)", link
    )
    if match:
        try:
            data = resolve_invite_link(match.group(5))
        except BaseException:
            await System.send_message(
                event.chat_id, "Couldn't fetch data from that link"
            )
            return
        await System.send_message(
            event.chat_id,
            f"Info from hash {match.group(5)}:\n**Link Creator**: {data[0]}\n**Chat ID**: {data[1]}",
        )


@System.on(system_cmd(pattern=r"leave"))
async def leave(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    c_id = re.match(r"-(\d+)", link)
    if c_id:
        await System(LeaveChannelRequest(int(c_id.group(0))))
        await System.send_message(
            event.chat_id, f"Phoenix has left chat with id[-{c_id.group(1)}]"
        )
    else:
        await System(LeaveChannelRequest(link))
        await System.send_message(event.chat_id, f"Phoenix has left chat[{link}]")


@System.on(system_cmd(pattern=r"get_redirect ", allow_Phoenix=True))
async def redirect(event) -> None:
    try:
        of = event.text.split(" ", 1)[1]
    except BaseException:
        return
    of = urlunparse(urlparse(of, "https"))
    async with session.get(of) as r:
        url = r.url
    await System.send_message(event.chat_id, f"URL: {url}")


help_plus = """
Help!
`addenf` - Adds a user as an redlion.
Format : addenf <user id / as reply>
`rmenf` - Removes a user from redlions.
Format : rmenf <user id / as reply>
`redlions` - Lists all redlions.
`addins` - Adds a user as an Phoenix.
Format : addins <user id / as reply>
`rmins` - Removes a user from Phoenix.
Format : rmins <user id / as reply>
`Phoenix` - Lists all Phoenix.
`join` - Joins a chat.
Format : join <chat username or invite link>
`leave` - Leaves a chat.
Format : leave <chat username or id>
`resolve` - Resolve a chat invite link.
Format : resolve <chat invite link>
`get_redirect` - Follows redirect of a link.
Format : get_redirect <URL>
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addenf` or `?addenf` or `.addenf`
"""

__plugin_name__ = "extras"
