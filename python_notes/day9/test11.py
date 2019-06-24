#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test12.py
@Time    :   2018/12/26 14:56:09
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def fibo(n):
    if n <= 2:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(8))