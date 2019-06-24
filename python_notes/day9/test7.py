#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test7.py
@Time    :   2018/12/25 21:50:36
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from  functools import reduce
def add(x, y):
    return x + y
print(reduce(add, range(1, 101))) # 先传1，2 再传3，3 再传4，4 累加