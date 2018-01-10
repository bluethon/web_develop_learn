#!/usr/bin/env python3
# coding=utf-8
# @Date     : 2018-01-09 15:51
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

# ### 跳转和重定向

from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')


@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return f'Name: {name}; UA: {user_agent}'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return f'User: {user_id} login'
    else:
        return 'Open Login page'


@app.route('/secret/')
def secret():
    abort(401)
    print('This is never executed')


if __name__ == '__main__':
    # app.config 可用是 flask.config.ConfigAttribute在app中做了配置的代理
    # app.debug <==> app.config['DEBUG']
    app.run(host='0.0.0.0', port=9000, debug=app.debug)
