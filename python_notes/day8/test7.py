#! /usr/bin/env python
# -*- coding: utf8 -*-

x = int(5.8) #built-in

y = 0 # global

def outer():
    count = 1 # enclosing
    def inner():
        i_count = 2 #local
        print(i_count)
    inner()

outer()

count = 10
def count():
    global count
#  count = count + 1
    count = 5
    print(count)
count()
# 全局的count不允许你修改 所以这里会报错 如果添加global则可以
# 如果变量不是全局范围，则可以使用nonlocal python3新增关键字
