from PhoenixSystem import MONGO_CLIENT
from datetime import datetime
from random import choice

db = MONGO_CLIENT["Shasa"]["Main"]


async def get_data() -> dict:
    data = await db.find_one({"_id": 4})
    return data


async def add_Phoenix(sibyl: int, Phoenix: int) -> True:
    data = await get_data()
    data["data"][str(sibyl)][str(Phoenix)] = []
    data["standalone"][str(Phoenix)] = {
        "addedby": sibyl,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)


async def add_redlions(Phoenix: int, redlion: int) -> True:
    data = await get_data()
    sibyl = data["standalone"][str(Phoenix)]["addedby"]
    if sibyl == 777000:
        s = data["data"][str(Phoenix)]
        s[list(choice(s.keys()))].append([redlion])
    else:
        data["data"][str(sibyl)][str(Phoenix)].append([redlion])
    data["standalone"][str(redlion)] = {
        "addedby": Phoenix,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)
