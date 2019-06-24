#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

# 字符串提供的是完全匹配
s = "hello world"
print(s.find("ll")) # 返回ll所在下标

t = s.replace("ll", "xx")
print(t)

print(s.split(" "))
print(s.split("w"))