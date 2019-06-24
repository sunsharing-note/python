#!/usr/bin/env python
# -*- coding: utf-8 -*-

class father: # 父类 基类
    def test1(self,name,sex):
        print(name,sex)
    def test2(self,phone):
        print(phone+"xxxxx")


class son(father): # 子类 派生类
    def test2(self,phone): # 重写
        print(phone)
        # 既执行父类的方法 也执行子类的方法
        super(son, self).test2(phone)
        #father.test2(self,phone)

s = son()
s.test2("13330393313")
s.test1("huahua","male")