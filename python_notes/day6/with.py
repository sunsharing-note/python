#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   with.py
@Time    :   2018/12/21 22:46:23
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
#f = open("test.txt", "r", encoding="utf8")

# 同时管理多个文件对象
with open("test.txt", "r", encoding="utf8") as f, open("test1.txt", "w", encoding="utf8") as f1:
    pass
