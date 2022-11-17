from tortoise.fields import *
from models.mix import TimestampMixin


class Post(TimestampMixin):
    pid = CharField(max_length=64)
    title = CharField(null=True, max_length=120, description="标题")
    name = CharField(null=True, max_length=120, description="地名")
    htmlVal = TextField(null=True, description="正文")


class PostLight(TimestampMixin):
    pid = CharField(null=True, max_length=64)
    name = CharField(null=True, max_length=120, description="地名")
    rate=IntField(null=True, description="推荐指数")
    brief=TextField(null=True, description="简介")
    longitude=IntField(null=True, description="经度")
    latitude=IntField(null=True, description="纬度")
    loc=TextField(null=True, description="地点")
