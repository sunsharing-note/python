#! /usr/bin/env python
# -*- coding: utf-8 -*-


import queue

q = queue.Queue(maxsize=3)

q.put("zhouzhou")
q.put("huahua")
q.put("xiyagxixia")

# 这里是谁先进 就谁先出

print(q.get())
print(q.get())
print(q.get())
