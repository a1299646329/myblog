#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: manager.py
@author: zlcao
@time: 2019/7/30 15:44
@version: 1.0
@desc: 
"""
from flask_script import Manager
from app.application import create_app
from app.config.development import DevelopmentConfig
from flask_migrate import Migrate, MigrateCommand

from app.extensions import db

monitor_app = create_app(DevelopmentConfig)

# 初始化 migrate
# 两个参数一个是 Flask 的 app，一个是数据库 db
migrate = Migrate(monitor_app, db)

# 初始化管理器
manager = Manager(app=monitor_app)

# 添加 db 命令，并与 MigrateCommand 绑定
# python manage.py db init  初始化并生成一个migrations文件夹
# python manage.py db migrate 初始化文件夹内容，升降级脚本等信息
# python manage.py db upgrade 数据库升级
# python manage.py db downgrade 数据库降级
# python manage.py db --help

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
