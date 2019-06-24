#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test8.py
@Time    :   2018/12/25 21:58:31
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from functools import reduce

print(reduce(lambda x,y: x * y, range(1, 6)))