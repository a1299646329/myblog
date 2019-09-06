#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: __init__.py.py
@author: zlcao
@time: 2019/7/30 15:47
@version: 1.0
@desc: 
"""
from app.config.default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8'


    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    # 这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False

