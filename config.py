# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:12
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : config.py
# @Software: PyCharm 
# @Project : clitab_fastapi
import os.path
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "24jq_backend"
    DESCRIPTION: str = "24jq后端"
    # 静态文件夹
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "template")
    # 跨域请求
    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60
    # Jwt
    JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60


settings = Config()
