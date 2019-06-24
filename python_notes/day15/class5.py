#!/usr/bin/env python
# -*- coding: utf-8 -*-
class F0:
    def a(self):
        print("F0.a")

class F1(F0):
    def a(self):
        print("F1.a")
class F2:
    def a(self):
        print("F2.a")

class s(F1,F2): # 谁在前面就执行谁 并且一条道走到黑(如果方法没有，就一直往下找)
    pass        # 但是如果F1 F2有共同的根 则不会一条道走到黑 在执行后面一个时才会找到根

s = s()
s.a()