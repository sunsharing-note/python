#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2018/12/15 16:02:58
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

_user = "admin"
_password = "abcd1234"

count = 0
while True:
    userName = input("请输入用户名：")
    password = input("请输入密码：")
    
    if userName == _user and password == _password:
        print("yes")
        break  #可以添加一个判断是否成功的变量flag进行标记
    else:
        print("your user or password is invalid")
    count += 1
    if count > 2:
        exit("your user is locked")  
