#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file: application.py
@author: zlcao
@time: 2019/7/30 15:48
@version: 1.0
@desc: 
"""
# 接口日志接收
interface_log_accept = {
    "type": "object",
    "properties": {
        "regionNo":  {
            "type": "string",
            "minLength": 1
        },
        "orgNo": {
            "type": "string",
            "minLength": 1
        },
        "groupNo": {
            "type": "string",
            "minLength": 1
        },
        "posId": {
            "type": "string",
            "minLength": 1
        },
        "monitorTypeDataDTOList": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "monitorDetailDataDTOList": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "status": {
                                    "type": "string",
                                    "minLength": 1
                                },
                                "useTime": {
                                    "type": "string",
                                    "minLength": 1
                                },
                                "remark": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string",
                                    "minLength": 1,
                                    "maxLength": 512
                                },
                                "code": {
                                    "type": "string",
                                    "minLength": 1
                                },
                                "occurTime": {
                                    "type": "string",
                                    "minLength": 1
                                },
                                "reversed": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }

        }
        },
    "required": [
        "regionNo", "orgNo"
    ]
}

# 接口日志查询
interface_log_query = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "region_no":  {
            "type": "string"
        },
        "org_no": {
            "type": "string"
        },
        "pos_no": {
            "type": "string"
        },
        "url": {
            "type": "string"
        },
        "net_status": {
            "type": "string"
        },
        "use_time": {
            "type": "string"
        },
        "page": {
            "type": "integer"
        }
    }
}
