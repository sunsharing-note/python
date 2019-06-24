#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import time

# 装饰器
def show_time(f):
    def  inner(*a, **b):
        start = time.time()
        f(*a, **b)
        end = time.time()
        print("spent %s" % (end-start))
    return inner
@show_time

def foo(*a, **b):
    sum = 0
    for i in a:
        sum += i
    print(sum)
    time.sleep(2)
#foo = show_time(foo)
foo(1, 2, 5, 7,9)