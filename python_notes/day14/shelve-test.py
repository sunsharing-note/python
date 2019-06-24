#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shelve

# 字典的值必须为字符串
f = shelve.open("shelve.txt")

# 写数据
# f["name"] = "zhouzhou"

# 读取数据
print(f.get("name"))

# 假如没有那个键 可设置一个默认值，如下所示
# print(f.get("name","huahua")