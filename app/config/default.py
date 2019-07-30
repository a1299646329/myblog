#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: __init__.py.py
@author: zlcao
@time: 2019/7/30 15:47
@version: 1.0
@desc: 
"""


class DefaultConfig(object):
    HOST = '127.0.0.1'
    PORT = '5000'
    DEBUG = False

    # 日志参数配置
    LOGGER_NAME = 'blog'
    INFO_LOG = 'blog.log'
    DEBUG_FORMATTER = "%(asctime)s %(levelname)s %(pathname)s %(funcName)s %(lineno)s %(message)s"
    INFO_FORMATTER = "%(asctime)s %(levelname)s %(pathname)s %(funcName)s %(lineno)s %(message)s"
    ERROR_FORMATTER = "%(asctime)s %(levelname)s %(pathname)s %(funcName)s lineNo=%(lineno)s processId=6%(process)d " \
                      "thread=%(thread)d  %(message)s"

    ROTATE_INTERVAL = 1  # 分割日志的时间间隔，单位天
    BACKUP_WHEN = "midnight"
    BACKUP_COUNT = 7  # 备份数

