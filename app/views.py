#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: hjl
@license: Apache Licence 
@contact: 799728970@gmail.com
@site: 
@software: PyCharm
@file: views.py.py
@time: 2015/12/18 22:51
"""
from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


if __name__ == '__main__':
    pass
