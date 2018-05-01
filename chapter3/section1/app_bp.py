#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-29 11:03
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

import user
from flask import Flask


app = Flask(__name__)
app.register_blueprint(user.bp)
