#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: hjl
@license: Apache Licence 
@contact: 799728970@gmail.com
@site: 
@software: PyCharm
@file: test.py
@time: 2015/12/19 15:26
"""

from app import db, models
from app.models import User

if __name__ == '__main__':
    u = models.User(nickname='john', email='john@email.com')
    db.session.add(u)

    u = models.User(nickname='susan', email='susan@email.com')
    db.session.add(u)

    db.session.commit()
