#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc:
"""
import json

from flask_restful import Resource
from flask import request

from app.article.services import ArticlesService
from app.tools.response import res, res_list_page
from app.config.code import ResponseCode


class ArticlesApi(Resource):
    """
    新建文章，文章列表查询
    """
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = int(request.args.get('per_page'))
        start = (int(page) - 1) * int(per_page)
        data, count = ArticlesService.query_articles(start, per_page)
        return res_list_page(code=ResponseCode.SUCCESS, msg=u'成功', data=data, count=count, current_page=page)

    @staticmethod
    def post():
        """
        example
        :return:
        """
        data = request.get_json()
        ArticlesService.submit_articles(data)
        return res(code=ResponseCode.SUCCESS, msg=u'成功')


class ArticlesSGCApi(Resource):
    """
    对单个文章的操作，查询，删除， 更新
    """

    @staticmethod
    def get(resource_id):
        """
        查询某个文章
        :return:
        """
        result = ArticlesService.query_article(resource_id)
        return res(code=ResponseCode.SUCCESS, data=result, msg=u'成功')
