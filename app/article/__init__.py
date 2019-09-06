#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
from flask import Blueprint
from flask_restful import Api
from .views import ArticlesApi
from .views import ArticlesSGCApi

articles_bp = Blueprint('article_bp', __name__)


# Api进行管理
api = Api(articles_bp)  # , prefix='article'

# # 首页
# api.add_resource(BlogMainApi, '/list')

# # 首页
# api.add_resource(BlogMainApi, '/<int:article_id>')

# 首页
api.add_resource(ArticlesApi, '/articles')

# 查询某个文章
api.add_resource(ArticlesSGCApi, '/articles/<int:resource_id>')