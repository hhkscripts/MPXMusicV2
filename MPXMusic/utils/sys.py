import time

import psutil

from MPXMusic.misc import _boot_
from MPXMusic.utils.formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    server_uptime = int(time.time() - psutil.boot_time())
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"
    DISK = f"{psutil.disk_usage('/').percent}%"
    SERVER = f"{get_readable_time(server_uptime)}"
    return UP, CPU, RAM, DISK, SERVER
