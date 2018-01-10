#!/usr/bin/env python3
# coding=utf-8
# @Date     : 2018-01-09 15:27
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

# ### 构造URL

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/item/1/')
def item(id):
    pass


with app.test_request_context():
    print(url_for('item', id='1'))
    print(url_for('item', id='2', next='/'))
