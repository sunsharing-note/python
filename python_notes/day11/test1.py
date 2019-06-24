#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

a = (x * 2 for x in range(10))

'''
print(a)

b = a.__next__()
c = next(a) # 尽量用这个 不用系统自带的内置函数
print(b)
print(c)
'''
for i  in a:
    print(i)