import base64
import os

from fastapi import File, UploadFile, Form

from core.Helper import random_str, press_img
from core.Verify import PictureV
from core.Response import success, fail
from models.picture import *


async def add_pic(pic: PictureV):
    await PicRaw.create(picid=pic.picId, base64=pic.base64, name=pic.name, size=pic.size)
    await Picture.create(picid=pic.picId, pid=pic.pid, name=pic.name, size=pic.size, url1=pic.url1, url2=pic.url2)
    return success({"status": 200})


async def get_pic(pid: str):
    res = Picture.filter(pid=pid).all()
    return success(res)


async def get_raw_pic(picid: str):
    res = PicRaw.filter(picid=picid).first()
    return success(dict(res))


def image_to_base64(data):
    image_base64_enc = base64.b64encode(data)
    image_base64_enc = str(image_base64_enc, 'utf-8')
    return image_base64_enc


async def upload_pic(file: UploadFile):
    name = random_str() + file.filename
    with open("static/assets/" + name, "wb+") as fp:
        data = await file.read()
        fp.write(data)
    press_img("static/assets/" + name, "static/pressure/" + name)

    return {
        "errno": 0,
        "data": {
            "url": f"{os.getenv('BASE_URL')}/static/assets/" + name,
            "alt": "图片",
            "href": ""
        }
    }
