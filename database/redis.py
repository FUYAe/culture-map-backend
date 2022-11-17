# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 20:54
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : redis.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :
import os

import aioredis
from aioredis import Redis


async def sys_cache() -> Redis:
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f"redis://{os.getenv('CACHE_HOST', '127.0.0.1')}:{os.getenv('cache_port', 6379)}",
        db=os.getenv("CACHE_DB", 0),
        encoding="utf-8",
        decode_responses=True
    )
    return Redis(connection_pool=sys_cache_pool)
