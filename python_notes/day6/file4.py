#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file4.py
@Time    :   2018/12/19 21:43:37
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
f = open("test.txt", "r", encoding="utf8")

print(f.tell()) # 打印光标位置
print(f.read(10))
print(f.tell()) # tell区分中英文 中文占3个字节 英文占一个字节
f.seek(0) # seek 调整光标位置
#f.truncate() 不加参数就是从开始截断
print(f.tell())
print(f.read(5))
f.close()