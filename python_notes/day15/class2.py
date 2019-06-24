#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 封装
class foo:
    def test(self,content):
        print(self.name,self.sex,content)

obj = foo()

obj.name = "huahua"
obj.sex = "male"

obj.test("hahaha")
obj.test("fanfanfan")