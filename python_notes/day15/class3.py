#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 封装到init方法中
class foo:
    # 静态字段 在内存中只保留一份
    country = "中国"
    # 初始化
    def __init__(self,name,sex):
        # 普通字段
        self.name = name
        self.sex = sex
        self.blood = "o"
    # 方法
    def test(self,content):
        print(self.name,self.sex,self.blood,content)

obj = foo("huahua","male") # 自动执行init方法
obj.test("xxxxxxxxx")

print(obj.country)
print(foo.country)
