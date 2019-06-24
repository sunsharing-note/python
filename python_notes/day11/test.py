#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

a = [x * 2 for x in range(10)]
print(a)


def f(n):
    return n ** 3


b = [f(x) for x in range(10)]

print(b)