#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import threading

begin = time.time()

def foo(n):
    print("foo%s"%n)
    time.sleep(1)
    print("end foo")

def bar(n):
    print("bar%s"%n)
    time.sleep(2)
    print("end bar")
# foo()
# bar()

# end = time.time()
# print(end-begin)

t1 = threading.Thread(target=foo,args=(1,))

t2 = threading.Thread(target=bar,args=(2,))
t1.start()
t2.start()

print(".......main..........")

t1.join() # 创建并发
t2.join() # 创建并发

end = time.time()

print(end-begin)