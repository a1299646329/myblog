#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
import logging
import os

from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from app.article import articles_bp
from app.extensions import db, cors


def create_app(config_name=None):
    # 初始化,__name__代表主模块名或者包
    app = Flask(__name__)
    app.config.from_object(config_name)
    # 配置日志
    configure_logger(app)
    # 配置蓝图
    configure_blueprint(app)
    # 配置扩展插件
    configure_extensions(app)
    configure_request_common(app)
    app.logger.info('创建app成功')
    return app


def configure_blueprint(app):
    """
    配置蓝图
    :param app:
    :return:
    """
    app.register_blueprint(blueprint=articles_bp, url_prefix='/api')
    print(app.url_defaults)


def configure_logger(app):
    """
    配置日志
    :param app:
    :return:
    """
    # 设置系统默认日志记录等级
    app.logger.setLevel(logging.INFO)

    logging.getLogger(app.config['LOGGER_NAME'])
    info_formatter = logging.Formatter(app.config['INFO_FORMATTER'])
    debug_formatter = logging.Formatter(app.config['DEBUG_FORMATTER'])
    error_formatter = logging.Formatter(app.config['ERROR_FORMATTER'])

    # 控制台输出
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(debug_formatter)
    app.logger.addHandler(stream_handler)

    # 按照日期切分日志
    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    if not os.path.exists(logs_folder):
        os.mkdir(logs_folder)
    time_handler = TimedRotatingFileHandler(filename=os.path.join(logs_folder, app.config['INFO_LOG']),
                                            when=app.config['BACKUP_WHEN'], interval=app.config['ROTATE_INTERVAL'],
                                            backupCount=app.config['BACKUP_COUNT'], encoding='utf-8')
    time_handler.setLevel(logging.INFO)
    time_handler.setFormatter(info_formatter)
    app.logger.addHandler(time_handler)


def configure_extensions(app):
    """
    上下文插件扩展初始化配置
    :param app:
    :return:
    """
    db.init_app(app)  # db初始化
    cors.init_app(app)  # 允许跨域


def configure_request_common(app):

    @app.before_request
    def before_request():
        print('11111111111111')
