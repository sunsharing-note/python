#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

def test():
    print("ok")


data = pickle.dumps(test)

# wb b表示二进制
f = open("pickle.txt","wb")
f.write(data)
f.close()