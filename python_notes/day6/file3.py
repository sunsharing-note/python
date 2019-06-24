#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file3.py
@Time    :   2018/12/19 21:26:45
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
# 读取文件用这个 用这种最好
f = open("test.txt", "r", encoding="utf8")
number = 0
for i in f:
    number += 1
    if number == 3:
        i = ''.join((i.strip(), "oooooooooo"))
    print(i.strip()) # 迭代器 用的时候就取一个 打开文件以后就用这种

f.close()