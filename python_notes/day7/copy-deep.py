#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copy-deep.py
@Time    :   2018/12/23 16:14:56
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import copy

s = [[1,2], "zhouhua", "huahua"]
#s = copy.copy() #浅拷贝
s1 = copy.deepcopy(s)
print(s1)