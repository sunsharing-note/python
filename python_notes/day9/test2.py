#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test2.py
@Time    :   2018/12/25 20:21:53
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def f(**kwargs):
    print(kwargs)

f(**{"name": "huahua", "sex": "male"})