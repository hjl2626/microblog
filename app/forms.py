#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: hjl
@license: Apache Licence 
@contact: 799728970@gmail.com
@site: 
@software: PyCharm
@file: forms.py
@time: 2015/12/19 13:32
"""
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
