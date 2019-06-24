#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test6.py
@Time    :   2018/12/25 21:42:35
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
str = ["a", "b", "c"]
def fun(s):
    return s + "zhouzhou"
ret = map(fun, str)

print(ret)
print(list(ret))

ret = filter(fun, str) # 不满足条件 直接过滤

print(ret)
print(list(ret))