#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test3.py
@Time    :   2018/12/25 20:59:55
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

def f(n):
    return n * n

def foo(a, b, func):
    ret = func(a) + func(b)
    return ret
print(foo(1, 2, f))
print(f)