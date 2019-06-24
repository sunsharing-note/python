#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test10.py
@Time    :   2018/12/26 14:27:36
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)

print(f(5))