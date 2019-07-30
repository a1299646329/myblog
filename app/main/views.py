#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc:
"""
from flask_restful import Resource
from flask import request
from app.tools.response import res
from app.config.code import ResponseCode


class BlogMainApi(Resource):
    """
    博客前端接口
    """
    @staticmethod
    def get():
        """
        example
        :return:
        """
        data = request.get_json()
        return res(code=ResponseCode.SUCCESS, msg=u'成功')
