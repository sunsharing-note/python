#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import time

def logger(flag=""):
# 装饰器
    def show_time(f):
        def  inner(*a, **b):
            start = time.time()
            f(*a, **b)
            end = time.time()
            print("spent %s" % (end-start))
            if flag == "true":
                print("日志记录")
        return inner
    return show_time
#@show_time
@logger("true")

def foo(*a, **b):
    sum = 0
    for i in a:
        sum += i
    print(sum)
    time.sleep(2)
#foo = show_time(foo)
foo(1, 2, 5, 7,9)