#! /usr/bin/env python
# _*_ coding: utf-8 _*_


# input接收的所有数据都是字符串，即便输入的是整数，还是会被当做字符串处理
a = 100
age = input("请输入你的年龄: ")
type_age = type(age)
print("test ", 100-int(age), " test test")


print("test " + str(100-int(age)) + " test test")