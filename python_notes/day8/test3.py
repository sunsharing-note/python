#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test3.py
@Time    :   2018/12/24 20:07:45
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
def stu_info(name, age, sex="male"):
    print("Name: %s" % name)
    print("Age: %d" % age)
    print("Sex: %s" % sex)

stu_info("zhouzhou", 18)
stu_info("huahua", 20, "female")