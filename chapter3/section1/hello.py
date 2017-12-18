#!/usr/bin/env python3
# encoding: utf-8
# @Date     : 2017-12-15 14:22
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

from flask import Flask

# app, Flask实例, 接收包或者模块名字作为参数
# flask.helpers.get_root_path 通过参数获得根目录
# 来获得静态文件和模板文件的目录
app = Flask(__name__)

# http://flask.pocoo.org/docs/latest/config/#builtin-configuration-values
# 配置 硬编码
app.config['DEBUG'] = True
# app.config 是flask.config.Config类的实例, 继承自Python的dict,
# 所以可以用 update 方式
app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)


# app.route 会将URL和执行的视图函数的关系保存到 app.url_map 属性上
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 服务器启动后, 会调用 werkzeug.serving.run_simple 进入轮询,
    # 默认使用单进程单线程的 werkzeug.serving.BaseWSGIServer 处理请求,
    # 实际还是使用标准库 BaseHTTPServer.HTTPServer,
    # 通过 select.select 做0.5s的 'while True' 的事件轮询
    # 其他的werkzeug自带类型还包括 ThreadedWSGIServer 和 ForkingWSGIServer
    app.run(host='0.0.0.0', port=9000, debug=True)
