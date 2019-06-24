#! /usr/bin/env python
# -*- coding: utf8 -*-

from multiprocessing import Process

import time

def f(name):
    time.sleep(1)
    print("hello",name,time.ctime())

if __name__ == "__name__":
    p_list = []
    for i in range(3):
        p = Process(target=f,args=("alven",))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print("end")