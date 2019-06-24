#! /usr/bin/env python
# -*- coding: utf8 -*-

class myType(type):
    def __init__(self,*args,**kwargs):
        print(1234)
        pass
    def __call__(self, *args, **kwargs): # self指的是Foo类
        r = self.__new__(self,*args, **kwargs)

class Foo(object,metaclass=myType):
    def func(self):
        print("xxxxxxx")
    def __init__(self, *args, **kwargs):
        pass
    def __new__(cls,*args, **kwargs): # cls创建Foo的对象
        return "1234"

obj = Foo()

# 程序在读到Class Foo时，遇到了metaclass，先执行myType的init，在执行到obj=Foo(),执行myType的call，再执行Foo的__new__,
# 在执行Foo的__init__
