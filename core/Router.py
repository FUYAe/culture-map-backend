# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 14:50
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Router.py
# @Software: PyCharm 
# @Project : clit-ab_fastapi
# @Comment :
from fastapi import APIRouter
from api.base import ApiRouter

AllRouter = APIRouter(prefix="/api")
AllRouter.include_router(ApiRouter)
