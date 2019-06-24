#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   set.py
@Time    :   2018/12/23 16:27:23
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
s = set("huahuazhouzhou")

print("h" in s)
s.add("uu") #当成一个整体加进去
print(s)
s.update("test") #添加内容到之前的内容 当作序列 每一个都会添加
print(s)
s.update("ooooooooooo")
print(s)
s.update([100, "amei"])
print(s)
#print(type(s))

# 去重
#print(s)