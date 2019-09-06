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

from sqlalchemy import text

from app.extensions import db


class ArticlesModels(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    author = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    views = db.Column(db.String(20), default='0')

    @classmethod
    def add_articles(cls, args):
        """
        新增一篇文章
        :param args:
        :return:
        """
        sql = """insert into articles (author, title, content) values (:author, :title, :content)"""
        data = db.session.execute(text(sql), args)
        _id = data.lastrowid
        db.session.commit()
        return _id

    @classmethod
    def get_article_by_id(cls, resource_id):
        """
        获取一篇文章
        :param resource_id:
        :return:
        """
        sql = """select id, author, title, content, views from articles where id =:resource_id"""
        data = db.session.execute(text(sql), {'resource_id': resource_id})
        data = [(dict(row.items())) for row in data]
        return data

    @classmethod
    def get_articles_by_page(cls, start, per_page):
        """
        按页获取文章列表
        :param start:
        :param per_page:
        :return:
        """
        sql = """select id, author, title from articles limit :start, :per_page"""
        data = db.session.execute(text(sql), {'start': start, 'per_page': per_page})
        data = [(dict(row.items())) for row in data]
        return data

    @classmethod
    def get_articles_count(cls):
        """
        获取文章数量
        :return:
        """
        sql = """select count(id) as count from articles"""
        data = db.session.execute(text(sql))
        for row in data:
            data = dict(row.items())
        return data
