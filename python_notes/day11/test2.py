#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

def f(): # f()这里是生成器对象
    print("test1")
    yield 1
    print("test2")
    yield 2


g = f()

#next(g)
#next(g)
for i in g: # for循环会去调用next
    print(i) # 1,2为返回值
