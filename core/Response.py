# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 20:50
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Response.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :
def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(data=None, msg='请求成功'):
    """成功返回格式"""
    return base_response(200, msg, data)


def fail(code=-1, msg='请求失败', data=None):
    """失败返回格式"""
    return base_response(code, msg, data)