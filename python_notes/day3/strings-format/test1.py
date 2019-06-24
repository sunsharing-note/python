#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2018/12/15 15:30:18
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

name = input("name: ")
sex = input("sex: ")
age = int(input("age: "))
salary = input("salary: ")


if salary.isdigit(): #判断是否类似数字
    salary = int(salary)
else:
'''    print("must input digit")
    exit()'''
    exit("must input digit")
msg = '''
--------infor of %s------------
name: %s
sex: %s
age: %s
salary: %s
---------the end-----------------
''' % (name, name, sex, age, salary)

print(msg)