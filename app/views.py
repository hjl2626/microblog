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
import logging

from app import lm, db
from app.models import User
from flask import flash
from flask import request
from flask.ext.login import login_user, current_user, login_required, logout_user


@lm.user_loader
def load_user(id):
    print("\nuserload"+id)
    return User.query.get(int(id))


from flask import render_template, redirect, session, url_for, g
from app import app, oid
from .forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    # print("login\n"+repr(g.user)+'\n')
    # if g.user is not None:
    #     return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    print('\nbefore_request:' + str(current_user)+"\n")
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    print("\nindex+"+repr(g.user)+'\n')
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
