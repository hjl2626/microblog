#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: hjl
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: views.py.py
@time: 2015/12/18 22:51
"""
from app import app


@app.route("/")
@app.route("/index")
def index():
    return "welcome"


if __name__ == '__main__':
    pass
