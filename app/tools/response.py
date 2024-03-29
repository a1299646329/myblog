#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc:
"""
from app.config.code import ResponseCode
from flask import jsonify


def res(code=ResponseCode.SUCCESS, msg='成功', data=None):
    """
    通用返回
    :param code:
    :param msg:
    :param data:
    :return:
    """
    result = {'status': code, 'message': msg}
    if data:
        result['data'] = data
    return jsonify(result)


def res_list_page(code=ResponseCode.SUCCESS, msg='成功', data=None, count=None, current_page=None, per_page=20):
    """
    分页返回类型
    :param code:
    :param msg:
    :param data:
    :param count: 数据总数
    :param current_page:  当前页
    :param per_page: 每页多少条数据
    :return:
    """
    result = {'status': code, 'message': msg}
    if data:
        result['data'] = data
    if count is not None:
        result['count'] = count
    if current_page is not None:
        result['current_page'] = current_page
    if per_page is not None:
        result['per_page'] = per_page
    return jsonify(result)
