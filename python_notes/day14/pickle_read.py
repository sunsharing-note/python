#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pickle

f = open("pickle.txt","rb")

data = pickle.loads(f.read())

f.close()

data()

# 内存发生了变化 所以无法读取
