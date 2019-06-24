#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file2.py
@Time    :   2018/12/19 20:47:36
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

f = open("test.txt", "r", encoding="utf8")
#data = f.readline()
#print(f.readline()) # 这一行读完之后，光标已经移动到了最后 read的光标也会移动
#print(f.readline())
#print(f.readlines()) # 返回一个列表(list)
data = f.readlines()
f.close()
number = 0
for i in data:
    number += 1
    if number == 3:
        i = ''.join((i.strip(), "oooooooooo"))#用元组和列表都行
    print(i.strip())
