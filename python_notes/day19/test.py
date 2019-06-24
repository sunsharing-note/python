#! /usr/bin/env python
# -*- coding: utf-8 -*-



import threading
import time

def addNum():
    global num
    # 加锁
    r.acquire()
    # num -= 1
    temp = num
    time.sleep(0.01)
    num = temp - 1
    # 释放锁
    r.release()


num = 100

thread_list = []
r = threading.Lock()
for i in  range(100):
    t = threading.Thread(target=addNum)
    # t1 = threading.BoundedSemaphore(5) # 信号量
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print("final num:", num)

