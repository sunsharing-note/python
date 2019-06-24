#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file1.py
@Time    :   2018/12/19 20:05:59
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
'''
r只可读，
w只可写 #先清空，再写
r+ 读写模式 w+ 写读模式 a+ 追加模式
'''

# here put the import lib

f = open("test1.txt", "a", encoding="utf8") #没有test1.txt 会创建 f就成为文件操作的句柄
#data = f.read(5) # 5个字符
#data = f.read(5)
#print(data)
f.write("\n离离原上草") #在对象存在时就已经被清空了
#f.write("我爱家乡\n") #如果两个都写的话 这样子不换行显示俩
#f.write("1")
f.close()