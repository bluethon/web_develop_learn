#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-29 11:01
# @Author   : Bluethon (j5088794@gmail.com)
# @Link     : http://github.com/bluethon

from flask import Blueprint


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    return "User's Index Page"
