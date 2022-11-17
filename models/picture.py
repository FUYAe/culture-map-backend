from tortoise.fields import *
from models.mix import TimestampMixin


# const picRaw={
#     picid:"",
#     name:"",
#     base64:""
# }
# const  pic={
#     picid:"",
#     postid:"",
#     name:"",
#     url1:"",
#     url2:""
# }

class PicRaw(TimestampMixin):
    picid = CharField(max_length=64)
    base64 = TextField(null=True)
    name = CharField(null=True, max_length=120)
    size = IntField(null=True)


class Picture(TimestampMixin):
    pid = CharField(max_length=64)
    picid = CharField(max_length=64)
    name = CharField(null=True, max_length=120)
    size = IntField(null=True)
    url1 = TextField(null=True)
    url2 = TextField(null=True)


class UpPic(TimestampMixin):
    pictureid = CharField(max_length=64)
    data = BinaryField(null=True)
