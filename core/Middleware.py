# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:16
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Middleware.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :中间件
import time

from fastapi import Request
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Scope, Receive, Send, Message

from core.Helper import random_str


class Middleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        request = Request(scope, receive, send)
        if not request.session.get("session"):
            request.session.setdefault("session", random_str())

        async def send_wrapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)

        await self.app(scope, receive, send_wrapper)
