#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
from functools import wraps

from flask import request, jsonify
from jsonschema import Draft4Validator

from app.config.code import ResponseCode
from app.tools.response import res


def validate_schema(schema):
    validator = Draft4Validator(schema)

    def wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            input = request.get_json(force=True)
            errors = [error.message for error in validator.iter_errors(input)]
            if errors:
                # response = jsonify(dict(success=False,
                #                         message="invalid input",
                #                         errors=errors))
                response = res(code=ResponseCode.ARGS_ERROR, msg='invalid input' + ','.join(errors))
                response.status_code = 406
                return response
            else:
                return fn(*args, **kwargs)
        return wrapped
    return wrapper