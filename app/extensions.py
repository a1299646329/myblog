#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: extensions.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()
cors = CORS()