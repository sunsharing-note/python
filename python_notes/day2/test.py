#! /usr/bin/env python
# _*_ coding: utf-8 _*_

a = 20
b = 19
c = 21
max = 0
if a > b:
    max = a
    if max > c:
        print("max is ", max)
    else:
        print("max is ", c)
else:
    max = b
    if max > c:
        print("max is ", max)
    else:
        print("max is ", c)