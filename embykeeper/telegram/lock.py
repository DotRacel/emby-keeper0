import asyncio

from cachetools import TTLCache

ocrs = TTLCache(maxsize=1024, ttl=3600)  # spec: (DdddOcr, bool)
ocrs_lock = asyncio.Lock()

misty_locks = {}  # uid: lock
