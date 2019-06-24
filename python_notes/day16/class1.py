#! /usr/bin/env python
# -*- coding: utf8 -*-

class Foo:
    def __init__(self, name,age):
        self.name = name
        self.__age = age # 私有 外部无法访问
    
obj = Foo("huahua",18)
print(obj.name)
print(obj.__age)  # 因为是私有 所以外部无法直接访问   