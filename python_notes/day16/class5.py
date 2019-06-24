#! /usr/bin/env python
# -*- coding: utf8 -*-


class Zhou:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Zhou("zhouzhou",19)

# print(obj.name)

# b = "name"

r = getattr(obj,"name")
print(r)

