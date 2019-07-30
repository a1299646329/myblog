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
from .views import BlogMainApi

main_bp = Blueprint('interface_bp', __name__)


# Api进行管理
api = Api(main_bp)

# 首页
api.add_resource(BlogMainApi, '/main')

