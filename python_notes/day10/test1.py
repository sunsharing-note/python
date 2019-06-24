#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import time

def foo():
    start = time.time()
    print("test")
    time.sleep(1)
    end = time.time()
    print("spend %s" % (end-start))

foo()