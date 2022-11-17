# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 9:18
# @Author  : fuya
# @Email    : f2956903402@gmail.com
# @File    : Helper.py
# @Software: PyCharm 
# @Project : clitab_fastapi
# @Comment :工具函数
import copy
import datetime
import hashlib
import json
import math
import os
import random
import uuid
from xpinyin import Pinyin
import tinify

tinify.key = "Z2vz2yCsajQb4bCQTVNEOtSfbpyMww8b9w"
pinyin = Pinyin()
tinify.proxy = "http://user:pass@192.168.0.1:8080"
from PIL import Image


def get_pinyin(chinese: str, sep=""):
    return pinyin.get_pinyin(chinese, splitter="")


def random_str():
    """
    唯一随机字符串
    :return: str
    """

    only = hashlib.md5(str(uuid.uuid1()).encode(encoding="UTF-8")).hexdigest()
    return str(only)


def random_int(long: int = 6):
    return random.randint(pow(10, long - 1), pow(10, long) - 1)


def handle_dict(data: dict):
    new_data = copy.deepcopy(data)
    for key, val in data.items():
        if type(val) == datetime.datetime:
            new_data[key] = str(val)
        if type(val) == dict:
            new_data[key] = handle_dict(val)

        if type(val) == list:
            new_data[key] = handle_list(val)
    return new_data


def handle_list(data: list):
    new_data = copy.deepcopy(data)
    for val in data:
        if type(val) == datetime.datetime:
            new_data.remove(val)
            new_data.append(str(val))
        if type(val) == dict:
            new_data.remove(val)
            new_data.append(handle_dict(val))
        if type(val) == list:
            new_data.remove(val)
            new_data.append(handle_list(val))
    return new_data


def orm2json(data):
    new_data = None
    if type(data) == list:
        new_data = handle_list(data)
    elif type(data) == dict:
        new_data = handle_dict(data)
    return json.dumps({"data": new_data})


def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile


def compress_image(infile, outfile='', mb=150, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)


def resize_image(infile, outfile='', x_s=676):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)


def press_img(inf,outf):
    compress_image(inf,outf)
    resize_image(inf,outf)