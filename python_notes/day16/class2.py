#! /usr/bin/env python
# -*- coding: utf8 -*-

class Foo:
    def __init__(self):
        print("init")
    def __call__(self,*args,**kwargs):
        print("call")

obj = Foo()
obj()

"""
int("1234") 内部会去调用__int__方法
"""