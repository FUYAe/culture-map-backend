# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 18:26
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : mysql.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

DB_ORM_CONFIG = {
    "connections": {
        "base": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("BASE_HOST", "101.35.40.119"),
                "user": os.getenv("BASE_USER", "fuya"),
                "password": os.getenv("BASE_PASSWORD", "2016hyfF"),
                "port": int(os.getenv("BASE_PORT", 8081)),
                "database": os.getenv("BASE_DB", "cuturemap")
            }
        }
    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"}
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}


async def init_mysql(app: FastAPI):
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,
        add_exception_handlers=True
    )

