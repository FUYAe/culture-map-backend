# -*- coding: utf-8 -*-
# @Time    : 2022/8/7 10:24
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : mix.py
# @Software: PyCharm 
# @Project : 24jq_backend
# @Comment :
from tortoise.models import Model
from tortoise import fields


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = None
