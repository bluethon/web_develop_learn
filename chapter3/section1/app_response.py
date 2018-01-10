#!/usr/bin/env python3
# coding=utf-8
# @Date     : 2018-01-09 16:57
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon


from flask import Flask, jsonify
from werkzeug.wrappers import Response

app = Flask(__name__)


# 负责转换
class JSONResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JSONResponse, cls).force_type(rv, environ)


app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return {'message': 'Hello World!'}


@app.route('/custom_headers')
def headers():
    # 如果返回的是一个字符串, 会用字符串数据和默认参数创建以字符串为主体, 状态码为200,
    # MIME类型是`text/html的`werkzeug.wrappers.Response`响应对象
    # return {'headers': [1, 2, 3]}, 201, [('X-Request-Id', '100')]
    # 可以直接指定状态字符串('201 CREATED1'), 替代数字的201
    return {'headers': [1, 2, 3]}, '201 CREATED1', [('X-Request-Id', '100')]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
