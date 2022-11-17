# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:10
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : base.py.py
# @Software: PyCharm 
# @Project : clitab_fastapi
from fastapi import APIRouter
from database.redis import sys_cache
from api.picture import upload_pic,add_pic,get_pic
from api.post import add_post, get_post, get_light_post

ApiRouter = APIRouter(prefix="/culture", tags=["Api路由"])

# pic
ApiRouter.post("/upload_pic")(upload_pic)
ApiRouter.post("/add_pic")(add_pic)
ApiRouter.post("/get_pic")(get_pic)

@ApiRouter.post("/get")
async def app():
    print(await (await sys_cache()).get("aa"))
    return ""


# post
ApiRouter.post("/add_post")(add_post)
ApiRouter.post("/get_post")(get_post)
ApiRouter.post("/get_light_post")(get_light_post)
