#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file5.py
@Time    :   2018/12/21 22:22:58
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
f_read = open("test.txt", "r", encoding="utf8")
f_write = open("test1.txt", "w", encoding="utf8")


number = 0
for line in f_read:
    number += 1
    if number == 3:
        line = "hello wold\n"
    f_write.write(line)
f_read.close()
f_write.close()