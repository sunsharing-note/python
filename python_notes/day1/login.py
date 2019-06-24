#! /usr/bin/env python
# _*_ coding: utf-8 _*_

user_name = "admin"
user_pass = "123456"

login_user_name = input("请输入用户名：")
login_user_pass = input("请输入密码：")


if login_user_name == user_name and login_user_pass == user_pass:
    print("welcome")
else:
    print("账号或密码错误")
    login_user_name = input("请输入用户名：")
    login_user_pass = input("请输入密码：")