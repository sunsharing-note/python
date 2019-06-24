#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import web.logger这样子调用不行
# from web import logger  # web/logger
# from web.web2 import logger # 多层 web/web2/logger
# 用这种也行

# import web 是去调用web下的__init__.py
# from web.web2.logger import logger

# logger()

# basedir
import os,sys
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))