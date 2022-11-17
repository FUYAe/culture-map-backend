# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 8:56
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : app.py
# @Software: PyCharm 
# @Project : 24jq_backend
import os.path
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from core.Router import AllRouter
from core.Middleware import Middleware
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, UnicornException, unicorn_exception_handler
from core.Init_data import init_post, init_terms

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
)


@application.get("/")
def appa():
    return {"message": "OK"}


# @application.get("/initdata")
# async def initdb():
#     await init_post()
#     await init_terms()
#     return {"message": "OK"}

# 项目启动停止事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))

# 异常处理自定义
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)
# 路由
application.include_router(AllRouter)
# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key="session",
    session_cookie="f_d",
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)
# 静态目录
application.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")))

app = application
