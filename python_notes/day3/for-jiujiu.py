#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   for-jiujiu.py
@Time    :   2018/12/15 16:39:32
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

#包括开头不包括结尾
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + "*" + str(i) + "=" + str(j * i), end="\t")
    print()
    