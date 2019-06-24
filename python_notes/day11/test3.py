#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

def test():
    print("test1")
    count = yield 1
    print(count)

    yield 2

b = test()
#next(b)

s = b.send(None)
print(s)
k = b.send("ttest2")
print(k)
