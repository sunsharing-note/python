#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test5.py
@Time    :   2018/12/25 21:22:13
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def f():
    def inner():
        return 8
    return inner
print(f())