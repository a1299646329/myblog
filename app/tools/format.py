#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
from sqlalchemy.engine import ResultProxy


def format_result(result_proxy):
    """
    格式化数据库查出来的结果进行字典化和列表化

    :param result_proxy: 数据库查询出来的结果集
    :return list: 结果集列表，可能为空
    """
    results = None
    if isinstance(result_proxy, ResultProxy):
        if result_proxy.rowcount:
            results = []
            for row in result_proxy:
                results.append({k: v for k, v in row.items()})
    return results
