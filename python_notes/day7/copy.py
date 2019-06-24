#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copy.py
@Time    :   2018/12/23 15:12:37
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
a = [1, "huahua", "zhouzhou"]
b = a.copy()
print(b)
b[0] = 2
print(a)
print(b)