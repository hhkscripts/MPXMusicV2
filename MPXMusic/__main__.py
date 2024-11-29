import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MPXMusic import LOGGER, app, userbot
from MPXMusic.core.call import MPX
from MPXMusic.misc import sudo
from MPXMusic.plugins import ALL_MODULES
from MPXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MPXMusic.plugins" + all_module)
    LOGGER("MPXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await MPX.start()
    try:
        await MPX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("MPXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await MPX.decorators()
    LOGGER("MPXMusic").info("MPXMusic Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MPXMusic").info("Stopping MPX Music Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
