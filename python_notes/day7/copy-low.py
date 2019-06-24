#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copy-low.py
@Time    :   2018/12/23 15:26:29
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
s = [[1,2], "zhouhua", "huahua"]
s1 = s.copy()
print(s)
print(s1)

#浅copy指copy第一层
s1[0][1] = 10
print(s1)
print(s) #因为s1[0]中存储的指向2的内存地址发生了改变，现在指向了10 所以改了s1，也影响了s
