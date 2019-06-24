#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test4.py
@Time    :   2018/12/24 20:20:03
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4,5)