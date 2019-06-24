#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   set1.py
@Time    :   2018/12/23 18:36:39
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])

print(a.intersection(b))#交集
print(a & b)
print(a.union(b))#并集
print(a | b)
print(a.difference(b))#差集
print(a - b)
print(a.symmetric_difference(b))#对称差集 两边都没有的
print(a ^ b)
print(a.issuperset(b))#a完全包含b?
print(a.issubset(b))#a被b完全包含？