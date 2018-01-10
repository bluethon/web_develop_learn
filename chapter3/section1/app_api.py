#!/usr/bin/env python3
# coding=utf-8
# @Date     : 2018-01-10 15:56
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

from flask import Flask, jsonify
from flask.views import MethodView


app = Flask(__name__)


class UserAPI(MethodView):

    # Flask >= 0.8, 可以使用下列定义添加装饰, 作为登录验证, 权限检查等
    decorators = []

    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'http://lorempixel.com/100/100/nature/'
        })

    def post(self):
        return 'UNSUPPORTED!'


app.add_url_rule('/user/', view_func=UserAPI.as_view('userview'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
