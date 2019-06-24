#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test5.py
@Time    :   2018/12/24 20:24:14
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def stu_info(*args, **kwargs): # 固定按照这种顺序放 O98K
    print(args)
    print(kwargs)
    for i in kwargs:
        print("%s: %s" % (i, kwargs[i]))

# **kwargs转换成字典
# 不能写一个单的再写一个键值对再写一个单的再写一个键值对
stu_info("zhouzhou", 18, "male", job="IT", hobby="pingpang")