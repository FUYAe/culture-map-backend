# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:13
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Events.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :fastapi事件监听
from typing import Callable
from fastapi import FastAPI

from database.mysql import init_mysql
from database.redis import sys_cache


def startup(app: FastAPI):
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        await init_mysql(app)
        app.state.cache = await sys_cache()
        print("========项目:{} 启动完成========".format(app.title))

    return app_start


def stopping(app: FastAPI) -> Callable:
    """
       FastApi 停止事件
       :param app: FastAPI
       :return: app_stop
       """

    async def app_stop() -> None:
        print("========== 项目{} 已停止==========".format(app.title))

    return app_stop
