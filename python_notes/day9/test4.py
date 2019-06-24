#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test4.py
@Time    :   2018/12/25 21:32:04
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
## print(all('12345 6'))
# print(eval('1+3*2'))
str = ["a", "b", "c"]

def fun(s):
    if s != "a":
        return s
ret = filter(fun, str) # 过滤器 返回的是过滤后的
print(ret)
print(list(ret))