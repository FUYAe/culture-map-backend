# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:14
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Exception.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment : 异常处理
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def http_error_handler(_: Request, exc: HTTPException)->JSONResponse:
    """
    http异常处理
    :param _:
    :param exc:
    :return:
    """
    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "data": exc.detail
    }, status_code=exc.status_code)


async def http422_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError])->JSONResponse:
    """
    参数校验错误处理
    :param _:
    :param exc:
    :return:
    """

    return JSONResponse({
        "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "message": "参数校验错误{}".format(exc.errors()),
        "data": exc.errors()
    }, status_code=422)


class UnicornException(Exception):
    def __init__(self, code, errmsg, data=None):
        """
        失败返回格式
        :param code:
        :param errmsg:
        """
        if not data:
            data = {}
        self.code = code
        self.errmsg = errmsg
        self.data = data


async def unicorn_exception_handler(_: Request, exc: UnicornException) -> JSONResponse:
    """
    unicorn 异常处理
    :param _:
    :param exc:
    :return:
    """
    print(_.query_params)
    return JSONResponse({
        "code": exc.code,
        "message": exc.errmsg,
        "data": exc.data
    })
