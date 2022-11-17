from core.Verify import PostV
from core.Response import success, fail
from models.post import *


async def add_post(post: PostV):

    await Post.create(pid=post.pid, title=post.title, name=post.name, htmlVal=post.htmlVal)
    await PostLight.create(pid=post.pid, name=post.name, rate=post.rate, brief=post.brief, longitude=post.longitude,
                               latitude=post.latitude)

    return success({"pid": post.pid})


async def get_post(pid: str):
    res = Post.filter(pid=pid).first()
    return success(dict(res))


async def get_light_post(pid: str):
    res = PostLight.filter(pid=pid).first()
    return success(dict(res))
