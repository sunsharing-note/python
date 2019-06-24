#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

# 找到mod1.py文件时，将其代码均解释然后给mod1
# import mod1
# import sys

# print(sys.path)
# print(mod1.add(2, 4))

# 当mod1中有很多函数时 可以使用from mode_name import function_name[fun1,func2]
# 从模块里调用方法 只会加载add 其他的不会
# from mod1 import add

# print(add(1, 4))

# 这样子 里面所有的都会被解释和加载
# from mod1 import * #这种不推荐 有可能会重复


# def add(a,b):
#     return a + b + 3

# # 如果遇到这种方法重复的 以顺序来区分 谁在后面就以谁为准
# print(add(1,3))


from mod1 import add as test

print(test(1, 2))
