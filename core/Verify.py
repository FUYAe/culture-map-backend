# -*- coding: utf-8 -*-
# @Time    : 2022/8/7 21:41
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Verify.py
# @Software: PyCharm 
# @Project : 24jq_backend
# @Comment :
import random
from typing import Dict, List

from pydantic import BaseModel, Field

from core.Helper import random_int


class PostV(BaseModel):
    pid: str
    htmlVal: str
    rate: str
    brief: str
    longitude: int
    latitude: int
    title: str
    name: str
    password: str
    loc:str


class PictureV(BaseModel):
    pid:str
    picId: str
    base64: str = ""
    name: str
    size: str
    url1: str
    url2: str = ""
