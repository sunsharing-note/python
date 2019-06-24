#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test9.py
@Time    :   2018/12/26 14:25:01
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def f(n):
    
    ret = 1
    for i in range(1, n + 1):
        ret = ret * i
    return ret

print(f(5))