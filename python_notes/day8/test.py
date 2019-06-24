#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2018/12/23 21:19:16
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def jiujiu():
    line = 1

    while line <= 9:
        column = 1
        while column <= line:
            print(str(column) + "*" + str(line) + "=" + str((column * line)), end="\t")
            column += 1
        print()
        line += 1
jiujiu()
print(jiujiu)