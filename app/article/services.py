#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
from app.article.models import ArticlesModels


class ArticlesService(object):

    @classmethod
    def submit_articles(cls, data):
        """
        创建文章
        :param data:
        :return:
        """
        return ArticlesModels.add_articles(data)

    @classmethod
    def query_article(cls, resource_id):
        """
        查询一篇文章
        :param resource_id:
        :return:
        """
        return ArticlesModels.get_article_by_id(resource_id)

    @classmethod
    def query_articles(cls, start, per_page):
        """
        查询文章列表，分页
        :param start:
        :param per_page:
        :return:
        """
        list_data = ArticlesModels.get_articles_by_page(start, per_page)
        count_data = ArticlesModels.get_articles_count()
        return list_data, count_data['count']
